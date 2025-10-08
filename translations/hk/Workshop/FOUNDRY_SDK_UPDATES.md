<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "fe36fce800723cb67570f9fc16497d86",
  "translation_date": "2025-10-08T16:14:17+00:00",
  "source_file": "Workshop/FOUNDRY_SDK_UPDATES.md",
  "language_code": "hk"
}
-->
# Foundry Local SDK 更新

## 概覽

更新了 Workshop 筆記本和工具，以正確使用 **官方 Foundry Local Python SDK**，遵循以下模式：
- https://github.com/microsoft/Foundry-Local
- https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local

## 修改的文件

### 1. `Workshop/samples/workshop_utils.py`

**更改內容：**
- ✅ 新增 `foundry-local-sdk` 套件的導入錯誤處理
- ✅ 使用官方 SDK 模式增強文件
- ✅ 使用 Unicode 符號（✓, ✗, ⚠）改進日誌記錄
- ✅ 添加包含範例的詳細註解
- ✅ 改進的錯誤訊息，參考 CLI 命令
- ✅ 更新註解以匹配官方 SDK 文件

**主要改進：**

#### 導入錯誤處理
```python
try:
    from foundry_local import FoundryLocalManager
except ImportError:
    raise ImportError(
        "foundry-local-sdk is required. Install with: pip install foundry-local-sdk"
    )
```

#### 增強的 `get_client()` 函數
- 添加有關 SDK 初始化模式的詳細文件
- 說明 `FoundryLocalManager` 自動啟動服務
- 解釋模型別名解析為硬件優化版本
- 改進的日誌記錄，包含端點資訊
- 更好的錯誤訊息，提供故障排除建議

#### 增強的 `chat_once()` 函數
- 添加包含使用範例的詳細註解
- 說明 OpenAI SDK 的相容性
- 記錄流式支援（通過 kwargs）
- 改進的錯誤訊息，提供 CLI 命令建議
- 添加有關模型可用性檢查的說明

### 2. `Workshop/notebooks/session06_models_router.ipynb`

**更改內容：**
- ✅ 更新所有 markdown 單元格，加入 SDK 參考
- ✅ 使用 SDK 模式解釋增強代碼註解
- ✅ 改進單元格文件和解釋
- ✅ 添加故障排除指導
- ✅ 更新模型目錄（將 'gpt-oss-20b' 替換為 'phi-3.5-mini'）
- ✅ 使用視覺指示器改進輸出格式
- ✅ 在整個筆記本中添加 SDK 連結和參考

**逐個單元格更新：**

#### 單元格 1（標題）
- 添加 SDK 文件連結
- 參考官方 GitHub 儲存庫

#### 單元格 2（場景）
- 使用編號步驟重新格式化
- 闡明基於意圖的路由模式
- 強調本地執行的優勢

#### 單元格 3（依賴安裝）
- 添加每個套件提供功能的解釋
- 記錄 SDK 功能（別名解析、硬件優化）

#### 單元格 4（環境設置）
- 增強函數註解
- 添加內聯註解，解釋 SDK 模式
- 記錄模型目錄結構
- 闡明優先級/能力匹配

#### 單元格 5（目錄檢查）
- 添加視覺檢查標記（✓）
- 更好地格式化輸出

#### 單元格 6（意圖檢測測試）
- 將輸出重新格式化為表格樣式
- 顯示意圖和選定模型

#### 單元格 7（路由函數）
- 全面的 SDK 模式解釋
- 記錄初始化流程
- 列出所有功能（重試、追蹤、錯誤）
- 添加 SDK 參考連結

#### 單元格 8（批量演示）
- 增強對預期結果的解釋
- 添加故障排除部分
- 包括用於調試的 CLI 命令
- 改進輸出顯示格式

### 3. `Workshop/notebooks/session06_README.md`（新文件）

**創建了涵蓋以下內容的全面文件：**

