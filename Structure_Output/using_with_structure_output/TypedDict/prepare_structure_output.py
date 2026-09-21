from langchain_openai import OpenAI
from typing import TypedDict, Optional, Literal, Annotated
from dotenv import load_dotenv

load_dotenv()

model = OpenAI()

class review(TypedDict):
    key_theme:Annotated[list[str], '<description>']
    summary:Annotated[str, '<description>']
    sentiment:Annotated[Literal['pos','neg','nut'],'']
    pros:Annotated[Optional[list[str]], '']

structure_model = model.with_structured_output(review)

result = structure_model.invoke("<prompt>")

print(result.key_theme)