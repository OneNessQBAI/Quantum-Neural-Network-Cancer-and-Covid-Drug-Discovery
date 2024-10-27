from flask import Flask, request, jsonify, render_template, send_from_directory
from main_workflow import process_user_input
from Qwen import Qwen
from Qwen2Math import Qwen2Math
from synthetic_data_layers.ToCoder import ToCoder
from Starcoder import Starcoder
from quantum_algorithms.quantum_optimization import QuantumOptimization
from synthetic_data_layers.data_layer_qwen_qwen2_math import DataLayerQwenQwen2Math
from synthetic_data_layers.data_layer_qwen2_math_tocoder import DataLayerQwen2MathToCoder
from synthetic_data_layers.data_layer_tocoder_starcoder import DataLayerToCoderStarcoder
from system_prompts import QWEN_PROMPT, QWEN2_MATH_PROMPT, TOCODER_PROMPT, STARCODER_PROMPT
import openai
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.ERROR)  # Set logging to ERROR level for production

# Initialize models and data layers
qwen5b = None
qwen2_math = None
qwen2_5_coder = None
starcoder = None

data_layer_qwen_qwen2_math = DataLayerQwenQwen2Math()
data_layer_qwen2_math_tocoder = DataLayerQwen2MathToCoder()
data_layer_tocoder_starcoder = DataLayerToCoderStarcoder()

quantum_optimizer = QuantumOptimization()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect_api', methods=['POST'])
def connect_api():
    global qwen5b, qwen2_math, qwen2_5_coder, starcoder
    data = request.json
    api_key = data['api_key']
    
    try:
        openai.api_key = api_key
        # Test the API key
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hello, World!"}],
            max_tokens=5
        )
        
        # Initialize models with the API key and system prompts
        try:
            qwen5b = Qwen(system_prompt=QWEN_PROMPT, api_key=api_key)
            qwen2_math = Qwen2Math(system_prompt=QWEN2_MATH_PROMPT, api_key=api_key)
            qwen2_5_coder = ToCoder(system_prompt=TOCODER_PROMPT, api_key=api_key)
            starcoder = Starcoder(system_prompt=STARCODER_PROMPT, api_key=api_key)
        except Exception as e:
            app.logger.error(f"Error initializing models: {str(e)}")
            return jsonify({'success': False, 'error': 'Failed to initialize models'}), 500
        
        return jsonify({'success': True})
    except Exception as e:
        app.logger.error(f"Error connecting API: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/qnn_process', methods=['POST'])
def qnn_process():
    data = request.json
    user_input = data['message']
    api_key = data['api_key']

    if not api_key or not qwen5b:
        return jsonify({'error': 'API key not set or models not initialized'}), 401

    try:
        response = process_user_input(
            user_input, qwen5b, qwen2_math, qwen2_5_coder,
            starcoder,
            data_layer_qwen_qwen2_math,
            data_layer_qwen2_math_tocoder,
            data_layer_tocoder_starcoder,
            quantum_optimizer
        )
        return jsonify({'response': response})
    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500

@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route('/videos/<path:filename>')
def serve_video(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)), debug=False)  # Set debug to False for production