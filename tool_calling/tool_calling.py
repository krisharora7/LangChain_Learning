from langchain.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """this tool multiplyies two numbers"""
    return a*b

llm = ChatGroq(model='openai/gpt-oss-20b')
llm_with_tool = llm.bind_tools([multiply])
result = llm_with_tool.invoke("whats 8 multipliyed by 243")
print(f"Result - > \n {result} \n")
print(result.tool_calls[0])