"""
one drawback is that - out put will be a json but key and value decided by llm.
"""

from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

llm = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen2.5-0.5B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

parser = JsonOutputParser()

# template = PromptTemplate(
#     template = "write a name and age and city of a fictional person.\n {format_instruction}",
#     input_variables=[],
#     partial_variables={'format_instruction':parser.get_format_instructions()}
# )

# chain = template|model|parser

# res = chain.invoke({})
# print(res)

template = PromptTemplate(
    template = "write five facts about {topic}.\n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template|model|parser

res = chain.invoke({'topic':'black hole'})
print(res)