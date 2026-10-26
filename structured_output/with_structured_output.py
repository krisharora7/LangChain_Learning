from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from typing import TypedDict, Annotated, Optional, NotRequired, Required, Literal
from dotenv import load_dotenv
load_dotenv()
class review(TypedDict):
    summary: Annotated[str,"short concise summary of review"]
    sentiment: Annotated[Literal["positive","negative"], "tell about sentiment of user"]
    pros: Annotated[Optional[list[str]], " write the pros told by user"]
    cons: Annotated[Optional[list[str]], " write the cons told by user"]


llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen3.8-2.4T-A95B',
    task='text-generation'
)
model = ChatHuggingFace(llm=llm)
structured_model = model.with_structured_output(review)
result = structured_model.invoke("phone's camera is too bad that it does not click clear photos in broad daylight. review by krish")
print(result['sentiment'])
print(result)