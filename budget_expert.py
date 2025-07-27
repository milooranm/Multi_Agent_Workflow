class BudgetExpert:
    def process_query(self, query: str) -> dict:
        print(f"BudgetExpert received: {query}")
        return {
            "can_afford" : True,
            "estimated_cost": 10000,
            "budget_remaining": 50000,
            "rationale": "Mock budget analysis based on query."
        }