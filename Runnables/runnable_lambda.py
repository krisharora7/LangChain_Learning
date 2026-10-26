from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableSequence, RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
def word_count(text):
    return len(text.split()) # .split() splits the string into words by spaces between them and add the words in a list
model = ChatGroq(model="openai/gpt-oss-20b")
parser = StrOutputParser()
prompt = PromptTemplate.from_template(
    "generate a short joke on {topic}"
)
joke_gen_chain = RunnableSequence(prompt,model,parser)
parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})
chain = RunnableSequence(joke_gen_chain, parallel_chain)
result = chain.invoke({'topic':"Distracted ambitious student"})
print(result)