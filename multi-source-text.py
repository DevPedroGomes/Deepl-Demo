import deepl
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

auth_key =   os.getenv("AUTH_KEY")
translator = deepl.Translator(auth_key)

# Translate text into a target language, in this case, French:
result = translator.translate_text("I hope someday we can live in March, what you think?", target_lang="FR")
print(result.text)  

print("")
# Translate multiple texts into British English
result = translator.translate_text(
    ["Isso aqui é um teste", "¿Cómo estás?", "How are we going to save the world?", "언젠가 3월에 살 수 있으면 좋겠는데, 어떻게 생각하세요"],
    target_lang="FR",
)
for text in result:
    print(text)

print("")

print(result[0].text) 
print(result[0].detected_source_lang)  
print(result[0].billed_characters)  
print("")
print(result[1].text)  
print(result[1].detected_source_lang)  
print(result[1].billed_characters)  


print("")
print("")


# Translate into German with less and more Formality:

print(
    translator.translate_text(
        "I hope this really works. Don't what what could really happen", target_lang="DE", formality="less"
    )
)
print(
    translator.translate_text(
        "I hope this really works.Don't what what could really happen", target_lang="DE", formality="more"
    )
)