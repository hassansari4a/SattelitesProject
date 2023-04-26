import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table', class_='wikitable sortable')
headers = [header.text.strip() for header in table.find_all('th')]
rows = []
for row in table.find_all('tr')[1:]:
    cells = [cell.text.strip() for cell in row.find_all('td')]
    rows.append(cells)

df = pd.DataFrame(rows, columns=headers)
df.drop(['Year', 'ccTLD', 'Notes'], axis=1, inplace=True)
df.to_csv('geocode.csv')