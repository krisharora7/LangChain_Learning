from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableBranch
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model = ChatGroq(model="openai/gpt-oss-20b")
parser = StrOutputParser()
prompt1 = PromptTemplate.from_template(
    "generate a short report on {topic}"
)
prompt2 = PromptTemplate.from_template(
    "generate a summary within 10 words for report \n {report} "
)
report_gen_chain = RunnableSequence(prompt1,model,parser)
conditional_chain = RunnableBranch(
    (lambda x: len(x.split())>10, RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)
chain = report_gen_chain | conditional_chain
result = chain.invoke({'topic':'polymaths'})
print(result)