import requests
import os

def download_images(articles):

    os.makedirs("images", exist_ok=True)

    for i, article in enumerate(articles):

        if article["image"]:

            try:
                response = requests.get(article["image"])

                with open(f"images/article_{i+1}.jpg", "wb") as f:
                    f.write(response.content)

            except:
                pass