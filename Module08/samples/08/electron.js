const { app, BrowserWindow, Menu, ipcMain, shell, dialog, nativeTheme } = require('electron');
const { autoUpdater } = require('electron-updater');
const windowStateKeeper = require('electron-window-state');
const Store = require('electron-store');
const path = require('path');
const { FoundryLocalManager } = require('foundry-local-sdk');
const OpenAI = require('openai');
const { v4: uuidv4 } = require('uuid');

// Enable live reload for development
if (process.env.NODE_ENV === 'development') {
  require('electron-debug')();
}

// Initialize persistent store
const store = new Store({
  defaults: {
    theme: 'system',
    model: 'phi-4-mini',
    streaming: true,
    maxTokens: 1000,
    temperature: 0.7,
    windowBounds: { width: 1200, height: 800 },
    conversations: [],
    settings: {
      notifications: true,
      autoSave: true,
      modelAutoLoad: true
    }
  }
});

// Global variables
let mainWindow;
let foundryManager;
let openaiClient;
let currentModel = null;
let isFoundryServiceRunning = false;

// Foundry Local Manager Setup
async function initializeFoundryLocal() {
  try {
    console.log('Initializing Foundry Local...');
    foundryManager = new FoundryLocalManager();
    
    // Check if service is running
    if (!foundryManager.isServiceRunning()) {
      console.log('Starting Foundry Local service...');
      await foundryManager.startService();
    }
    
    isFoundryServiceRunning = true;
    
    // Load default model
    const defaultModel = store.get('model', 'phi-4-mini');
    if (store.get('settings.modelAutoLoad', true)) {
      await loadModel(defaultModel);
    }
    
    console.log('Foundry Local initialized successfully');
    return true;
    
  } catch (error) {
    console.error('Failed to initialize Foundry Local:', error);
    isFoundryServiceRunning = false;
    return false;
  }
}

async function loadModel(modelAlias) {
  try {
    console.log(`Loading model: ${modelAlias}`);
    const modelInfo = await foundryManager.init(modelAlias);
    
    // Initialize OpenAI client with Foundry Local endpoint
    openaiClient = new OpenAI({
      baseURL: foundryManager.endpoint,
      apiKey: foundryManager.apiKey
    });
    
    currentModel = {
      alias: modelAlias,
      info: modelInfo,
      endpoint: foundryManager.endpoint
    };
    
    console.log(`Model loaded successfully: ${modelInfo.id}`);
    
    // Notify renderer
    if (mainWindow) {
      mainWindow.webContents.send('model-loaded', currentModel);
    }
    
    return modelInfo;
    
  } catch (error) {
    console.error(`Failed to load model ${modelAlias}:`, error);
    throw error;
  }
}

// Window Management
function createMainWindow() {
  // Load window state
  let mainWindowState = windowStateKeeper({
    defaultWidth: 1200,
    defaultHeight: 800
  });
  
  // Create browser window
  mainWindow = new BrowserWindow({
    x: mainWindowState.x,
    y: mainWindowState.y,
    width: mainWindowState.width,
    height: mainWindowState.height,
    minWidth: 800,
    minHeight: 600,
    show: false,
    titleBarStyle: 'hidden',
    titleBarOverlay: {
      color: '#00000000',
      symbolColor: '#74b1be',
      height: 32
    },
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      enableRemoteModule: false,
      preload: path.join(__dirname, 'preload.js'),
      webSecurity: true,
      allowRunningInsecureContent: false
    },
    frame: false,
    transparent: false,
    backgroundColor: nativeTheme.shouldUseDarkColors ? '#1e1e1e' : '#f5f5f5',
    icon: path.join(__dirname, 'build/icon.ico')
  });
  
  // Let windowStateKeeper manage the window
  mainWindowState.manage(mainWindow);
  
  // Load the app
  mainWindow.loadFile('src/index.html');
  
  // Window event handlers
  mainWindow.once('ready-to-show', () => {
    mainWindow.show();
    
    // Focus window on creation
    if (process.platform === 'win32') {
      mainWindow.focus();
    }
  });
  
  mainWindow.on('closed', () => {
    mainWindow = null;
  });
  
  // Handle external links
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });
  
  // Development tools
  if (process.env.NODE_ENV === 'development') {
    mainWindow.webContents.openDevTools();
  }
  
  return mainWindow;
}

