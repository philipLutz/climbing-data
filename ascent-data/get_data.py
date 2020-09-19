#import pandas as pd
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("/Users/philipandrewlutz/climbing-data/ascent-data/boulders.html"), "html.parser")
#print(soup.prettify())
#print(soup.find("table", "user-ascents"))

ascent_table = soup.find("table", "user-ascents")
#print(type(ascent_table))
#for child in ascent_table.contents:
    #print(child)
#print(ascent_table.thead.find_all("th"))

headers = []
for header in ascent_table.thead.find_all("th"):
    if header.text:
        headers.append(header.text.strip())

print(headers)