import threading
import time
from selenium import webdriver
from src.browserstack_config import BROWSERSTACK_URL

def run_browser_test():

    options = webdriver.ChromeOptions()

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    driver.get("https://elpais.com")

    # Page load wait ⭐
    time.sleep(3)

    print("Browser Title:", driver.title)

    driver.quit()


def run_parallel_tests():

    threads = []

    for i in range(5):   # 5 parallel threads
        t = threading.Thread(target=run_browser_test)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
