from budget_expert import BudgetExpert
from legal_expert import LegalExpert
from marketing_expert import MarketingExpert

BUDGETKEYWORDS = ["budget", "cost", "affordability", "financial"]
LEGALKEYWORDS = ["legal", "compliance", "regulation", "law"]
MARKETINGKEYWORDS = ["launch", "product", "marketing", "campaign"]


class OrchestratorAgent:
    def __init__(self):
        self.budget_expert = BudgetExpert()
        self.legal_expert = LegalExpert()
        self.marketing_expert = MarketingExpert()

    def process_query(self, query: str) -> dict:
        print(f"OrchestratorAgent received query: {query}")

        if any(keyword in query.lower() for keyword in BUDGETKEYWORDS):
            print("Routing to BudgetExpert")
            budget_response = self.budget_expert.process_query(query)
        else:
            budget_response = None
            
        if any(keyword in query.lower() for keyword in LEGALKEYWORDS):
            print("Routing to LegalExpert")
            legal_response = self.legal_expert.process_query(query)
        else:
            legal_response = None
        
        if any(keyword in query.lower() for keyword in MARKETINGKEYWORDS):
            print("Routing to MarketingExpert")
            marketing_response = self.marketing_expert.process_query(query)
        else:
            marketing_response = None

        return {
            "budget": budget_response,
            "legal": legal_response,
            "marketing": marketing_response
        }