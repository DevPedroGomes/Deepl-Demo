import requests
import os
import time
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

auth_key =   os.getenv("AUTH_KEY")

def translate_text(text, lang_from, lang_to, api_key, formality="default"):
    #formality options are: "more", "less", "prefer_more", "prefer_less"
    url = "https://api-free.deepl.com/v2/translate"
    data = {
        "auth_key": api_key,
        "text": text,
        "source_lang": lang_from,
        "target_lang": lang_to,
        "formality": formality
    }
    
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        print(response.json())
        return response.json().get("translations")[0].get("text")
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")


text="Hey Rai, whats up! This is a little test for this translation application, haha."
result = translate_text(text, "EN", "FR", api_key=auth_key, formality="less")
print(result)
