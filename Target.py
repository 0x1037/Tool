import requests
from bs4 import BeautifulSoup

visited_urls = set()


def spider_url(url, keyword):
    global urls  

    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Request failed for {url}. Error: {e}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tags = soup.find_all('a')
        urls = []

        for tag in a_tags:
            href = tag.get("href")
            if href is not None and href != "":
                urls.append(href)
        print(urls)


# Example usage:
url = input("Enter Your Target: ")
kword = input("Enter The Keyword: ")
spider_url(url, "google")