// IPC Handlers
function setupIpcHandlers() {
  
  // Window controls
  ipcMain.handle('window-minimize', () => {
    mainWindow?.minimize();
  });
  
  ipcMain.handle('window-maximize', () => {
    if (mainWindow?.isMaximized()) {
      mainWindow.unmaximize();
    } else {
      mainWindow?.maximize();
    }
  });
  
  ipcMain.handle('window-close', () => {
    mainWindow?.close();
  });
  
  // Application state
  ipcMain.handle('get-app-info', () => {
    return {
      version: app.getVersion(),
      platform: process.platform,
      foundryStatus: isFoundryServiceRunning,
      currentModel: currentModel,
      theme: nativeTheme.themeSource
    };
  });
  
  // Settings management
  ipcMain.handle('get-settings', () => {
    return store.store;
  });
  
  ipcMain.handle('update-settings', (event, settings) => {
    Object.keys(settings).forEach(key => {
      store.set(key, settings[key]);
    });
    
    // Apply theme changes
    if (settings.theme) {
      nativeTheme.themeSource = settings.theme;
    }
    
    return store.store;
  });
  
  // Model management
  ipcMain.handle('load-model', async (event, modelAlias) => {
    try {
      const modelInfo = await loadModel(modelAlias);
      store.set('model', modelAlias);
      return { success: true, model: modelInfo };
    } catch (error) {
      return { success: false, error: error.message };
    }
  });
  
  ipcMain.handle('list-available-models', async () => {
    try {
      if (!foundryManager) {
        return { success: false, error: 'Foundry Local not initialized' };
      }
      
      const models = await foundryManager.listCatalogModels();
      return { 
        success: true, 
        models: models.map(model => ({
          id: model.id,
          name: model.name || model.id,
          alias: model.alias,
          size: model.fileSizeMb || 0,
          provider: model.providerType || 'unknown'
        }))
      };
    } catch (error) {
      return { success: false, error: error.message };
    }
  });
  
  ipcMain.handle('list-cached-models', async () => {
    try {
      if (!foundryManager) {
        return { success: false, error: 'Foundry Local not initialized' };
      }
      
      const models = await foundryManager.listCachedModels();
      return { success: true, models };
    } catch (error) {
      return { success: false, error: error.message };
    }
  });
  
  // Chat functionality
  ipcMain.handle('send-message', async (event, messageData) => {
    try {
      if (!openaiClient || !currentModel) {
        throw new Error('No model loaded');
      }
      
      const { messages, options = {} } = messageData;
      const conversationId = options.conversationId || uuidv4();
      
      // Store message in conversation history
      const conversation = getOrCreateConversation(conversationId);
      
      const requestOptions = {
        model: currentModel.info.id,
        messages: messages,
        max_tokens: options.maxTokens || store.get('maxTokens', 1000),
        temperature: options.temperature || store.get('temperature', 0.7),
        stream: options.stream !== false && store.get('streaming', true)
      };
      
      if (requestOptions.stream) {
        return { success: true, conversationId, streaming: true };
      } else {
        const response = await openaiClient.chat.completions.create(requestOptions);
        const assistantMessage = response.choices[0].message.content;
        
        // Store response in conversation
        conversation.messages.push(...messages);
        conversation.messages.push({
          role: 'assistant',
          content: assistantMessage,
          timestamp: Date.now()
        });
        saveConversation(conversation);
        
        return { 
          success: true, 
          conversationId,
          response: assistantMessage,
          usage: response.usage
        };
      }
      
    } catch (error) {
      console.error('Error sending message:', error);
      return { success: false, error: error.message };
    }
  });
  
  ipcMain.handle('stream-message', async (event, messageData) => {
    try {
      if (!openaiClient || !currentModel) {
        throw new Error('No model loaded');
      }
      
      const { messages, options = {} } = messageData;
      const conversationId = options.conversationId || uuidv4();
      
      const conversation = getOrCreateConversation(conversationId);
      conversation.messages.push(...messages);
      
      const requestOptions = {
        model: currentModel.info.id,
        messages: messages,
        max_tokens: options.maxTokens || store.get('maxTokens', 1000),
        temperature: options.temperature || store.get('temperature', 0.7),
        stream: true
      };
      
      const stream = await openaiClient.chat.completions.create(requestOptions);
      let fullResponse = '';
      
      for await (const chunk of stream) {
        const content = chunk.choices[0]?.delta?.content || '';
        if (content) {
          fullResponse += content;
          mainWindow.webContents.send('chat-chunk', {
            conversationId,
            content,
            fullResponse
          });
        }
      }
      
      // Store complete response
      conversation.messages.push({
        role: 'assistant',
        content: fullResponse,
        timestamp: Date.now()
      });
      saveConversation(conversation);
      
      mainWindow.webContents.send('chat-complete', {
        conversationId,
        fullResponse
      });
      
      return { success: true, conversationId };
      
    } catch (error) {
      console.error('Error streaming message:', error);
      mainWindow.webContents.send('chat-error', {
        error: error.message
      });
      return { success: false, error: error.message };
    }
  });
  
  // Conversation management
  ipcMain.handle('get-conversations', () => {
    return store.get('conversations', []);
  });
  
  ipcMain.handle('get-conversation', (event, conversationId) => {
    const conversations = store.get('conversations', []);
    return conversations.find(conv => conv.id === conversationId);
  });
  
  ipcMain.handle('save-conversation', (event, conversation) => {
    return saveConversation(conversation);
  });
  
  ipcMain.handle('delete-conversation', (event, conversationId) => {
    const conversations = store.get('conversations', []);
    const filteredConversations = conversations.filter(conv => conv.id !== conversationId);
    store.set('conversations', filteredConversations);
    return true;
  });
  
  // Health check
  ipcMain.handle('health-check', async () => {
    try {
      if (!foundryManager) {
        return { 
          success: false, 
          status: 'not-initialized',
          error: 'Foundry Local not initialized'
        };
      }
      
      const isRunning = foundryManager.isServiceRunning();
      const cachedModels = await foundryManager.listCachedModels();
      
      return {
        success: true,
        status: isRunning ? 'running' : 'stopped',
        endpoint: foundryManager.endpoint,
        currentModel: currentModel,
        cachedModels: cachedModels.length,
        memoryUsage: process.memoryUsage()
      };
    } catch (error) {
      return { 
        success: false, 
        status: 'error',
        error: error.message
      };
    }
  });
}

