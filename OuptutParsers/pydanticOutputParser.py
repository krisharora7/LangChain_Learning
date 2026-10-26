from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field, BaseModel
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2
)
class schema(BaseModel):
    name: str = Field(description='name of person')
    age: int = Field(ge=18, description='age of the person')
    place: str = Field(description='city of the person')

parser = PydanticOutputParser(pydantic_object=schema)
template = PromptTemplate.from_template(
    "generate name , age and place of a fictional {place} person \n {format_instruction}",
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain = template | model | parser
result = chain.invoke({'place':"Sonipat"})
print(result)
print(result.age)