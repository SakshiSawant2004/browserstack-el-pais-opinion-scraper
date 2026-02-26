from deep_translator import GoogleTranslator

def translate_titles(articles):

    translated_headers = []

    for article in articles:

        translated = GoogleTranslator(source='es', target='en').translate(
            article["title"]
        )

        translated_headers.append(translated)

    return translated_headers