// Conversation helpers
function getOrCreateConversation(conversationId) {
  const conversations = store.get('conversations', []);
  let conversation = conversations.find(conv => conv.id === conversationId);
  
  if (!conversation) {
    conversation = {
      id: conversationId,
      title: 'New Conversation',
      messages: [],
      createdAt: Date.now(),
      updatedAt: Date.now()
    };
    conversations.push(conversation);
    store.set('conversations', conversations);
  }
  
  return conversation;
}

function saveConversation(conversation) {
  const conversations = store.get('conversations', []);
  const index = conversations.findIndex(conv => conv.id === conversation.id);
  
  conversation.updatedAt = Date.now();
  
  // Generate title from first user message if not set
  if (conversation.title === 'New Conversation' && conversation.messages.length > 0) {
    const firstUserMessage = conversation.messages.find(msg => msg.role === 'user');
    if (firstUserMessage) {
      conversation.title = firstUserMessage.content.substring(0, 50) + '...';
    }
  }
  
  if (index >= 0) {
    conversations[index] = conversation;
  } else {
    conversations.push(conversation);
  }
  
  store.set('conversations', conversations);
  return conversation;
}

// App Event Handlers
app.whenReady().then(async () => {
  // Initialize Foundry Local
  await initializeFoundryLocal();
  
  // Setup IPC handlers
  setupIpcHandlers();
  
  // Create main window
  createMainWindow();
  
  // Setup menu
  if (process.platform === 'darwin') {
    const template = [
      {
        label: app.getName(),
        submenu: [
          { role: 'about' },
          { type: 'separator' },
          { role: 'services' },
          { type: 'separator' },
          { role: 'hide' },
          { role: 'hideothers' },
          { role: 'unhide' },
          { type: 'separator' },
          { role: 'quit' }
        ]
      },
      {
        label: 'Edit',
        submenu: [
          { role: 'undo' },
          { role: 'redo' },
          { type: 'separator' },
          { role: 'cut' },
          { role: 'copy' },
          { role: 'paste' },
          { role: 'selectall' }
        ]
      },
      {
        label: 'View',
        submenu: [
          { role: 'reload' },
          { role: 'forceReload' },
          { role: 'toggleDevTools' },
          { type: 'separator' },
          { role: 'resetZoom' },
          { role: 'zoomIn' },
          { role: 'zoomOut' },
          { type: 'separator' },
          { role: 'togglefullscreen' }
        ]
      },
      {
        label: 'Window',
        submenu: [
          { role: 'minimize' },
          { role: 'close' }
        ]
      }
    ];
    
    const menu = Menu.buildFromTemplate(template);
    Menu.setApplicationMenu(menu);
  } else {
    Menu.setApplicationMenu(null);
  }
  
  // Check for updates
  if (process.env.NODE_ENV === 'production') {
    autoUpdater.checkForUpdatesAndNotify();
  }
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createMainWindow();
  }
});

