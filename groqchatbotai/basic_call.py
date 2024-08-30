import os

from groq import Groq
print(os.environ.get("GROQ_API_KEY"))
client = Groq(
    api_key="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",

)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "tell a joke",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)