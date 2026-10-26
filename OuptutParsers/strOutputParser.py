from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2
)
parser = StrOutputParser()
template1 = PromptTemplate.from_template(
    "generate a documenation on {topic}"
)
template2 = PromptTemplate.from_template(
    "generate a 5 line summary on /n {text}"
)
chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'black hole'})
print(type(result))
