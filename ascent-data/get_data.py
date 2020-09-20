"""
HTML to CSV

We are going to parse the raw HTML from 8a.nu, and then convert the logged
ascents into CSV files. We are separating routes and boulders.
"""

import csv
from bs4 import BeautifulSoup

file_paths = [
    "/Users/philipandrewlutz/climbing-data/ascent-data/boulders.html",
    #"/Users/philipandrewlutz/climbing-data/ascent-data/routes.html"
]

def parse_file(path):
    """
    Creates CSV file of ascents from 8a.nu HTML
    """
    reference_string = path[50:]
    reference_string = reference_string.split('.')[0]
    csv_path = ("/Users/philipandrewlutz/climbing-data/ascent-data/ascents_" 
        + reference_string + ".csv")
    
    soup = BeautifulSoup(open(path),"html.parser")
    ascent_table = soup.find("table", "user-ascents")

    #headers = []
    # for header in ascent_table.thead.find_all("th"):
    #     if header.text:
    #         headers.append(header.text.strip())
    
    # create dictionaries for each ascent
    
    
    
    # Write to CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ["name", "crag", "date", "grade", "comment"]
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)

        writer.writeheader()
        writer.writerow({
            "name": "Mandala",
            "crag": "Bishop",
            "date": "11/8/2021",
            "grade": "8A+",
            "comment": "Sick!"
        })
        
    print("Finished write to:")
    print("    " + csv_path + "\n")
    

for path in file_paths:
    parse_file(path)