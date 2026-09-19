# # using huggingface API

# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# load_dotenv()

# from huggingface_hub import login

# # Interactive login (prompts for token or uses browser)
# login()

# # Non-interactive login with a specific token
# login(token="")   

# llm = HuggingFaceEndpoint(
#     repo_id = "deepseek-ai/DeepSeek-V4.1-Flash",
#     task = "text-generation"
# )
# model = ChatHuggingFace(llm = llm)

# result = model.invoke("what is the capital of India?")

# print(result.content)


## Using Huggingface downloaded model

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
load_dotenv()

# from huggingface_hub import login

# # Interactive login (prompts for token or uses browser)
# login()

llm = HuggingFacePipeline.from_model_id(
    model_id= "Qwen/Qwen2.5-Coder-3B-Instruct",
    task = "text-generation",
    pipeline_kwargs= dict(
        temperqture = 0.5,
        max_new_tokens = 500
    )
)

model = ChatHuggingFace(llm = llm)

result = model.invoke("what is the capital of India?")

print(result.content)