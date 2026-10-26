from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")
parser = StrOutputParser()
prompt1 = PromptTemplate.from_template(
    "generate a joke on {topic}"
)
prompt2 = PromptTemplate.from_template(
    "generate explanation for joke -> {joke}"
)
joke_gen_chain = RunnableSequence(prompt1,model,parser)
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})
chain = joke_gen_chain | parallel_chain
result = chain.invoke({'topic':'agentic ai'})
print(result)