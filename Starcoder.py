import openai

class Starcoder:
    def __init__(self, system_prompt, api_key):
        self.system_prompt = system_prompt
        openai.api_key = api_key  # Correctly set the API key

    def optimize_code(self, code_input):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": code_input}
            ],
            max_tokens=1000,
            temperature=0.5
        )
        return response["choices"][0]["message"]["content"]