from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

model = OpenAI()

json_schema = {
    "title":"Review",
    "type":'object',
    "properties":{
        "key_theme":{
            "type":"array",
            "items":{
                "type":"string"
            },
            "description":""
        },
        "summary":{
            "type":"string",
            "description":""
        },
        "key_theme":{
            "type":"String",
            "enum":['pos','neg'],
            "description":""
        },
        "pros":{
            "type":["array","null"],
            "items":{
                "type":"string"
            },
            "description":""
        }
    }

}

structure_model = model.with_structured_output(json_schema)

result = structure_model.invoke("<prompt>")

print(result.key_theme)
