#from bs4 import BeautifulSoup
# import requests

# url = "https://indianexpress.com/"
# response = requests.get(url)
# soup = BeautifulSoup(requests.text, "html.parser")
# print(soup.title.text)

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
def get_news():
    url = "https://indianexpress.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title=[]
				
    for items in soup.find_all("a",class_="article-click topblockNews__sidebarLink"):
        title.append(items.text)

        return {
            "news":title
        }