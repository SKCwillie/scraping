import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://fbref.com/en/comps/22/Major-League-Soccer-Stats'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find_all('table', {'id':'stats_squads_standard_for'})
df = pd.read_html(str(table))[0]
print(df)