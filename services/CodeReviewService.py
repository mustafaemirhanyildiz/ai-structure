
from prompts.en import GptPromptBuilderEn
from openai import OpenAI
import os
import json
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def review_code_for_clean_principles(code_string:str):

    response = client.chat.completions.create(
        model= "gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": GptPromptBuilderEn.build_chat_prompt_user(code_string)},
            {"role": "user", "content": GptPromptBuilderEn.build_chat_prompt_system()}
        ],
        response_format={"type": "json_object"},
        frequency_penalty=0.2,
        presence_penalty=0.2,
        temperature=0.5
    )
    
    json_response = json.loads(response.choices[0].message.content)
    return json_response