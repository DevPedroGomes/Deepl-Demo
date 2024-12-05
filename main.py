import deepl
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

auth_key =   os.getenv("AUTH_KEY")
translator = deepl.Translator(auth_key)

result = translator.translate_text("Parlez-moi, mon ami", source_lang="FR", target_lang="PT-BR")
print(result.text)  




