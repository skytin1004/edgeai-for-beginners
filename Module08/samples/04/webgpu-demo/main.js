const statusEl = document.getElementById('status');
const outputEl = document.getElementById('output');
const metricsEl = document.getElementById('metrics');
const loadTimeEl = document.getElementById('load-time');
const inferenceTimeEl = document.getElementById('inference-time');
const predictionEl = document.getElementById('prediction');

function log(msg) {
    const timestamp = new Date().toLocaleTimeString();
    outputEl.textContent += `[${timestamp}] ${msg}\n`;
    outputEl.scrollTop = outputEl.scrollHeight;
    console.log(msg);
}

function updateStatus(message, type = 'info') {
    statusEl.textContent = message;
    statusEl.className = `status ${type}`;
}

function updateMetric(elementId, value) {
    document.getElementById(elementId).textContent = value;
}

(async () => {
    let startTime, endTime;
    
    try {
        // Step 1: WebGPU Detection
        log('🔍 Checking WebGPU availability...');
        
        if (!('gpu' in navigator)) {
            updateStatus('❌ WebGPU not available in this browser', 'error');
            log('❌ WebGPU not supported. Please use Chrome/Edge 113+ with WebGPU enabled.');
            log('💡 Check chrome://gpu to verify WebGPU status');
            log('🔄 Falling back to CPU execution...');
            
            // Continue with CPU fallback
            await runWithCPU();
            return;
        }
        
        log('✅ WebGPU API detected');
        updateStatus('🔍 WebGPU detected. Initializing ONNX Runtime...', 'success');
        
        // Step 2: ONNX Runtime Initialization
        log('📦 Initializing ONNX Runtime Web...');
        
        // Configure ONNX Runtime for WebGPU
        ort.env.wasm.wasmPaths = 'https://cdn.jsdelivr.net/npm/onnxruntime-web/dist/';
        
        log('🌐 Loading MNIST classification model...');
        updateStatus('📥 Loading AI model (MNIST classifier)...', 'info');
        
        startTime = performance.now();
        
        // Use a small, publicly available ONNX model
        const modelUrl = 'https://huggingface.co/onnx/models/resolve/main/vision/classification/mnist-12/mnist-12.onnx';
        
        // Create inference session with WebGPU
        const session = await ort.InferenceSession.create(modelUrl, {
            executionProviders: ['webgpu', 'wasm'], // WebGPU first, fallback to WASM
            graphOptimizationLevel: 'all'
        });
        
        endTime = performance.now();
        const loadTime = Math.round(endTime - startTime);
        
        log('✅ ONNX Runtime session created successfully');
        log(`⚡ Model loaded in ${loadTime}ms`);
        log(`📊 Execution provider: ${session.executionProviders.join(', ')}`);
        log(`🔧 Input names: [${session.inputNames.join(', ')}]`);
        log(`🔧 Output names: [${session.outputNames.join(', ')}]`);
        
        updateMetric('load-time', loadTime);
        updateStatus('🚀 Running inference on sample data...', 'info');
        
        // Step 3: Inference
        log('🎯 Creating sample input data (28x28 handwritten digit)...');
        
        // Create a sample input that resembles a handwritten digit
        const inputData = new Float32Array(1 * 1 * 28 * 28);
        
        // Create a simple pattern (like a "1")
        for (let i = 0; i < 28; i++) {
            for (let j = 0; j < 28; j++) {
                const idx = i * 28 + j;
                if (j >= 12 && j <= 15) { // Vertical line for "1"
                    inputData[idx] = Math.random() * 0.5 + 0.5; // Some noise
                } else {
                    inputData[idx] = Math.random() * 0.1; // Background noise
                }
            }
        }
        
        const input = new ort.Tensor('float32', inputData, [1, 1, 28, 28]);
        
        log('🔥 Running WebGPU inference...');
        startTime = performance.now();
        
        // Prepare feeds
        const feeds = {};
        feeds[session.inputNames[0]] = input;
        
        // Run inference
        const results = await session.run(feeds);
        const output = results[session.outputNames[0]];
        
        endTime = performance.now();
        const inferenceTime = Math.round(endTime - startTime);
        
        // Step 4: Process Results
        log(`⚡ Inference completed in ${inferenceTime}ms`);
        
        // Find prediction (argmax)
        let maxIdx = 0;
        let maxValue = output.data[0];
        for (let i = 1; i < output.data.length; i++) {
            if (output.data[i] > maxValue) {
                maxValue = output.data[i];
                maxIdx = i;
            }
        }
        
        const confidence = (maxValue * 100).toFixed(1);
        
        log(`🎯 Predicted digit: ${maxIdx} (confidence: ${confidence}%)`);
        log(`📈 Raw predictions: [${Array.from(output.data).map(x => x.toFixed(3)).join(', ')}]`);
        
        // Update metrics display
        updateMetric('inference-time', inferenceTime);
        updateMetric('prediction', `${maxIdx} (${confidence}%)`);
        metricsEl.style.display = 'grid';
        
        updateStatus('✅ WebGPU inference completed successfully!', 'success');
        
        // Step 5: Performance Analysis
        log('\n📊 Performance Summary:');
        log(`   • Model Load Time: ${loadTime}ms`);
        log(`   • Inference Time: ${inferenceTime}ms`);
        log(`   • Execution Provider: ${session.executionProviders[0]}`);
        log(`   • Total Time: ${loadTime + inferenceTime}ms`);
        
        log('\n🎉 Demo completed successfully!');
        log('💡 This demonstrates running AI models directly in your browser');
        log('🔒 All processing happened locally - no data left your device');
        
    } catch (error) {
        updateStatus(`❌ Error: ${error.message}`, 'error');
        log(`❌ Error occurred: ${error.message}`);
        log(`📝 Full error: ${error.stack || error}`);
        
        log('\n🔧 Troubleshooting suggestions:');
        log('   • Ensure you\'re using Chrome/Edge 113+ with WebGPU enabled');
        log('   • Check chrome://gpu for WebGPU status');
        log('   • Try refreshing the page');
        log('   • Check browser console for additional details');
        
        console.error('WebGPU Demo Error:', error);
    }
})();

