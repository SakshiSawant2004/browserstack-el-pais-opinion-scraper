import time
from bs4 import BeautifulSoup
from src.driver import get_driver

def scrape_opinion():

    driver = get_driver()

    driver.get("https://elpais.com/opinion/")
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    articles = soup.find_all("article")[:5]

    data = []

    for article in articles:

        title = article.find("h2")
        content = article.find("p")
        img = article.find("img")

        data.append({
            "title": title.text if title else "",
            "content": content.text if content else "",
            "image": img["src"] if img and img.get("src") else None
        })

    driver.quit()
    return data