#!/usr/bin/env python
# coding: utf-8

# Import dependencies
print("Starting...")
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
print("Getting website content")

# GET html from website
request = requests.get("https://punchng.com/")
# Print request result
print(f"Request Status: {request.status_code}")

source = request.content

# Convert to BeautifulSoup object
soup = BeautifulSoup(source, 'html.parser')

# Get headline text from soup
raw_text = []
headlines = []
date = []
divs = soup.find_all('div', class_ = "title-box")

for div in divs:
    raw_text.append(div.text)
    
for text in raw_text:
    headline = text.strip('\n')
    headlines.append(headline)
    date.append(datetime.date.today().strftime("%d/%m/%Y"))

df = pd.DataFrame({"date": date,
                   "headline": headlines,
                  })

df.to_csv('headlines_data.csv', index=False, mode='a', header=False)

