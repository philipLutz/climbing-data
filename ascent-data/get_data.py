"""
HTML to CSV

We are going to parse the raw HTML from 8a.nu, and then convert the logged
ascents into CSV files. We are separating routes and boulders.
"""

import csv
from bs4 import BeautifulSoup

file_paths = [
    "/Users/philipandrewlutz/climbing-data/ascent-data/boulders.html",
    "/Users/philipandrewlutz/climbing-data/ascent-data/routes.html"
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
    
    # create dictionaries for each ascent
    ascents = []
    for grade_category in ascent_table.find_all("tbody"):
        grade = grade_category.find(class_="sub-header").th.text.strip()
        for item in grade_category.find_all(class_="col-name"):
            item_parts = [
                element for element in item.parent.contents if element != ' '
            ]
            
            name = item_parts[1].contents[0].text.strip().title()
            crag_untrimmed = item_parts[2].text.strip().split('\n')[0]
            crag = ""
            if not crag_untrimmed.isalpha():
                split_index = len(crag_untrimmed)
                for index, char in enumerate(crag_untrimmed):
                    if not char.isalpha() and not char.isspace():
                        split_index = index - 1
                        break
                crag = crag_untrimmed[:split_index]
            else:
                crag = crag_untrimmed
            date = item_parts[3].text.strip()
            comment = item_parts[4].text.strip()
                
            ascent = {
                "name": name,
                "crag": crag,
                "date": date,
                "grade": grade,
                "comment": comment
            }
            ascents.append(ascent)
        
    # Write to CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ["name", "crag", "date", "grade", "comment"]
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for ascent in ascents:
            writer.writerow(ascent)
        
    print("Finished write to:\n    " + csv_path + "\n")

for path in file_paths:
    parse_file(path)