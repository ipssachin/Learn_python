#realtime analysis of web data
import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup

#provide web url to fetch the data from
# url = "https://www.hubertiming.com/results/2017GPTR10K"
# url = "https://www.hubertiming.com/results/2019Hope"
url = "https://www.hubertiming.com/results/2019Hope10K"
# url = input("Enter url: ")
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')
# print(soup)


# Get the title
title = soup.title+

# print(title)
# #
#
# # Print out the text
text = soup.get_text()
# print(soup.text)
#
#
# #use find_all() method to find html tag in the code eg. useful tags
# #include < a > for hyperlinks, < table > for tables, < tr > for table rows,
# #< th > for table headers, and < td > for table cells
#
# print(soup.find_all('a'))

# #to get a better view of it
# #
# all_links = soup.find_all("a")
# for link in all_links:
#     print(link.get("href"))
#     # print(link ,"\n")

# # We will pass <tr> tag to get the table and print the
# #first 10 rows for sanity check
#
rows = soup.find_all('tr')
# print(rows[:10])
#
# #to convert this raw table data in real table format so we can use this data as
# #our datafram in pandas for the analysis purpose.
#
# #get inner tag <td>
#
for row in rows:
    row_td = row.find_all('td')
# print(row_td)
# print(type(row_td))
#
# #clean the data and get the text
#
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
# print(cleantext)
#
# #lets use regular expression we learned in previous sessions
# #to get more clean dataframe
import re
#
list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
    # print(clean2)
# # print(type(clean2))
#
# #next step is to convert the list into a dataframe
# #and get a quick view of the first 10 rows using Pandas
df = pd.DataFrame(list_rows)
pdd=df.head(10)
# print(pdd)
#
#hurrahh!! not yet we need to perform data manipulation and cleaning.
#We are digital janitors

df1 = df[0].str.split(',', expand=True)
# print(df1.head(10))
#
# #table heads are missing
#
col_labels = soup.find_all('th')
all_header = []
col_str = str(col_labels)
cleantext2 = BeautifulSoup(col_str, "lxml").get_text()
all_header.append(cleantext2)
# print(all_header)
df2 = pd.DataFrame(all_header)
# print(df2.head())

df3 = df2[0].str.split(',', expand=True)
# print(df3.head())

frames = [df3, df1]
# print(frames)
#
df4 = pd.concat(frames)
# print(df4.head(10))
#
#
df5 = df4.rename(columns=df4.iloc[0])
#
# print(df5.head())
# print(df5.info())
# print(df5.shape)
df6 = df5.dropna(axis=0, how='any')
# print(df6.head())
df7 = df6.drop(df6.index[0])
# print(df7.head())
#
# #looks beautiful!! but we need to puff it littile more
#
df7.rename(columns={'[Place': 'Place'},inplace=True)
# df7.rename(columns={' Team]': 'Team'},inplace=True)
df7.rename(columns={' Gun Time]': 'Gun Time'},inplace=True)
# print(df7.head())
#
df7['Place'] = df7['Place'].str.strip('[')
# df7['Team'] = df7['Team'].str.strip(']')
df7['Gun Time'] = df7['Gun Time'].str.strip(']')
print(df7.head())
#
df7.to_csv('hubertiming_data.csv')
