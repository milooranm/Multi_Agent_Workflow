# Lauchyfi Task

## Prep
so I had some ideas about the problem after reading it, but I wanted to broaden my horizons on the topic. there's a lot of things I'm sure I could have read on the topic, but to save on time, I prompted Gemini DeepResearch and told it to go research the topic with respect to the posting and get back to me. I run the risk of getting something of a generic answer by offloading this research to an AI, but I believe that in this case it is worth the tradeoff, and will save a good bit of time and effort on my part.
Notes from said deepresearch. 
- sharing via full COT or final result
- llm managed dynamic control flow? rather than fixed.
- fault tolerance super important (can happen later?)
- architecture design - use hierarchical and dynamic control flows
- sufficient prompt engineering for orchestrator essential

## Thoughts as I go/workflow
Moving forward, I have set up the environment and the requirements files, set up my OpenAI API key and the small bit of billing I'll need to handle, and am trying to get the LLM instance working. I've chosen 3.5 turbo as it's in theory the cheapest.(I didn't need to worry about the cost I'm using nowhere near enough tokens)
having got those working the next step I'm going to do is create hardcoded files for each agent so that I can build the Orchestrator and get it working, that I can update later to return JSON responses based on LLM responses.
Got the operator working and handling the inputs for each based on keywords being accounted for. Will adjust keywords to handle all the sample requests. (looking at the sample prompts, I need this part to be LLM powered)
Added LLM calls to the agents, decided to go extra modular rather than writing the code to make API calls several times I would include that somewhere else. I did the same thing with the prompts, so that they can all be tailored and edited from the same place without needing to alter the agent files themselves.
I should add error handling for the json outputs for each.
Next step is deciding how I want the Orchestrator to utilise the json responses and synthesise a response based on it's own response
After getting that working I wanted a real quick fastapi implementation and decided thst answering a randow query from the list each run would allow for minimal html and allow me to test the outputs based on different inputs.

### next steps and conclusions

the keyword decomposition from the orchestrator is definitely insufficient but easily rectified

the formatting of the output via fastapi needs a polish even with pretty print.

the agents could do with being put into their own files for neatness and organisation

the fastapi endpoint should be edited to take in any kind of query.


there could be more error handling/validation on the JSON's, but I can't justify it at this point, they aren't throwing up any errors and the final output reads them as if they were natural language anyway. I think the value in making sure internal agents output jsons is to make sure they refer to everything. and I guess you can add lots of specific considerations to the json, and by extension the prompt

THE big issue stopping the agent from being actually useful is that it isn't relying on context. it doesn't have any functionality on how to go through the companies internal information and look for things to to base it's answers on. Ideally you want the model basing these decisions on reports and deep knowledge of the companies systems. So maybe this would go well if the individual agents called a RAG based on the companies data (securely), or not quite as good, the LLM calls could involve searching the web and the prompts could include the company that one wants to search for as well. Critic expert agent has most value when the whole process returns a lot more detail.