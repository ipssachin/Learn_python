import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.hubertiming.com/results/2019Hope10K"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
title = soup.title
text = soup.get_text()
rows = soup.find_all('tr')
for row in rows:
    row_td = row.find_all('td')
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()

import re
list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)

df = pd.DataFrame(list_rows)
pdd=df.head(10)
df1 = df[0].str.split(',', expand=True)

col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
df2 = pd.DataFrame(all_header)
df3 = df2[0].str.split(',', expand=True)

frames = [df3, df1]
df4 = pd.concat(frames)
df5 = df4.rename(columns=df4.iloc[0])
df6 = df5.dropna(axis=0, how='any')
df7 = df6.drop(df6.index[0])

df7.rename(columns={'[Place': 'Place'},inplace=True)
df7.rename(columns={' Gun Time]': 'Gun Time'},inplace=True)


df7['Place'] = df7['Place'].str.strip('[')
df7['Gun Time'] = df7['Gun Time'].str.strip(']')

df7.to_csv('hubertiming_data.csv')
