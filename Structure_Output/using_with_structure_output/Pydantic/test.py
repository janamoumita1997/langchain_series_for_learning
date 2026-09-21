from pydantic import BaseModel,Field
from typing import Optional, Annotated 

class student(BaseModel):
    name:str = "Moumita"
    age:int = None
    cgpa:float = Field(gt = 1,lt = 10, default = 5, description='')

new_student = {'name':'Akash', 'age':32}
st = student(**new_student) 

print(st)