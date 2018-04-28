"""
Code for sentiment analysis of tweets and tokenization

TO DO:
    Add rest of bitcoin data
    Write the label to the data
    DRY

"""

from textblob import TextBlob
import json

# read in data
data = []
files = ['bitcoin_tweet.json', 'bitcoin_tweet2.json', 'bitcoin_tweet3.json', 'bitcoin_tweet4.json']

for f in files:
    with open(f, 'r') as read_file:
        for line in read_file:
            data.append(json.loads(line))

combined_data = []

# convert tweet text to text blob and get sentiment, write to new json file
for tweet in data:
    tb = TextBlob(tweet["text"])
    
    # note: sentiment is a Sentiment object in form:
    # Sentiment(polarity = -1 <= n <= 1, subjectivity = 0 <= n <= 1)
    sent = tb.sentiment

    data = {"tweet" : tb, "sentiment" : sent }
    
    with open('data_file.json', 'w') as write_file:
        json.dump(data, write_file)




# should try different experiemnts for tokenization and n-grams. 
# n = 2 or 3
# tb.ngrams(n = 3)
# returns Wordlist object
