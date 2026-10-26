from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2
)
template = PromptTemplate.from_template(
    "give me 5 key words on {topic}"
)
chain = template | model | StrOutputParser()
result = chain.invoke({'topic': 'cost of success'})
print(result)
chain.get_graph().print_ascii()