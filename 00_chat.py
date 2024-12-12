import openai

openai.api_key = ""

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role":"user",
            "content":"Como buscar documento en Worksite"
        }
    ],
    
)
print(response)