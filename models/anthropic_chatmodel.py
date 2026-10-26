from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
model = ChatAnthropic(model='gpt-4', temperature=0.5, max_completion_tokens=10)
result = model.invoke("hi how are you?")
print(result.content)