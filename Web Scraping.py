import requests
from bs4 import BeautifulSoup

def get_title(url):
    """
    Returns the title of the webpage at the given url
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find('title').get_text()
    

print(get_title("https://github.com"))

print(get_title("https://yahoo.com/news"))
