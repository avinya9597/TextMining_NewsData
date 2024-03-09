# Tokenization Techniques

This repository contains examples of various tokenization techniques commonly used in natural language processing (NLP). Tokenization is the process of breaking down text into smaller units, usually words or subwords, which are then used as input for further NLP tasks such as parsing, sentiment analysis, and named entity recognition.

## List of Tokenization Techniques

1. **Whitespace Tokenization**: This technique splits text based on whitespace characters such as spaces, tabs, and newlines.

2. **Word Tokenization**: Word tokenization splits text into individual words. It typically handles punctuation marks and special characters as separate tokens.

3. **Sentence Tokenization**: Sentence tokenization divides text into individual sentences. It uses punctuation marks such as periods, exclamation marks, and question marks to determine sentence boundaries.

4. **Punctuation Tokenization**: This technique tokenizes text based on punctuation marks while retaining the punctuation marks as separate tokens.

5. **Regular Expression Tokenization**: Regular expression tokenization uses user-defined regular expressions to split text into tokens. This allows for more customized tokenization based on specific patterns.

6. **N-gram Tokenization**: N-gram tokenization generates tokens by sliding a window of size N over the text and extracting substrings of length N. This can capture both individual words and phrases of varying lengths.

7. **Byte Pair Encoding (BPE)**: BPE tokenization is a subword tokenization technique that iteratively merges the most frequent pairs of characters or tokens to build a vocabulary. This is particularly useful for handling out-of-vocabulary words and rare terms.

8. **WordPiece Tokenization**: WordPiece tokenization is similar to BPE but operates at the level of word pieces instead of characters. It is commonly used in models like BERT for subword tokenization.
