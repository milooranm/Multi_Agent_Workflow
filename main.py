from orchestrator_agent import OrchestratorAgent

def main():
    try:
        orchestrator = OrchestratorAgent()
        
        query = "Can we launch a new product in Q3 with a budget of $50,000?"
        response = orchestrator.process_query(query)
        
        print("Orchestrator Response:")
        print(response)
        
    except Exception as e:
        print(f"Error in orchestrator processing: {e}")

if __name__ == "__main__":
    main()