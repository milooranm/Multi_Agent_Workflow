from llm_call import LLMHandler
from prompt_templates import PromptTemplates

class LegalExpert:
    def __init__(self):
        self.llm = LLMHandler()


    def process_query(self, query: str) -> dict:
        print(f"LegalExpert received: {query}")
        formatted_prompt = PromptTemplates.LEGAL_PROMPT_PROMPT.format(query=query)
        response = self.llm.make_request(formatted_prompt)


        return response