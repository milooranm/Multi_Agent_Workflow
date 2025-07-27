from budget_expert import BudgetExpert
from legal_expert import LegalExpert
from marketing_expert import MarketingExpert

class OrchestratorAgent:
    def __init__(self):
        self.budget_expert = BudgetExpert()
        self.legal_expert = LegalExpert()
        self.marketing_expert = MarketingExpert()

    def process_query(self, query: str) -> dict:
        print(f"OrchestratorAgent received query: {query}")
        
        budget_response = self.budget_expert.process_query(query)
        legal_response = self.legal_expert.process_query(query)
        marketing_response = self.marketing_expert.process_query(query)

        return {
            "budget": budget_response,
            "legal": legal_response,
            "marketing": marketing_response
        }