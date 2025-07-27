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

    ORCHESTRATOR_PROMPT = """You are an orchestrator agent. You will recieve responses from various experts relating to a query: {query}.
    Please Synthesise a final coherent, actionable response to the query based on the responses from each agent that has a non-null response.
    the response from the BudgetExpert is: {budget}, the response from the LegalExpert is: {legal}, 
    and the response from the MarketingExpert is: {marketing}. 
    be sure to make reference to whether the query is feasible from a financial and budgetary standpoint, 
    checking the 'can_afford' and 'compliant' fields,  then, responding with the insights from each of the agents, 
    before going on to explain some actionable reccomendations based on those findings and your own business accumen.
    Please provide your final response in structured JSON format according to the following schema:
    {{  'final_decision': bool, 
        'insights': {{'budget': '...', 'legal': '...', 'marketing': '...'}}, 
        'recommendations': [str] }}
    """