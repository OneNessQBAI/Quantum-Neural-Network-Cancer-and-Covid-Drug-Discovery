
from Qwen import Qwen
from Qwen2Math import Qwen2Math
from Starcoder import Starcoder
from system_prompts import QWEN_PROMPT, QWEN2_MATH_PROMPT, TOCODER_PROMPT, STARCODER_PROMPT
from synthetic_data_layers.data_layer_qwen_qwen2_math import DataLayerQwenQwen2Math
from synthetic_data_layers.data_layer_qwen2_math_tocoder import DataLayerQwen2MathToCoder
from synthetic_data_layers.data_layer_tocoder_starcoder import DataLayerToCoderStarcoder
from quantum_algorithms.quantum_optimization import QuantumOptimization
from code_interpreter import code_interpret

def process_user_input(user_input, qwen5b, qwen2_math, qwen2_5_coder,
                       starcoder,
                       data_layer_qwen_qwen2_math,
                       data_layer_qwen2_math_tocoder,
                       data_layer_tocoder_starcoder,
                       quantum_optimizer):
    qwen5b_output = qwen5b.process(user_input)

    if requires_coding(user_input):
        return process_coding_task(user_input, qwen2_5_coder, starcoder,
                                   data_layer_qwen2_math_tocoder,
                                   data_layer_tocoder_starcoder,
                                   quantum_optimizer)
    elif requires_math(user_input):
        return process_math_task(user_input, qwen2_math,
                                 data_layer_qwen_qwen2_math,
                                 quantum_optimizer)
    else:
        return qwen5b_output

def process_coding_task(user_input, qwen2_5_coder, starcoder,
                        data_layer_qwen2_math_tocoder,
                        data_layer_tocoder_starcoder,
                        quantum_optimizer):
    # Generate initial code
    code_output = qwen2_5_coder.generate_code(user_input)
    
    # Check if optimization is required
    if "no optimization" not in user_input.lower():
        # Optimize code using Starcoder
        optimized_code = starcoder.optimize_code(code_output)
        
        # Apply quantum optimization
        final_code = quantum_optimizer.optimize(optimized_code)
    else:
        final_code = code_output

    # Execute the code using execute_code from code_interpreter.py
    execution_result = code_interpret(final_code)

    # Format the result
    formatted_result = f"""
Generated and Optimized Code:
```python
{final_code}
```

Execution Output:
{execution_result}
"""
    return formatted_result

def process_math_task(user_input, qwen2_math, data_layer_qwen_qwen2_math,
                      quantum_optimizer):
    math_input = data_layer_qwen_qwen2_math.process_data(user_input)
    math_output = qwen2_math.compute(math_input)
    quantum_math_output = quantum_optimizer.optimize(math_output)
    return quantum_math_output

def requires_coding(query):
    keywords = ['code', 'implement', 'program', 'script', 'develop', 'algorithm', 'run']
    return any(keyword in query.lower() for keyword in keywords)

def requires_math(query):
    keywords = ['calculate', 'compute', 'solve', 'equation', 'formula', 'mathematics', 'derivation']
    return any(keyword in query.lower() for keyword in keywords)
