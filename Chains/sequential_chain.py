from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")
template = PromptTemplate.from_template(
    "generate a report on {topic}"
)
template2 = PromptTemplate.from_template(
    "generate a two point summary on \n {text}"
)
parser = StrOutputParser()
chain = template | model | parser | template2 | model | parser
result = chain.invoke({'topic':'mindset of succesful people'})
print(result)
chain.get_graph().print_ascii()