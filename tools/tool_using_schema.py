from langchain_community.tools import StructuredTool
from pydantic import BaseModel, Field
class schema(BaseModel):
    a: int = Field(description="first number to multiply")
    b: int = Field(description="second number to multiply")

def multiply_func(a :int, b :int) -> int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="multiply two numbers",
    args_schema=schema
)

result = multiply_tool.invoke({'a':62, 'b':10})
print(result)
print(multiply_tool.description)
print(multiply_tool.args_schema.model_json_schema())