from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain.messages import HumanMessage, AIMessage, SystemMessage
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3.8-2.4T-A95B',
    task='text-generation'
)
model = ChatHuggingFace(llm = llm)
chat_history=[]
chat_history.append(SystemMessage(content="you are a helpful assistant"))
while True:
    user_query = input("enter query: ")
    if(user_query=='exit'):
        break
    chat_history.append(HumanMessage(user_query))
    result = model.invoke(chat_history)
    print(result.content)
    chat_history.append(AIMessage(result.content))
print(chat_history)