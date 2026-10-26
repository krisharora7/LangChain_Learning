from langchain_core.tools import tool

@tool
def multiply(a :int, b :int)->int:
    '''this is multiplication tool'''
    return a*b

@tool
def addition(a :int, b :int)->int:
    '''this is addition tool'''
    return a+b

class MathToolkit:
    def get_tools(self):
        return [multiply,addition]

toolkit = MathToolkit()
tools = toolkit.get_tools()
for tool in tools:
    print(tool.description)