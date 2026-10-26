from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
class schema(BaseModel):
    a: int = Field(description="first number to multiply")
    b: int = Field(description="second number to multiply")

class multiply_tool(BaseTool):
    name: str = "multiply"
    description: str = "it multiplies two numbers"

    args_schema: Type[BaseModel] = schema

    def _run(self, a :int, b :int):
        return a*b

multiply_tool = multiply_tool()
result = multiply_tool.invoke({'a':28, 'b':52})
print(result)
print(multiply_tool.description)
print(multiply_tool.args_schema.model_json_schema())