app.on('before-quit', async () => {
  // Cleanup
  if (foundryManager) {
    try {
      // Optionally stop service or unload models
      console.log('Cleaning up Foundry Local resources...');
    } catch (error) {
      console.error('Error during cleanup:', error);
    }
  }
});

// Auto-updater events
autoUpdater.on('checking-for-update', () => {
  console.log('Checking for update...');
});

autoUpdater.on('update-available', (info) => {
  console.log('Update available.');
});

autoUpdater.on('update-not-available', (info) => {
  console.log('Update not available.');
});

autoUpdater.on('error', (err) => {
  console.log('Error in auto-updater. ' + err);
});

autoUpdater.on('download-progress', (progressObj) => {
  let log_message = "Download speed: " + progressObj.bytesPerSecond;
  log_message = log_message + ' - Downloaded ' + progressObj.percent + '%';
  log_message = log_message + ' (' + progressObj.transferred + "/" + progressObj.total + ')';
  console.log(log_message);
});

autoUpdater.on('update-downloaded', (info) => {
  console.log('Update downloaded');
  autoUpdater.quitAndInstall();
});

// Handle certificate errors
app.on('certificate-error', (event, webContents, url, error, certificate, callback) => {
  // For development, allow self-signed certificates
  if (process.env.NODE_ENV === 'development') {
    event.preventDefault();
    callback(true);
  } else {
    callback(false);
  }
});

// Prevent navigation to external URLs
app.on('web-contents-created', (event, contents) => {
  contents.on('will-navigate', (event, navigationUrl) => {
    const parsedUrl = new URL(navigationUrl);
    
    if (parsedUrl.origin !== 'file://' && parsedUrl.origin !== 'http://localhost') {
      event.preventDefault();
    }
  });
});

console.log('Foundry Local Chat - Main process initialized');