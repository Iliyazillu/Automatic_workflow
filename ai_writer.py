import openai

openai.api_key = "your-api-key"

def spin_text(original_text):
    prompt = f"Rewrite this chapter creatively while keeping its meaning:\n\n{original_text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
