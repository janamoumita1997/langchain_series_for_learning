from typing import TypedDict

class person(TypedDict):
    name:str
    age: int

new_person:person = {'name':'Moumita','age':123}

print(new_person)