1. **概覽**：架構圖和組件解釋
2. **SDK 集成**：遵循官方模式的代碼範例
3. **先決條件**：逐步設置指導
4. **使用方法**：如何運行和自定義筆記本
5. **模型別名**：硬件優化版本的解釋
6. **故障排除**：常見問題和解決方案
7. **擴展**：如何添加意圖、模型和自定義邏輯
8. **性能提示**：生產環境的最佳實踐
9. **資源**：官方文件和社群連結

## SDK 模式實現

### 官方模式（來自 Foundry Local 文件）

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

# By using an alias, the most suitable model will be downloaded
alias = "phi-3.5-mini"

# Create a FoundryLocalManager instance
manager = FoundryLocalManager(alias)

# Configure the client to use the local Foundry service
client = OpenAI(
    base_url=manager.endpoint,
    api_key=manager.api_key
)

# Generate completion
stream = client.chat.completions.create(
    model=manager.get_model_info(alias).id,
    messages=[{"role": "user", "content": "What is AI?"}],
    stream=True
)
```

### 我們的實現（在 workshop_utils 中）

```python
def get_client(alias: str, endpoint: Optional[str] = None):
    """Initialize FoundryLocalManager and OpenAI client (with caching)"""
    # Initialize manager (starts service if needed)
    manager = FoundryLocalManager(alias, endpoint=endpoint) if endpoint else FoundryLocalManager(alias)
    
    # Create OpenAI-compatible client
    client = OpenAI(
        base_url=manager.endpoint,
        api_key=manager.api_key
    )
    
    # Resolve model ID
    model_id = manager.get_model_info(alias).id
    
    return manager, client, model_id

def chat_once(alias: str, messages: List[dict], **kwargs):
    """Execute chat completion with retry logic"""
    _, client, model_id = get_client(alias)
    resp = client.chat.completions.create(model=model_id, messages=messages, **kwargs)
    return resp.choices[0].message.content, resp.usage
```

**我們方法的優勢：**
- ✅ 完全遵循官方 SDK 模式
- ✅ 添加緩存以避免重複初始化
- ✅ 包括生產環境的重試邏輯
- ✅ 支援令牌使用追蹤
- ✅ 提供更好的錯誤訊息
- ✅ 與官方範例相容

## 模型目錄更改

### 更改前
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'gpt-oss-20b': {'capabilities':['code','refactor'],'priority':1},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':3},
}
```

### 更改後
```python
CATALOG = {
    'phi-4-mini': {'capabilities':['general','summarize'],'priority':2},
    'qwen2.5-0.5b': {'capabilities':['classification','fast'],'priority':1},
    'phi-3.5-mini': {'capabilities':['code','refactor'],'priority':3},
}
```

**原因：** 將 'gpt-oss-20b'（非標準別名）替換為 'phi-3.5-mini'（官方 Foundry Local 別名）。

## 依賴項

### 更新的 requirements.txt

Workshop 的 requirements.txt 已包含：
```
foundry-local-sdk
openai>=1.30.0
```

這些是 Foundry Local 集成所需的唯一套件。

## 測試更新

### 1. 驗證 Foundry Local 是否正在運行

```bash
# Windows
foundry service status

# If not running
foundry service start
```

### 2. 檢查可用模型

```bash
foundry model ls
```

確保這些模型可用或將自動下載：
- phi-4-mini
- phi-3.5-mini
- qwen2.5-0.5b

### 3. 運行筆記本

```bash
cd Workshop
jupyter notebook notebooks/session06_models_router.ipynb
```

或者在 VS Code 中打開並運行所有單元格。

### 4. 預期行為

**單元格 1（安裝）：** 成功安裝套件  
**單元格 2（設置）：** 無錯誤，導入成功  
**單元格 3（驗證）：** 顯示 ✓ 和模型列表  
**單元格 4（測試意圖）：** 顯示意圖檢測結果  
**單元格 5（路由器）：** 顯示 ✓ 路由函數準備就緒  
**單元格 6（執行）：** 將提示路由到模型，顯示結果  

