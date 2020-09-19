"""
HTML to CSV

We are going to parse the raw HTML from 8a.nu, and then convert the logged
ascents into CSV files. We are separating routes and boulders.
"""

from bs4 import BeautifulSoup

# Parse saved HTML file
soup = BeautifulSoup(
    open("/Users/philipandrewlutz/climbing-data/ascent-data/boulders.html"),
    "html.parser")

ascent_table = soup.find("table", "user-ascents")

headers = []
for header in ascent_table.thead.find_all("th"):
    if header.text:
        headers.append(header.text.strip())

print(headers)