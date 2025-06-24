import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class LLMInferenceGemini:
    def __init__(self, model_name='gemini-1.5-flash'):
        self.gemini_model = model_name
        self.gemini_api_key = os.getenv("API_GEMINI")
        genai.configure(api_key=self.gemini_api_key)
        self.client = genai.GenerativeModel(self.gemini_model)

    def load_prompt(self, prompt_dict, verbose=False):
        if verbose:
            print(f"Instruction Length: {len(prompt_dict['instruction'])}")
        self.system_message = prompt_dict['instruction']
        self.user_message_content = prompt_dict['output_format']

    def infer(self, max_tokens_response=None):
        try:
            prompt = f"{self.system_message}\n\n{self.user_message_content}"
            
            generation_config = {}
            if max_tokens_response:
                generation_config['max_output_tokens'] = max_tokens_response
            
            response = self.client.generate_content(
                prompt,
                generation_config=generation_config if generation_config else None
            )
            return response.text
        except Exception as e:
            print(f"Error during inference: {e}")
            return None