# Text Mining using News API with CountVectorizer and TF-IDF

This repository demonstrates text mining techniques using the News API, CountVectorizer, and TF-IDF (Term Frequency-Inverse Document Frequency). The aim is to extract insights from news articles using these text processing methods.

## Getting Started

To get started with this project, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/text-mining-news-api.git
```

2. Install the required dependencies. 

3. Sign up for the News API and get your API key. You can sign up [here](https://newsapi.org/).

4. Replace `'YOUR_API_KEY'` in the `config.py` file with your actual News API key.

## Implementation Details

### 1. Data Collection

This project fetches news articles using the News API. The `NewsAPI` class in the `news_api.py` file handles the interaction with the API. You need to provide your API key in the `config.py` file to access the News API.

### 2. Text Preprocessing

Before analyzing the text, we preprocess it by:

- Removing stopwords
- Tokenization
- Lowercasing
- Removing punctuation
- Lemmatization (optional)

### 3. CountVectorizer

We use the `CountVectorizer` from the `sklearn.feature_extraction.text` module to convert the text data into a matrix of token counts. This matrix represents the frequency of each word in the corpus.

### 4. TF-IDF (Term Frequency-Inverse Document Frequency)

TF-IDF is a numerical statistic that reflects the importance of a word in a document relative to a collection of documents. We use the `TfidfVectorizer` from the `sklearn.feature_extraction.text` module to compute the TF-IDF scores for each word in the corpus.
