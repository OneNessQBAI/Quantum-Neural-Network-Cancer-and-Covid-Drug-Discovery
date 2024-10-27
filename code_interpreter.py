from e2b_code_interpreter import CodeInterpreter
import re

def code_interpret(assistant_response):
    """
    Extracts code from the assistant's response and executes it using the E2B Code Interpreter.
    Returns the execution output as a string.
    """
    code = extract_code_from_response(assistant_response)
    if not code:
        return "No executable code found in the assistant's response."

    output = ""

    with CodeInterpreter() as sandbox:
        # Execute the extracted code in the sandbox
        execution = sandbox.notebook.exec_cell(code)

        # Handle execution errors
        if execution.error:
            output += f"There was an error during execution: {execution.error.name}: {execution.error.value}.\n{execution.error.traceback}\n"
            return output

        # Handle execution results
        if execution.results:
            output += "Execution Results:\n"
            for i, result in enumerate(execution.results):
                output += f"Result {i + 1}:\n"
                if result.is_main_result:
                    output += f"[Main result]: {result.text}\n"
                else:
                    output += f"[Display data]: {result.text}\n"

        # Handle execution logs
        if execution.logs.stdout or execution.logs.stderr:
            output += "Execution Logs:\n"
            if execution.logs.stdout:
                output += "Stdout:\n"
                output += "\n".join(execution.logs.stdout) + "\n"
            if execution.logs.stderr:
                output += "Stderr:\n"
                output += "\n".join(execution.logs.stderr) + "\n"

        if not output:
            output = "Execution completed with no output.\n"

    return output

def extract_code_from_response(response):
    """
    Extracts code from the assistant's response by finding code within markdown code blocks.
    """
    # Find code within markdown code blocks
    code_blocks = re.findall(r'```(?:python)?\s*([\s\S]*?)```', response)
    if not code_blocks:
        return ''
    # Join all code blocks into one string
    code = '\n'.join(code_blocks)
    return code.strip()

# Additional functions or placeholders can be added below if needed