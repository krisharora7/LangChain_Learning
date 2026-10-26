from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()

class Schema(BaseModel):
    sentiment :Literal['Positive', 'Negative'] = Field(description="tell about the sentiment of user's feedback")
    
parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Schema)

model = ChatGroq(model="openai/gpt-oss-20b")
prompt1 = PromptTemplate.from_template(
    "Give me the sentiment of the feedback ->{feedback} \n {format_instruction}",
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)
prompt2 = PromptTemplate.from_template(
    "write an appropriate reply for this positive feedback -> {feedback}"
)
prompt3 = PromptTemplate.from_template(
    "write an appropriate reply for this negative feedback directly to the user-> {feedback}"
)

classify_chain = prompt1 | model | parser2
branch_chain = RunnableBranch(
    # (condition,chain)
    (lambda x: x.sentiment.lower()=='positive', prompt2 | model | parser1),
    (lambda x: x.sentiment.lower()=='negative', prompt3 | model | parser1),
    # default chain, not have any default chain so i used runnable lamda to convert my func into a runnable
    RunnableLambda(lambda x: "could not find any sentiment")
)
chain = classify_chain | branch_chain
result = chain.invoke({'feedback':'i really dislike the battery life of this smartphone, it not even last my whole day'})
print(result)
chain.get_graph().print_ascii()
# print(classify_chain.invoke({'feedback': "what a camera of this phone"}))