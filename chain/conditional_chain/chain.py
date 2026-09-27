from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain.schema.runnable import RunnableParallel, Runnablebranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

llm = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen2.5-0.5B-Instruct",
    task = "text-generation"
)
model = ChatHuggingFace(llm = llm)

parser2 = StrOutputParser()

class feedback(BaseModel):
    sentiment: Literal['pos','neg'] = Field(description="Sentiment of the comment of product review")

parser = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template="Analyze the sentiment of the given text and classify the feedback: {text}, \n {format_instruction}",
    input_variables=['text'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain = prompt1 | model | parser

# result = chain.invoke({"text":"nice product. go for it guys."}).sentiment

# print(result)

conditional_chain = Runnablebranch(
    (condition1, chain1),
    (conditional2, chain2)
)

final_chain = chain | conditional_chain
res = final_chain.invoke("text":"")
print(res)