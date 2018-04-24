"""
Code for sentiment analysis of tweets and tokenization

"""

from textblob import TextBlob
import json

# read in data
with open('bitcoin_tweet.json', 'r') as read_file1:
    btc_tweet1 = json.load(read_file1)
with open('bitcoin_tweet2.json', 'r') as read_file2:
    btc_tweet2 = json.load(read_file2)

# convert tweet text to text blob and get sentiment, write to new json file
for tweet in btc_tweet1:
    tb = TextBlob(tweet["text"])
    
    # note: sentiment is a Sentiment object in form:
    # Sentiment(polarity = -1 <= n <= 1, subjectivity = 0 <= n <= 1)
    sent = tb.sentiment

    data = {"tweet" : tb, "sentiment" : sent}
    
    with open('data_file.json', 'w') as write_file:
        json.dump(data, write_file)

# repeat for btc_tweet2
for tweet in btc_tweet2:
    tb = TextBlob(tweet["text"])
    sent = tb.sentiment

    data = {"tweet" : tb, "sentiment" : sent}
    
    with open('data_file.json', 'w') as write_file:
        json.dump(data, write_file)
        
# should try different experiemnts for tokenization and n-grams. 
# n = 2 or 3
# tb.ngrams(n = 3)
# returns Wordlist object
        