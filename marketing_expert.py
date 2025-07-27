class MarketingExpert:
    def process_query(self, query: str) -> dict:
        print(f"MarketingExpert received: {query}")
        return {
            "launch_score": 10, 
            "channels": "LinkedIn, Youtube", 
            "tagline": "Mock tagline."
            }