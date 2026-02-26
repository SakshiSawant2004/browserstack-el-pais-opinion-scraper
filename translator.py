import requests

def translate_titles(articles):

    translated_headers = []

    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com",
        "X-RapidAPI-Key": "824f6aa3f5msh8b867de2629129ap1fd87bjsn6ee979d7bfde"
    }

    for article in articles:

        payload = {
            "from": "es",
            "to": "en",
            "q": article["title"]
        }

        response = requests.post(url, json=payload, headers=headers)

        data = response.json()

        # ✅ Fix — list response handle karo
        translated_headers.append(data[0])

    return translated_headers