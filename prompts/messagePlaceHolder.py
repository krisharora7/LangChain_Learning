from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3.8-2.4T-A95B',
    task='text-generation'
)
model = ChatHuggingFace(llm = llm)
template = ChatPromptTemplate([
    ('system', 'you are a {domain} expert'),
    MessagesPlaceholder("history"),
    ('human', 'explain me about {topic}')
])
chat_history=[]



while True:
    user_query = input("enter query: ")
    if(user_query=='exit'):
        break
    
    prompt = template.invoke({
    'domain':'ai',
    'history':chat_history,
    'topic':'explain: ' + user_query
})
    result = model.invoke(prompt)
    print(result.content)
    chat_history.append(HumanMessage(user_query))
    chat_history.append(AIMessage(result.content))
    
print(chat_history)