"""
HTML to CSV

Parses the raw HTML from 8a.nu and then converts the logged
ascents into CSV files. Navigate to your logbook and load all ascents. 
Save the current pages as HTML files to use for this script.
"""

import csv
from bs4 import BeautifulSoup

# Separate files for boulders and routes
file_paths = [
    "/Users/philipandrewlutz/climbing-data/ascent-data/boulders.html",
    "/Users/philipandrewlutz/climbing-data/ascent-data/routes.html"
]

def parse_file(path):
    """
    Creates CSV file of ascents from 8a.nu HTML file
    """
    # Format the following variables accordingly to your machine and files
    reference_string = path[50:]
    reference_string = reference_string.split('.')[0]
    csv_path = ("/Users/philipandrewlutz/climbing-data/ascent-data/ascents_" 
        + reference_string + ".csv")
    
    soup = BeautifulSoup(open(path),"html.parser")
    ascent_table = soup.find("table", "user-ascents")
    
    # Create dictionaries for each ascent
    ascents = []
    for grade_category in ascent_table.find_all("tbody"):
        grade = grade_category.find(class_="sub-header").th.text.strip()
        for item in grade_category.find_all(class_="col-name"):
            item_parts = [
                element for element in item.parent.contents if element != ' '
            ]
            style = item_parts[0].i.get('title').title()
            name = item_parts[1].contents[0].text.strip().title()
            crag_untrimmed = item_parts[2].text.strip().split('\n')[0]
            crag = ""
            if not crag_untrimmed.isalpha():
                split_index = len(crag_untrimmed)
                for index, char in enumerate(crag_untrimmed):
                    if char == '(':
                        split_index = index - 1
                        break
                crag = crag_untrimmed[:split_index]
            else:
                crag = crag_untrimmed
                
            sub_crag = item_parts[2].contents[2].text.strip().title()
            if crag != sub_crag:
                crag = crag + "/" + sub_crag
            
            date = item_parts[3].text.strip()
            comment = item_parts[4].text.strip()
                
            ascent = {
                "NAME": name,
                "CRAG": crag,
                "DATE": date,
                "GRADE": grade,
                "STYLE": style,
                "COMMENT": comment
            }
            ascents.append(ascent)
        
    # Write ascents to CSV file
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ["NAME", "CRAG", "DATE", "GRADE", "STYLE", "COMMENT"]
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        for ascent in ascents:
            writer.writerow(ascent)
    
    print("Finished write to:\n    " + csv_path + "\n")

for path in file_paths:
    parse_file(path)