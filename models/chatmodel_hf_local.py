from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFacePipeline(
    repo_id='Qwen/Qwen3.8-2.4T-A95B',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("give me a roadmap for ai engineer")
print(result.content)