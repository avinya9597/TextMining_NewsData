# -*- coding: utf-8 -*-
"""CountVectorize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BILzsmN4JipVpAO242gADyQgMAc_4jPu
"""

import pandas as pd
#import countVectorizer
from sklearn.feature_extraction.text import CountVectorizer

"""### Sample texts to show the working of Countvectorizer in Python"""

texts = [
    "I like drinking hot chocolate today",
    "I made Hot chocolate today"]

"""
In the context of CountVectorizer, fit_transform serves two purposes:

Fit: It learns the vocabulary dictionary of the corpus (a collection of text documents) and builds the document-term matrix based on the frequencies of words in the documents. During this step, it analyzes the corpus to determine the unique words (features) in the documents.

Transform: It transforms the text documents into the document-term matrix, where rows represent documents, columns represent words, and the values represent the frequencies of words in each document. Once the vocabulary is learned, this method transforms the input text into numerical vectors based on the learned vocabulary."""

#you can include custom stopwords stop_words=’english’; stop_words= ['I']
#use max_df,min_df : Max_df looks at how many documents contain the word
#and if it exceeds the max_df threshold then it is eliminated from the sparse matrix.
#Min_df if words appear in only 1 or 2 documents, now these could be ignored as they do not provide enough information
#takes abosulte and percentage values
#max_features = numbers of features you want to consider
# by default LOWERCASE  is set True
# if tokenpattern is undefined, 'i' will not be shown. TokenPattern removes tokens of a single character

coun_vect = CountVectorizer(token_pattern=r"\b\w+\b")
count_matrix = coun_vect.fit_transform(texts)
count_array = count_matrix.toarray()
df = pd.DataFrame(data=count_array,columns = coun_vect.get_feature_names_out())
print(df)

# ********************************************************************************************************************************

df = pd.read_csv('/content/FinalData.csv')

df.sample(frac=1).head(10)

df.isnull().sum()
df.dropna(inplace=True)

def count_vectorize(label_col_name, text_col_name):
    countVectorizer = CountVectorizer(max_df=6, min_df=1, strip_accents="ascii",stop_words='english', max_features=2000)
    countVector = countVectorizer.fit_transform(text_col_name)
    count_vect_df = pd.DataFrame(countVector.toarray(), columns=countVectorizer.get_feature_names_out())
    import re
    cols_to_drop = []
    for col_name in count_vect_df:
        if re.search(r'\d', col_name):
            cols_to_drop.append(col_name)

    count_vect_df.drop(columns=cols_to_drop, inplace=True)
    return count_vect_df, labels

labels = df["Label"]
description = df["Description"]
desc_li = description.to_list()

count_vect_df, labels = count_vectorize(labels,desc_li)

count_vect_df.head()

#############################################################################################################################################################################