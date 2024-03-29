# -*- coding: utf-8 -*-
"""News_API_ExtractData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gfjn-1zKONiJ5Sx4A_szKrNvaXVlFMcr
"""

#impotr required libraries
import requests
import re
import os
import pandas as pd

#API key
secret = os.environ(NEWS_API_KEY)
query1 = "recession"
query2 = "ai"
query3 = "technology"
query4 = "economics"

url = 'https://newsapi.org/v2/everything?'

"""### Recession"""

#providing the query parameters
parameters = {
    'q': query1, # query phrase
    'pageSize': 100,  # maximum is 100
    'apiKey': secret, # your own API key
    'sortBy':'popularity'
}
# Call API using get method
response1 = requests.get(url, params=parameters)
# Convert the response to JSON format and pretty print it
response_json1 = response1.json()

"""### AI"""

parameters = {
    'q': query2, # query phrase
    'pageSize': 100,  # maximum is 100
    'apiKey': secret, # your own API key
    'sortBy':'popularity'
}
# Call API using get method
response2 = requests.get(url, params=parameters)
# Convert the response to JSON format and pretty print it
response_json2 = response2.json()

"""### Technology"""

parameters = {
    'q': query3, # query phrase
    'pageSize': 100,  # maximum is 100
    'apiKey': secret, # your own API key
    'sortBy':'popularity'
}
# Call API using get method
response3 = requests.get(url, params=parameters)
# Convert the response to JSON format and pretty print it
response_json3 = response3.json()

"""### Economics"""

parameters = {
    'q': query4, # query phrase
    'pageSize': 100,  # maximum is 100
    'apiKey': secret, # your own API key
    'sortBy':'popularity'
}
# Call API using get method
response4 = requests.get(url, params=parameters)
# Convert the response to JSON format and pretty print it
response_json4 = response4.json()

"""## Extract articles by querying the urls and create a text file for each

### Recession Articles
"""

for i, article in enumerate(response_json1["articles"]):
      #print("Extracting Data from URL - %s"%article["url"])
      content_li = article["description"]
      #if there is any empty description, handle the exception
      if content_li is None:
        pass
      else:
        with open("/content/%s/%s_%d.txt"%(query1, query1, i), "w+", encoding="utf-8") as file_obj:
            file_obj.writelines(content_li)
        #print("Success")

"""### AI Articles"""

for i, article in enumerate(response_json2["articles"]):
      #print("Extracting Data from URL - %s"%article["url"])
      content_li = article["description"]
      #if there is any empty description, handle the exception
      if content_li is None:
        pass
      else:
        with open("/content/%s/%s_%d.txt"%(query2, query2, i), "w+", encoding="utf-8") as file_obj:
            file_obj.writelines(content_li)
        #print("Success")

"""### Technology Articles"""

for i, article in enumerate(response_json3["articles"]):
      #print("Extracting Data from URL - %s"%article["url"])
      content_li = article["description"]
      #if there is any empty description, handle the exception
      if content_li is None:
        pass
      else:
        with open("/content/%s/%s_%d.txt"%(query3, query3, i), "w+", encoding="utf-8") as file_obj:
            file_obj.writelines(content_li)
        #print("Success")

"""### Economics Articles"""

for i, article in enumerate(response_json4["articles"]):
      #print("Extracting Data from URL - %s"%article["url"])
      content_li = article["description"]
      #if there is any empty description, handle the exception
      if content_li is None:
        pass
      else:
        with open("/content/%s/%s_%d.txt"%(query4, query4, i), "w+", encoding="utf-8") as file_obj:
            file_obj.writelines(content_li)
        #print("Success")

"""## Add labels and description in list and create dataframe

### Recession DataFrame
"""

Description = []
recession = []
for ll in os.listdir("/content/recession/"):
    with open("/content/recession/%s"%ll, "r", encoding='ISO-8859-1') as file_obj:
        content = file_obj.read()
        Description.append(content)
        recession.append("recession")

rdf = pd.DataFrame(list(zip(recession, Description)), columns=["Label", "Description"])

rdf.head()

"""### AI DataFrame"""

Description = []
ai = []
for ll in os.listdir("/content/ai/"):
    with open("/content/ai/%s"%ll, "r", encoding='ISO-8859-1') as file_obj:
        content = file_obj.read()
        Description.append(content)
        ai.append("ai")

adf = pd.DataFrame(list(zip(ai, Description)), columns=["Label", "Description"])
adf.head()

"""### Technology DataFrame"""

Description = []
technology = []
for ll in os.listdir("/content/technology/"):
    with open("/content/technology/%s"%ll, "r", encoding='ISO-8859-1') as file_obj:
        content = file_obj.read()
        Description.append(content)
        technology.append("technology")

tdf = pd.DataFrame(list(zip(technology, Description)), columns=["Label", "Description"])
tdf.head()

"""### Economics DataFrame"""

Description = []
economics = []
for ll in os.listdir("/content/economics/"):
    with open("/content/economics/%s"%ll, "r", encoding='ISO-8859-1') as file_obj:
        content = file_obj.read()
        Description.append(content)
        economics.append("economics")

edf = pd.DataFrame(list(zip(economics, Description)), columns=["Label", "Description"])
edf.head()

"""## Merge all the dataframes"""

result = pd.concat([rdf, adf, tdf, edf], axis=0)

result.reset_index(drop = True, inplace = True)
result.to_csv("/content/FinalData.csv", index=False)

result.sample(frac=1).head(10)

########################################################################################################################################