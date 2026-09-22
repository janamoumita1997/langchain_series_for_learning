from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

llm = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen2.5-0.5B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

schema = [
    ResponseSchema(name= 'fact1', description= "fact 1 about the topic"),
    ResponseSchema(name= 'fact2', description= "fact 2 about the topic"),
    ResponseSchema(name= 'fact3', description= "fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schema(schema)

template = PromptTemplate(
    template='Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


chain = template | model | parser

result = chain.invoke({'topic':"balck hole"})

print(result)