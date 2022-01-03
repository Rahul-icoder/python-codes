import requests
from bs4 import BeautifulSoup
URL = 'https://www.youtube.com/watch?time_continue=17&v=2wEA8nuThj8'
page = requests.get(URL)
s = BeautifulSoup(page.text, "html.parser")
views = s.find("div", class_="watch-view-count").text
likes = s.find("span", class_="like-button-renderer").span.button.text
data = {'views':views, 'likes':likes}
print(data)
