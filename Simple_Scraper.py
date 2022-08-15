from bs4 import BeautifulSoup
import requests
import re
url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
html_text = requests.get(url).text

soup = BeautifulSoup(html_text, "lxml")

jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")

for i in jobs:
    print(re.sub("\s+"," ",i.h2.text))
