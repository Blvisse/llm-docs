import os
from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI
from pytest import skip


# @skip("Generates real costs")
# def test_open_api_response():
#     open_api_key = os.getenv("OPEN_API_KEY")
#     openai_client = OpenAI(api_key=open_api_key)
#     response = openai_client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user",
#                    "content": "write a small hello world poem"}]
#     )
#     assert "hello world" in response.choices[0].message.content
#     assert open_api_key is not None
