from pydantic import BaseModel
from agents import RunConfig ,Agent, Runner,AsyncOpenAI, OpenAIChatCompletionsModel
import os
gemini_api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

Model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)
run_config =RunConfig(
    model=Model,
    model_provider=external_client,


)
# class User(BaseModel):
#     name :str
#     age :int


# user =User(name ="urooj", age = 19 )   
# print(user.age)

# from typing import Optional

# class User(BaseModel):
#     name: str
#     age: Optional[int] = None

# user =User(name ="urooj")       
# print(user.age)
# from openai import tool



# class MathInput(BaseModel):
#     x: int
#     y: int

# @tool
# def add_numbers(input: MathInput) -> str:
#     return str(input.x + input.y)

# data=MathInput(x = 10 , y =20)
# print(data.x)