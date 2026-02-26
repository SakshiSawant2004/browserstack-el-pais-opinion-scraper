from src.scraper import scrape_opinion
from src.translator import translate_titles
from src.analyzer import analyze_repeated_words
from src.image_downloader import download_images
from src.browserstack_parallel import run_parallel_tests

def main():

    # Scrape articles
    articles = scrape_opinion()

    print("\nSpanish Articles:")
    for i, a in enumerate(articles):
        print("\nArticle", i+1)
        print("Title:", a["title"])
        print("Content:", a["content"])

    # Download images
    download_images(articles)

    # Translate titles
    translated_headers = translate_titles(articles)

    print("\nEnglish Headers:")
    for header in translated_headers:
        print(header)

    # Word analysis
    analyze_repeated_words(translated_headers)

    # BrowserStack parallel testing
    print("\nRunning BrowserStack Parallel Tests...")
    run_parallel_tests()

if __name__ == "__main__":
    main()