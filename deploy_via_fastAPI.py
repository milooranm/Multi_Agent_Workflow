from fastapi import FastAPI, Response
from fastapi.responses import StreamingResponse
from fastapi.responses import HTMLResponse
import uvicorn
import json
import random

from orchestrator_agent import OrchestratorAgent

app = FastAPI(
    title = 'Launchyfi Agents',
    description = 'Launchyfi Agents API for orchestrating tasks'
)

def load_prompts():
    with open('promptsInterview.json', 'r') as file:
        return json.load(file)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <body>
            <h1>Launchyfi Agents API</h1>
            <p>Visit <a href="/docs">/docs</a> for the API documentation</p>
            <p>Visit <a href="/analyse">/sample</a> for response to a random sample query</p>
        </body>
    </html>
    """

@app.get("/analyse")
async def analyse_random():
    try:
        # Load prompts and select random one
        prompts = load_prompts()
        random_prompt = random.choice(prompts)
        
        # Process with orchestrator
        orchestrator = OrchestratorAgent()
        response = orchestrator.process_query(random_prompt["query"])
        
        return {
            "query_id": random_prompt["id"],
            "query": random_prompt["query"],
            "analysis": response
        }
        
        
    except Exception as e:
        return {"error": str(e)}

