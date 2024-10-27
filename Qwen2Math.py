import openai

class Qwen2Math:
    def __init__(self, system_prompt, api_key):
        self.system_prompt = system_prompt
        openai.api_key = api_key  # Correctly set the API key

    def compute(self, math_input):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": math_input}
            ],
            max_tokens=1000,
            temperature=0.0  # Lower temperature for deterministic output
        )
        return response["choices"][0]["message"]["content"]