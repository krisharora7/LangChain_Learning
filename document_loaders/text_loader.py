from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
loader = TextLoader('sample.txt')
docs = loader.load()
model = ChatGroq(model="openai/gpt-oss-20b")
prompt = PromptTemplate.from_template(
    "how is the character of writer of this text in few words -> {text}"
)
chain = prompt | model | StrOutputParser()
# print(docs)
# print(docs[0])
# print(docs[0].metadata)
print(chain.invoke({'text':docs[0].page_content}))