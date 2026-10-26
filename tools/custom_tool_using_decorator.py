"""def add():
    ''' this function is used for addition'''

print(add.__doc__)"""

from langchain_community.tools import tool
@tool
def multiply(a :int, b :int ) -> int:
    """it multiplies two integers"""
    return a*b

# multiply is now a runnable
result = multiply.invoke({'a':5, 'b':90})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())