from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")
parser = StrOutputParser()
prompt1 = PromptTemplate.from_template(
    "generate a name of a state from {country}"
)
prompt2 = PromptTemplate.from_template(
    "tell me the captital of {state}"
)
chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)
result = chain.invoke({'country':'India'})
print(result)