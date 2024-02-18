# Description: This file contains the code to translate an input text from English to a selected language using the transformers model from huggingface
# Model and Tokenizer initialization
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
global tokenizer, model

# given the string of the language, return the language code
def get_language_code(language):
    languages = {
        "english": "en",
        "spanish": "es",
        "french": "fr",
        "german": "de",
        "italian": "it",
        "dutch": "nl",
        "portuguese": "pt",
        "russian": "ru",
        "chinese": "zh",
        "japanese": "ja",
        "korean": "ko",
        "arabic": "ar",
        "turkish": "tr",
        "vietnamese": "vi",
        "greek": "el",
        "hebrew": "he",
        "hindi": "hi",
        "indonesian": "id",
        "malay": "ms",
        "thai": "th",
        "swedish": "sv",
        "czech": "cs",
        "danish": "da",
        "finnish": "fi",
        "hungarian": "hu",
        "norwegian": "no",
        "polish": "pl",
        "romanian": "ro",
        "slovak": "sk",
        "ukrainian": "uk",
        "catalan": "ca",
        "basque": "eu",
        "galician": "gl",
        "scottish gaelic": "gd",
        "swahili": "sw",
        "welsh": "cy",
        "burundian": "rn",
        "somali": "so",
        "zulu": "zu",
        "afrikaans": "af",
        "albanian": "sq",
        "amharic": "am",
        "armenian": "hy",
        "azerbaijani": "az",
        "bengali": "bn",
        "bosnian": "bs",
        "bulgarian": "bg",
        "croatian": "hr",
        "czech": "cs",
        "danish": "da",
        "estonian": "et",
        "filipino": "tl",
        "finnish": "fi",
        "georgian": "ka",
        "greek": "el",
        "haitian creole": "ht",
        "hebrew": "he",
        "hindi": "hi",
        "hungarian": "hu",
        "icelandic": "is",
        "igbo": "ig"
    }
    return languages.get(language.lower(), "en")

# using the transformers model from huggingface, ask the user to select a language and then translate an input text from english to the selected language
# The user can select the language by typing the language name or the language code
# The user can also select the language by typing the language name or the language code
def translate(text, language):
    global tokenizer, model
    # translate the input text
    translated = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    # undo tokenization the translated text and return it
    decoded = tokenizer.decode(translated[0], skip_special_tokens=True)
    return decoded

def initializeModel(language):
    global tokenizer, model
    tokenizer = AutoTokenizer.from_pretrained(f'Helsinki-NLP/opus-mt-en-{language}')
    model = AutoModelForSeq2SeqLM.from_pretrained(f'Helsinki-NLP/opus-mt-en-{language}')

# Example usage
def example():
    #choose language and initialize model
    language = input("Choose Language: ")
    lang = get_language_code(language)
    initializeModel(lang)

    #input text and translate
    text = input(translate("Enter the text you want to translate: ", lang))
    print(translate(text, lang))

example()

