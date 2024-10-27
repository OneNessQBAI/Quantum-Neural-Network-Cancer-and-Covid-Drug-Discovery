import sys
import logging
from main_workflow import process_coding_task
from synthetic_data_layers.ToCoder import ToCoder
from Starcoder import Starcoder
from synthetic_data_layers.data_layer_qwen2_math_tocoder import DataLayerQwen2MathToCoder
from synthetic_data_layers.data_layer_tocoder_starcoder import DataLayerToCoderStarcoder
from quantum_algorithms.quantum_optimization import QuantumOptimization
from dotenv import load_dotenv
import os

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

def main():
    try:
        # Initialize components
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            logging.error("OPENAI_API_KEY not found in environment variables.")
            return

        logging.info("Initializing components...")
        qwen2_5_coder = ToCoder(system_prompt="You are an AI code generator. Your task is to generate Python code based on the user's input. Always provide complete, executable Python code without any additional explanations.", api_key=api_key)
        starcoder = Starcoder(system_prompt="You are an AI code optimizer. Your task is to optimize the given Python code for better performance and readability.", api_key=api_key)
        data_layer_qwen2_math_tocoder = DataLayerQwen2MathToCoder()
        data_layer_tocoder_starcoder = DataLayerToCoderStarcoder()
        quantum_optimizer = QuantumOptimization()

        # Test cases
        test_cases = [
            "Write a Python function to calculate the factorial of a number",
            "run this directly no optimization print('Hello world')"
        ]

        for i, user_input in enumerate(test_cases, 1):
            logging.info(f"Processing test case {i}: {user_input}")
            try:
                result = process_coding_task(user_input, qwen2_5_coder, starcoder,
                                             data_layer_qwen2_math_tocoder,
                                             data_layer_tocoder_starcoder,
                                             quantum_optimizer)
                logging.info(f"Result of test case {i}:")
                print(result)
            except Exception as e:
                logging.error(f"Error processing test case {i}: {str(e)}")
                logging.error(f"Traceback: {sys.exc_info()}")
            print("-" * 50)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        logging.error(f"Traceback: {sys.exc_info()}")

if __name__ == "__main__":
    main()