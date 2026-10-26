from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")
prompt1 = PromptTemplate.from_template(
    "generate me a tweet on {topic}"
)
prompt2 = PromptTemplate.from_template(
    "generate me a linkedIn post on {topic}"
)
parser = StrOutputParser()
chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedIn': RunnableSequence(prompt2,model,parser)
})

result = chain.invoke({'topic':'super human'})
print(result)