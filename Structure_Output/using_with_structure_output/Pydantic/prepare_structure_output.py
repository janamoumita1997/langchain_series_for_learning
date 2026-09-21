from langchain_openai import OpenAI
from pydantic import BaseModel, Field
from typing import TypedDict, Optional, Literal
from dotenv import load_dotenv

load_dotenv()

model = OpenAI()

class review(BaseModel):
    key_theme:list[str] = Field(description='')
    summary:str = Field(description='')
    sentiment:Literal['pos','neg','nut'] = Field(description='')
    pros:Optional[list[str]] = Field(default=None, description='')

structure_model = model.with_structured_output(review)

result = structure_model.invoke("<prompt>")

print(result.key_theme)