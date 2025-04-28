from langdetect import detect
from deep_translator import GoogleTranslator

def detect_language(text):
    """Detects the language of the given text."""
    return detect(text)

def translate_to_english(text):
    """Translates the given text to English if it's not in English."""
    try:
        return GoogleTranslator(source='auto', target='en').translate(text)
    except Exception as e:
        return f"Translation error: {str(e)}"
