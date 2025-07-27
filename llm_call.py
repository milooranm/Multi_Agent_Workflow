import os
from dotenv import load_dotenv
from openai import OpenAI

class LLMHandler:
    """Class to handle LLM API requests."""
    
    def __init__(self, model="gpt-3.5-turbo"):
        """Initialize the LLM handler.
        
        Args:
            model (str): The model to use for requests. Defaults to "gpt-3.5-turbo".
        """
        self.model = model
        try:
            load_dotenv()
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        except Exception as e:
            print(f"Error initializing OpenAI client: {e}")
            raise

    def make_request(self, input_text: str) -> str:
        """Make a request to the OpenAI API.
        
        Args:
            input_text (str): The input text to send to the LLM.
            
        Returns:
            str: The response from the LLM.
            
        Raises:
            Exception: If there's an error connecting to the LLM.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": input_text}]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error connecting to LLM: {e}")
            raise
