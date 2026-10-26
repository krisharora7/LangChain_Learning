from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(model='openai/gpt-oss-20b')

url = ['https://www.amazon.in/amazon-basics-Cancellation-Coumputer-Headphones/dp/B0DG2RP3MM?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=AJ6SIZC8YQDZX&th=1','https://www.amazon.in/All-New-release-speaker-Detection-Temperature/dp/B09B8M1M51?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=AJ6SIZC8YQDZX&th=1']

loader = WebBaseLoader(url)

docs = loader.load()

prompt = PromptTemplate.from_template(
    "Answer the following question -> {question} \n from text -> {text}"
)
chain = prompt | model | StrOutputParser()
print(chain.invoke({'question':'what product are we talking about? and what is the price of product','text':docs[1].page_content}))