### 5. 故障排除連接錯誤

如果您看到 `APIConnectionError: Connection error`：

```bash
# Check service
foundry service status

# Check endpoint
curl http://localhost:55769/health

# Restart if needed
foundry service stop
foundry service start
```

## 環境變數

支持以下環境變數：

| 變數 | 預設值 | 描述 |
|------|--------|------|
| `SHOW_USAGE` | `0` | 設置為 `1` 以打印令牌使用情況 |
| `RETRY_ON_FAIL` | `1` | 啟用重試邏輯 |
| `RETRY_BACKOFF` | `1.0` | 初始重試延遲（秒） |
| `FOUNDRY_LOCAL_ENDPOINT` | 自動 | 覆蓋服務端點 |

### 使用範例

```python
import os

# Enable token tracking
os.environ['SHOW_USAGE'] = '1'

# Adjust retry timing
os.environ['RETRY_BACKOFF'] = '2.0'

# Use custom endpoint
os.environ['FOUNDRY_LOCAL_ENDPOINT'] = 'http://localhost:8000'
```

## 從舊模式遷移

如果您有使用直接 API 調用的現有代碼，以下是遷移方法：

### 更改前（直接 API）
```python
import requests

response = requests.post(
    'http://localhost:8000/v1/chat/completions',
    json={
        'model': 'phi-4-mini',
        'messages': [{'role': 'user', 'content': 'Hello'}]
    }
)
```

### 更改後（SDK）
```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager('phi-4-mini')
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)

response = client.chat.completions.create(
    model=manager.get_model_info('phi-4-mini').id,
    messages=[{'role': 'user', 'content': 'Hello'}]
)
```

### 遷移的好處
- ✅ 自動服務管理
- ✅ 模型別名解析
- ✅ 硬件優化選擇
- ✅ 更好的錯誤處理
- ✅ 與 OpenAI SDK 相容
- ✅ 支援流式處理

## 參考資料

### 官方文件
- **Foundry Local GitHub**: https://github.com/microsoft/Foundry-Local  
- **Python SDK 原始碼**: https://github.com/microsoft/Foundry-Local/tree/main/sdk/python/foundry_local  
- **CLI 參考**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-cli.md  
- **REST API**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-rest.md  
- **故障排除**: https://github.com/microsoft/Foundry-Local/blob/main/docs/reference/reference-troubleshooting.md  

### Workshop 資源
- **Session 06 README**: `Workshop/notebooks/session06_README.md`  
- **Workshop 工具**: `Workshop/samples/workshop_utils.py`  
- **範例筆記本**: `Workshop/notebooks/session06_models_router.ipynb`  

### 社群
- **Discord**: https://aka.ms/foundry-local-discord  
- **GitHub 問題回報**: https://github.com/microsoft/Foundry-Local/issues  

## 下一步

1. **檢視更改：** 閱讀更新的文件  
2. **測試筆記本：** 運行 session06_models_router.ipynb  
3. **驗證 SDK：** 確保已安裝 foundry-local-sdk  
4. **檢查服務：** 確認 Foundry Local 正在運行  
5. **探索文件：** 閱讀新的 session06_README.md  

## 總結

這些更新確保 Workshop 資料完全遵循 **官方 Foundry Local SDK 模式**，與 GitHub 儲存庫中的文件一致。所有代碼範例、文件和工具現在都符合 Microsoft 推薦的本地 AI 模型部署最佳實踐。

這些更改改進了：
- ✅ **正確性：** 使用官方 SDK 模式  
- ✅ **文件：** 詳盡的解釋和範例  
- ✅ **錯誤處理：** 更好的訊息和故障排除指導  
- ✅ **可維護性：** 遵循官方慣例  
- ✅ **用戶體驗：** 更清晰的指導和調試幫助  

---

**更新日期：** 2025 年 10 月 8 日  
**SDK 版本：** foundry-local-sdk（最新）  
**Workshop 分支：** Reactor  

---

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。