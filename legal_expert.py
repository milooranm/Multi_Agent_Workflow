class LegalExpert:
    def process_query(self, query: str) -> dict:
        print(f"LegalExpert received: {query}")
        return {
            "compliant": False,
            "issues": ["Data residency Law in Germany"], 
            "recommendation": "Mock reccomendation."
            }