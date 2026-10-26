from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3.8-2.4T-A95B',
    task='text-generation'
)
model = ChatHuggingFace(llm = llm)
template = ChatPromptTemplate([
    ('system', 'you are a {domain} expert'),
    ('human', 'explain me about {topic}')
])
prompt = template.invoke({
    'domain':'ai',
    'topic':'agentic ai'
})
result = model.invoke(prompt)
print(result.content)
print(prompt)