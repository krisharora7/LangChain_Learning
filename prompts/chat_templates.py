from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
profession = input("enter a profession: ")
topic = input("enter a topic: ")
tone = input("enter a tone: ")
llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3.8-2.4T-A95B',
    task='text-generation'
)
template = PromptTemplate.from_template(
    '''
    You are a {profession} , help me to understand {topic}.
    explain in {tone} tone'''

)
# prompt = template.invoke(
#     {
#         'profession':profession,
#         'topic':topic,
#         'tone':tone
#     }
# )

model = ChatHuggingFace(
    llm=llm,
    temperature=0.2,
    max_completion_tokens=500
)
chain = template | model
result = chain.invoke(
    {
         'profession':profession,
         'topic':topic,
         'tone':tone
    }
)
print(result.content)
