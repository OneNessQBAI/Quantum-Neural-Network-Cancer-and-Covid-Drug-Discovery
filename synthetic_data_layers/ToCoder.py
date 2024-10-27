import requests
import json
import os
import re
from dotenv import load_dotenv

class ToCoder:
    def __init__(self, system_prompt, api_key):
        self.system_prompt = system_prompt + "\nProvide ONLY Python code enclosed within triple backticks. Do not include ANY explanations, comments, or markdown formatting outside the code block."
        self.openrouter_api_key = "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"
        self.site_url = "https://your-site-url.com"  # Replace with your actual site URL
        self.app_name = "QNN-CodeGenerator"  # Replace with your actual app name

        # Load E2B API key from .env file
        load_dotenv()
        self.e2b_api_key = os.getenv('E2B_API_KEY')
        if not self.e2b_api_key:
            raise ValueError("E2B_API_KEY not found in .env file")

    def generate_code(self, prompt):
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.openrouter_api_key}",
                "HTTP-Referer": self.site_url,
                "X-Title": self.app_name,
            },
            json={
                "model": "o1-mini",
                "messages": [
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": f"Generate ONLY Python code for the following task, enclosed within triple backticks. NO explanations or comments: {prompt}"}
                ]
            }
        )

        if response.status_code == 200:
            generated_text = response.json()['choices'][0]['message']['content']
            code = self.extract_code(generated_text)
            if not code:
                return "# No valid Python code found in the response."
            return code
        else:
            return f"# Error: Unable to generate code. Status code: {response.status_code}"

    def extract_code(self, text):
        # Extract code within triple backticks
        match = re.search(r'```(?:python)?\s*([\s\S]*?)\s*```', text)
        if match:
            code = match.group(1)
            # Remove any leading/trailing whitespace
            code = code.strip()
            return code
        return None