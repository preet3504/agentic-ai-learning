'''
Create a AI agent that can search overthe web and answer questions using the retrieved information.
'''

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_classic import hub
from dotenv import load_dotenv
from langsmith import Client

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

client = Client()

prompt = client.pull_prompt("hwchase17/react", dangerously_pull_public_prompt=True)

search = DuckDuckGoSearchRun()

agent = create_react_agent(model, tools=[search], prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=[search], verbose=True)

response = agent_executor.invoke({'input': 'Way to go goa, india tourise place?'})

print(response)