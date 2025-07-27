from budget_expert import BudgetExpert
from legal_expert import LegalExpert
from marketing_expert import MarketingExpert
from llm_call import LLMHandler
from prompt_templates import PromptTemplates

BUDGETKEYWORDS = ["budget", "cost", "affordability", "financial"]
LEGALKEYWORDS = ["legal", "compliance", "regulation", "law"]
MARKETINGKEYWORDS = ["launch", "product", "marketing", "campaign"]


class OrchestratorAgent:
    def __init__(self):
        self.budget_expert = BudgetExpert()
        self.legal_expert = LegalExpert()
        self.marketing_expert = MarketingExpert()
        self.llm = LLMHandler()

    def process_query(self, query: str) -> dict:
        print(f"OrchestratorAgent received query: {query}")

        if any(keyword in query.lower() for keyword in BUDGETKEYWORDS):
            print("\nRouting to BudgetExpert")
            budget_response = self.budget_expert.process_query(query)
        else:
            budget_response = None
            
        if any(keyword in query.lower() for keyword in LEGALKEYWORDS):
            print("\nRouting to LegalExpert")
            legal_response = self.legal_expert.process_query(query)
        else:
            legal_response = None
        
        if any(keyword in query.lower() for keyword in MARKETINGKEYWORDS):
            print("\nRouting to MarketingExpert")
            marketing_response = self.marketing_expert.process_query(query)
        else:
            marketing_response = None

        formatted_prompt = PromptTemplates.ORCHESTRATOR_PROMPT.format(query=query, 
                                                                      budget = budget_response, 
                                                                      legal=legal_response, 
                                                                      marketing=marketing_response)
        response = self.llm.make_request(formatted_prompt)

        return response