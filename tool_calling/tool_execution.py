from langchain.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """this tool multiplyies two numbers"""
    return a*b

llm = ChatGroq(model='openai/gpt-oss-20b')
llm_with_tool = llm.bind_tools([multiply])
query = HumanMessage("whats 8 multipliyed by 243")
messages=[query]
result = llm_with_tool.invoke(messages)
messages.append(result)
tool_result=multiply.invoke(result.tool_calls[0])
messages.append(tool_result)
print(messages)
print('\n')
print(llm_with_tool.invoke(messages))