// CPU Fallback Implementation
async function runWithCPU() {
    try {
        log('🔄 Initializing CPU fallback mode...');
        updateStatus('🔄 Running with CPU execution (WebGPU unavailable)', 'warning');
        
        const startTime = performance.now();
        
        // Use WASM execution provider
        const modelUrl = 'https://huggingface.co/onnx/models/resolve/main/vision/classification/mnist-12/mnist-12.onnx';
        const session = await ort.InferenceSession.create(modelUrl, {
            executionProviders: ['wasm']
        });
        
        const loadTime = Math.round(performance.now() - startTime);
        log(`✅ Model loaded with CPU in ${loadTime}ms`);
        
        // Run same inference logic
        const inputData = new Float32Array(1 * 1 * 28 * 28).fill(0.1);
        const input = new ort.Tensor('float32', inputData, [1, 1, 28, 28]);
        
        const feeds = {};
        feeds[session.inputNames[0]] = input;
        
        const inferenceStart = performance.now();
        const results = await session.run(feeds);
        const inferenceTime = Math.round(performance.now() - inferenceStart);
        
        const output = results[session.outputNames[0]];
        let maxIdx = 0;
        for (let i = 1; i < output.data.length; i++) {
            if (output.data[i] > output.data[maxIdx]) maxIdx = i;
        }
        
        updateMetric('load-time', loadTime);
        updateMetric('inference-time', inferenceTime);
        updateMetric('prediction', maxIdx);
        metricsEl.style.display = 'grid';
        
        updateStatus('✅ CPU inference completed (WebGPU would be faster)', 'success');
        log(`🎯 CPU prediction: ${maxIdx}`);
        log('💡 For better performance, use a WebGPU-compatible browser');
        
    } catch (error) {
        updateStatus(`❌ CPU fallback failed: ${error.message}`, 'error');
        log(`❌ CPU execution failed: ${error.message}`);
    }
}