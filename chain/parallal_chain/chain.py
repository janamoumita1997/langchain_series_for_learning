from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

llm1 = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen2.5-0.5B-Instruct",
    task = "text-generation"
)

model1 = ChatHuggingFace(llm = llm1)


llm2 = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen2.5-0.5B-Instruct",
    task = "text-generation"
)

model2 = ChatHuggingFace(llm = llm2)


prompt1 = PromptTemplate(
    template="Generate short and simple notes from the following text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate 5 short question answers from the following text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}",
    input_variables=['note','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'note': prompt1|model1|parser,
    'quiz': prompt2|model2|parser 
})

merge_chain = prompt3|model1|parser

chain = parallel_chain|merge_chain

text = """

"""

result = chain.invoke({"text":text})
print(result)

chain.get_graph().print_ascii()