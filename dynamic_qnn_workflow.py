```python
import threading
from queue import Queue

from Qwen import Qwen
from Qwen2Math import Qwen2Math
from DeepSeekCoder import DeepSeekCoder
from Starcoder import Starcoder

from system_prompts import QWEN_PROMPT, QWEN2_MATH_PROMPT, TOCODER_PROMPT, STARCODER_PROMPT

from synthetic_data_layers.data_layer_qwen_qwen2_math import DataLayerQwenQwen2Math
from synthetic_data_layers.data_layer_qwen2_math_tocoder import DataLayerQwen2MathToCoder
from synthetic_data_layers.data_layer_tocoder_starcoder import DataLayerToCoderStarcoder

from quantum_algorithms.quantum_optimization import QuantumOptimization

def main():
    # Initialize models
    qwen5b = Qwen(system_prompt=QWEN_PROMPT)
    qwen2_math = Qwen2Math(system_prompt=QWEN2_MATH_PROMPT)
    qwen2_5_coder = DeepSeekCoder(system_prompt=TOCODER_PROMPT)
    starcoder = Starcoder(system_prompt=STARCODER_PROMPT)
    deepseek = DeepSeekCoder(system_prompt=TOCODER_PROMPT)

    # Initialize data layers
    data_layer_qwen_qwen2_math = DataLayerQwenQwen2Math()
    data_layer_qwen2_math_tocoder = DataLayerQwen2MathToCoder()
    data_layer_tocoder_starcoder = DataLayerToCoderStarcoder()

    # Initialize quantum optimizer
    quantum_optimizer = QuantumOptimization()

    print("Welcome to the Quantum Neural Network (QNN) Interface.")
    print("Type your query below. Type 'exit' to quit.")

    while True:
        user_input = input("\nUser: ")
        if user_input.lower() == 'exit':
            print("Exiting QNN Interface.")
            break

        # Start a new thread to handle the user input
        threading.Thread(target=process_user_input, args=(
            user_input, qwen5b, qwen2_math, qwen2_5_coder,
            starcoder, deepseek,
            data_layer_qwen_qwen2_math,
            data_layer_qwen2_math_tocoder,
            data_layer_tocoder_starcoder,
            quantum_optimizer)).start()

def process_user_input(user_input, qwen5b, qwen2_math, qwen2_5_coder,
                       starcoder, deepseek,
                       data_layer_qwen_qwen2_math,
                       data_layer_qwen2_math_tocoder,
                       data_layer_tocoder_starcoder,
                       quantum_optimizer):
    # Qwen-5b processes the user input
    print("Qwen-5b is processing your request...")
    qwen5b_output = qwen5b.process(user_input)

    # Determine task type and assign to appropriate models
    if requires_coding(user_input):
        # Start parallel processing for coding tasks
        q = Queue()

        threading.Thread(target=process_coding_task, args=(
            user_input, qwen2_5_coder, starcoder, deepseek,
            data_layer_qwen2_math_tocoder,
            data_layer_tocoder_starcoder, q,
            quantum_optimizer)).start()
        threading.Thread(target=process_math_task, args=(
            user_input, qwen2_math,
            data_layer_qwen_qwen2_math, q,
            quantum_optimizer)).start()

        # Collect responses
        responses = []
        for _ in range(2):
            responses.append(q.get())

        # DeepSeek aggregates and selects the best response
        print("DeepSeek is aggregating responses...")
        deepseek_output = deepseek.select_best_response(responses)
        print(f"\nQNN Response:\n{deepseek_output}")

    elif requires_math(user_input):
        # Process mathematical query
        print("Qwen2-Math is solving the problem...")
        qwen2_math_output = qwen2_math.compute(user_input)
        # Quantum optimization
        print("Applying quantum optimizations to mathematical computations...")
        quantum_math_output = quantum_optimizer.optimize(qwen2_math_output)
        print(f"\nQwen2-Math Response:\n{quantum_math_output}")

    else:
        # General query processed by Qwen-5b
        print(f"\nQwen-5b Response:\n{qwen5b_output}")

def process_coding_task(user_input, qwen2_5_coder, starcoder, deepseek,
                        data_layer_qwen2_math_tocoder,
                        data_layer_tocoder_starcoder, q,
                        quantum_optimizer):
    # Qwen2.5-Coder processes the coding task
    print("Qwen2.5-Coder is generating code...")
    tocoder_input = data_layer_qwen2_math_tocoder.process_data(user_input)
    code_output = qwen2_5_coder.generate_code(tocoder_input)

    # Starcoder optimizes the code
    print("Starcoder is optimizing the code...")
    starcoder_input = data_layer_tocoder_starcoder.transform_data(code_output)
    optimized_code = starcoder.optimize_code(starcoder_input)

    # Quantum optimization
    print("Applying quantum optimizations...")
    quantum_optimized_code = quantum_optimizer.optimize(optimized_code)

    q.put(quantum_optimized_code)

def process_math_task(user_input, qwen2_math, data_layer_qwen_qwen2_math, q,
                      quantum_optimizer):
    # Qwen2-Math processes the mathematical task
    print("Qwen2-Math is solving the problem...")
    math_input = data_layer_qwen_qwen2_math.process_data(user_input)
    math_output = qwen2_math.compute(math_input)

    # Quantum optimization
    print("Applying quantum optimizations to mathematical computations...")
    quantum_math_output = quantum_optimizer.optimize(math_output)

    q.put(quantum_math_output)

def requires_coding(query):
    keywords = ['code', 'implement', 'program', 'script', 'develop', 'algorithm']
    return any(keyword in query.lower() for keyword in keywords)

def requires_math(query):
    keywords = ['calculate', 'compute', 'solve', 'equation', 'formula', 'mathematics', 'derivation']
    return any(keyword in query.lower() for keyword in keywords)

if __name__ == "__main__":
    main()
```