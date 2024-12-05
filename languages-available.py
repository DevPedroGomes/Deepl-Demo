#DEMO TO SHOWCASE FORMALITTY SUPPORTS
import deepl
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

auth_key =   os.getenv("AUTH_KEY")
translator = deepl.Translator(auth_key)

print("SOURCE LANGUAGES:")
for language in translator.get_source_languages():
    print(f"{language.name} ({language.code})")  

print("-----------------------------------------")
print("-----------------------------------------")

print("TARGET LANGUAGES:")
print("")

for language in translator.get_target_languages():
    if language.supports_formality:
        print(f"{language.name} ({language.code}) supports formality")
        # Example: "Italian (IT) supports formality"
    else:
        print(f"{language.name} ({language.code})")
        # Example: "Lithuanian (LT)"