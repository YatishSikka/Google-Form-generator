import os
import openai
from dotenv import load_dotenv
from form import form_link

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")

openai.api_key = API_KEY

form_title = input("Enter the form title: ")

query = "write 10 questions for a google form on the topic "+form_title+" and just return questions with options for answers and start each question with # sign instead of numbers and start each option with alphabets instead of bullets and do not return any other text"
queries = [{'role':"user","content":"You are a kind and helpful assistant"},]
msg = {"role": "user","content": query}
queries.append(msg)
chat = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=queries
)

reply = chat.choices[0].message.content
qa_set = reply.split("\n")
for i in qa_set:
    if(len(i)<1):
        qa_set.remove(i)
print(form_link(form_title,qa_set))