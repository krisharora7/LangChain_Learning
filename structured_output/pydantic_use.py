from langchain_groq import ChatGroq
from typing import Optional,Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()
class review(BaseModel):
    key_themes: list[str] = Field(description="extract main keys from summary")
    summary: str = Field(description="short summary of review")
    sentiment: Literal["positive","negative"] = Field(description="tell about sentiment of user") 
    pros: Optional[list[str]] = Field(description=" write the pros told by user")
    cons: Optional[list[str]] = Field(description=" write the cons told by user")
    age: Optional[int] = Field(ge=1, le=100, default=None)
    day: str = "monday" # default


model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2
)
structured_model = model.with_structured_output(review)
result = structured_model.invoke("phone's camera is too bad that it does not click clear photos in broad daylight. review by krish who is 15 years old")
print(result.sentiment)
print(result)