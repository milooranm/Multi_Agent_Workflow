Lauchyfi Task
so I had some ideas about the problem after reading it, but I wanted to broaden my horizons on the topic. there's a lot of things I'm sure I could have read on the topic, but to save on time, I prompted Gemini DeepResearch and told it to go research the topic with respect to the posting and get back to me. I run the risk of getting something of a generic answer by offloading this research to an AI, but I believe that in this case it is worth the tradeoff, and will save a good bit of time and effort on my part.
Notes from said deepresearch. 
- sharing via full COT or final result
- llm managed dynamic control flow? rather than fixed.
- fault tolerance super important (can happen later?)
- perception, memory, planning, tool & reflection modules typical
- architecture design - use hierarchical and dynamic control flows
- how does orchestrator perform query decomposition
- sufficient prompt engineering for orchestrator essential
- 

Moving forward, I have set up the environment and the requirements files, set up my OpenAI API key and the small bit of billing I'll need to handle, and am trying to get the LLM instance working. I've chosen 3.5 turbo as it's in theory the cheapest.
having got those working the next step I'm going to do is create hardcoded files for each agent so that I can build the Orchestrator and get it working, that I can update later to return JSON responses based on LLM responses.
Got the operator working and handling the inputs for each based on keywords being accounted for. Will adjust keywords to handle all the sample requests.
Added LLM calls to the agents, decided to go extra modular rather than writing the code to make API calls several times I would include that somewhere else. I did the same thing with the prompts, so that they can all be tailored and edited from the same place without needing to alter the agent files themselves.
I should add error handling for the json outputs for each.
Next step is deciding how I want the Orchestrator to utilise the json responses and synthesise a response based on it's own response