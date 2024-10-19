# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 10:53:46 2024

@author: Andrew Caruana
"""

# Import packages
from bs4 import BeautifulSoup
import requests
from fpdf import FPDF
import json

# Scrape website for 'data scientist' information
url = 'https://www.techtarget.com/searchenterpriseai/definition/data-scientist#:~:text=A%20data%20scientist%20is%20an,decision%2Dmaking%20in%20an%20organization.'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'lxml')

# Get the title of the page
title = soup.title.string.strip()

# Print the title with a newline for readability
print(title + '\n')  

# Initialise the sections list
sections = []

# Variable to hold the current section
current_section = {"header": None, "paragraphs": []}

# Create a PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Creation of page
pdf.add_page()
pdf.set_font("Arial", size=12)

# Add the title to the PDF
pdf.set_font("Arial", size=14, style='B')
pdf.multi_cell(0, 10, title + '\n')

# Add some space after the title
pdf.ln(10)  

# Iterate over all elements in the soup, checking for <h2>, <p>, or <li>
for element in soup.find_all(['h2', 'p', 'li']):
    if element.name == 'h2' and 'section-title' in element.get('class', []):
        # If we hit a new <h2>, save the previous section if it exists
        if current_section["header"]:
            sections.append(current_section)
        
        # Start a new section with this <h2> as the header
        h2_content = element.get_text().strip()
        
        # Print the section title with a newline
        print(h2_content + '\n')  
        pdf.set_font("Arial", size=12, style='B')
        pdf.multi_cell(0, 10, h2_content + '\n')
        
        # Add some space after the section title
        pdf.ln(5)  
        current_section = {"header": h2_content, "paragraphs": []}
    
    elif element.name == 'p':
        # Process <p> tags
        text = element.get_text().strip()
        
        # Check if the paragraph ends with '.' or ':', but not '...'
        if not text.endswith('...') and (text.endswith('.') or text.endswith(':') or text.endswith('.)')):
            
            # Print the paragraph with a newline
            print(text + '\n')  
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, text + '\n')
            pdf.ln(5)
            current_section["paragraphs"].append(text)
    
    elif element.name == 'li':
        # Process <li> tags with specific criteria
        text = element.get_text().strip()
        
        # Check if the list item ends with 'and', ';', or '.' but not '...'
        if (text.endswith('and') or text.endswith(';') or text.endswith('.')) and not text.endswith('...'):
            print(text + '\n')  # Print the list item with a newline
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, text + '\n')
            pdf.ln(5)
            current_section["paragraphs"].append(text)

# Append the last section if it's valid
if current_section["header"]:
    sections.append(current_section)

# Save the sections to a JSON file - Please enter filepath between inverted commas
with open(r"", "w") as json_file:
    json.dump(sections, json_file, indent=4)

# Save the content to a PDF file - Please enter filepath between inverted commas

print("PDF and JSON files have been created.")
