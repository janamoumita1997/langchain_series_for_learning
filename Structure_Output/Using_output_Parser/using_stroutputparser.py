# # using result.content -> without stroutputparser
# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# from langchain_core.prompts import PromptTemplate

# llm = HuggingFacePipeline.from_model_id(
#     model_id="Qwen/Qwen2.5-0.5B-Instruct",
#     task = "text-generation"
# )
# model = ChatHuggingFace(llm = llm)

# template1 = PromptTemplate(
#     template="write a details report on {topic}",
#     input_variables=['topic']
# )

# template2 = PromptTemplate(
#     template="write a 1 lines summary on a give /n {text}",
#     input_variables=['text']
# )

# prompt1 = template1.invoke({'topic':'black hole in 3 line '})

# result1 = model.invoke(prompt1)

# prompt2 = template2.invoke({"text":result1.content})

# result2 = model.invoke(prompt2)

# print(result2)


# with parser
# using result.content -> without stroutputparser
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task = "text-generation"
)
model = ChatHuggingFace(llm = llm)

template1 = PromptTemplate(
    template="write a 3 lines report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="write a 1 lines summary on a give /n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser |template2 | model | parser

result = chain.invoke({"topic":"black hole"})

print(result)