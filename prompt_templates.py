class PromptTemplates:
    BUDGET_PROMPT = """You are a budget expert. Analyze the budget feasibility based on the provided query: {query}. 
    Please provide your analysis in structured JSON format according to the following schema: 
    {{'can_afford': bool, 'estimated_cost': float, 'budget_remaining': float, 'rationale': str}}"""

    LEGAL_PROMPT = """You are a legal expert. Analyze the legal implications and compliance requirements for the following query: {query}.
    Please provide your analysis in structured JSON format according to the following schema:
    {{'compliant': bool, 'issues': list[str], 'recommendation': str}}"""

    MARKETING_PROMPT = """You are a marketing expert. Analyze the marketing strategy and potential for the following query: {query}.
    Please provide your analysis in structured JSON format according to the following schema:
    {{'launch_score': int, 'channels': str, 'tagline': str}}"""