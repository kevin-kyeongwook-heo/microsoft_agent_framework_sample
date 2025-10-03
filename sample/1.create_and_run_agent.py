# https://learn.microsoft.com/en-us/agent-framework/tutorials/agents/run-agent?pivots=programming-language-python

import asyncio
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from dotenv import load_dotenv
load_dotenv()

# Create an agent with Azure OpenAI Chat Client
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent(
    instructions="You are good at telling jokes.",
    name="Joker"
)

# Run the agent with a prompt
async def main():
    result = await agent.run("Tell me a joke about a pirate.")
    print(result.text)

asyncio.run(main())