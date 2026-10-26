from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(model='openai/gpt-oss-20b')
tool = DuckDuckGoSearchRun()

agent = create_agent(
    model=llm,
    tools=[tool],
    system_prompt='you are a helpful assistant , answer the user query and use available tools if required'
)

result = agent.invoke({
    'messages':[
        {
            'role':'user',
            'content':'what is the population of capital of france?'
        }
    ]
})
print(result)
print(result['messages'][-1].content)