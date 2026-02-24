import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)


def translate_and_structure(text: str, chunk_size=4000) -> str:
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    outputs = []

    for chunk in chunks:
        prompt = f"""
متن زیر را به فارسی روان ترجمه کن و به صورت جزوه دانشگاهی ساختاردهی کن:

{chunk}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        outputs.append(response.choices[0].message.content)

    return "\n\n".join(outputs)
