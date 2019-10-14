# # import pandas as pd
# import pandas as pd
#
# # list of strings
# lst = ['Python', 'For', 'us', 'is',
#             'potion', 'for', 'prince', 'of', 'Parsia']
# #
# print(lst)
# # # Calling DataFrame constructor on list
# df = pd.DataFrame(lst)
# print(df)

# # Python code demonstrate creating
# # DataFrame from dict array / lists
# # By default addresses.

import pandas as pd

# intialise data of lists.
# data = {'Name':['Himanshu', 'Sagar', 'Ronak', 'Sourav'],
#         'Age':[20, 21, 19, 18]}
# print(data)
# # Create DataFrame
# df = pd.DataFrame(data)
# #
# # # Print the output.
# print(df)


# import pandas as pd
#
# Define a dictionary containing employee data
# data = {'Name':['Sachin', 'Sagar', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Wagholi', 'Moshi', 'Kharadi', 'Viman nagar'],
#         'Qualification':['MCA', 'BE', 'MA', 'Phd']}
#
# # Convert the dictionary into DataFrame
# df = pd.DataFrame(data)
#
# # select two columns
# print(df[['Name','Address','Age']])

#
# importing pandas package
# import pandas as pd
#
# # making data frame from csv file
# data = pd.read_csv("nba.csv", index_col ="Name")
#
# # retrieving row by loc method (like a vlookup in excel but mixed togather with offset to retrive coloumn names as well)
# print('-'*40,"\n")
# first = data.loc["Avery Bradley"]
# second = data.loc["Timofey Mozgov"]
#
#
# print(first, "\n\n", "-"*40,"\n\n", second)
# print("\n",'-'*40,"\n")

# importing pandas package
# import pandas as pd
#
# # making data frame from csv file
# data = pd.read_csv("nba.csv", index_col ="Name")
#
# # retrieving columns by indexing operator
# first = data["Age"]
# print(first)

#
# import pandas as pd
#
# # making data frame from csv file
# data = pd.read_csv("nba.csv", index_col ="Name")
#
#
# # retrieving rows by iloc method
# row2 = data.iloc[3]
#
# print(row2)


#
#
# # importing pandas as pd
# import pandas as pd
#
# # importing numpy as np
# import numpy as np
#
# # # dictionary of lists
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score':[np.nan, 40, 80, 98]}
#
# # # creating a dataframe from list
# df = pd.DataFrame(dict)
# print(df)
# # using isnull() function
# print(df.isnull())


#
#
#
# importing pandas as pd
# import pandas as pd
#
# # importing numpy as np
# import numpy as np
#
# # dictionary of lists
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, 45, 56, np.nan],
#         'Third Score':[np.nan, 40, 80, 98]}
#
# # creating a dataframe from dictionary
# df = pd.DataFrame(dict)
# print(df)
# # filling missing value using fillna()
# df= df.fillna(0)
# print(df)
#

# # importing pandas as pd
# # import pandas as pd
# #
# # importing numpy as np
# import numpy as np
#
# # dictionary of lists
# dict = {'First Score':[100, 90, np.nan, 95],
#         'Second Score': [30, np.nan, 45, 56],
#         'Third Score':[52, 40, 80, 98],
#         'Fourth Score':[np.nan, np.nan, np.nan, 65]}
#
# # creating a dataframe from dictionary
# df = pd.DataFrame(dict)
#
# print(df)
# # using dropna() function to drop lines containing 'nan' data
# df=df.dropna()
# print(df)

#
#
# #
# # importing pandas as pd
import pandas as pd

# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
# dicts =[["aparna", "pankaj", "sudhir", "Geeku"],["MBA", "BCA", "M.Tech", "MBA"]]
# print(dicts)
# creating a dataframe from a dictionary
df = pd.DataFrame(dict)
print(df)
#writing data to excel file.
# df.to_excel("output.xlsx")
# print(df)

# # iterating over rows using iterrows() function
# for i, j in df.iterrows():
#     print(i, j)
#     print()
#
# creating a list of dataframe columns
# columns = list(df)
# # print(columns)
# #
# for i in columns:
#     # printing the third element of the column
#     print (df[i][0])
