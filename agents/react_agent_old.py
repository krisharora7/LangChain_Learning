from langchain_groq import ChatGroq
from langchain_classic.agents import create_react_agent, AgentExecutor
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langsmith import Client
load_dotenv()

llm = ChatGroq(model='openai/gpt-oss-20b')

tool = DuckDuckGoSearchRun()
# testing -> print(tool.invoke('top news in india today'))

client = Client()
prompt = client.pull_prompt("hwchase17/react", dangerously_pull_public_prompt=True)

agent=create_react_agent(
    llm=llm,
    tools=[tool],
    prompt=prompt
)
agent_executer = AgentExecutor(
    agent=agent,
    tools=[tool],
    verbose=True
)

response = agent_executer.invoke({'input':'what is the population of capital of france?'})
print(response)

"""
    OLD IMPLEMENTATION WHICH CRASHES NOW WITH MODERN LANGCHAIN
"""