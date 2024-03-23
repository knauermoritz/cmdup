from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
def llm(systemprompt, prompt):
    completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": systemprompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        model="gemma"
    )

    return completion.choices[0].message.content