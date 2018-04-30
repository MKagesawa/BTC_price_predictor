"""
Code for sentiment analysis of tweets and tokenization

"""

from textblob import TextBlob
import json
import datetime 

# read in data
data = []
files = ['bitcoin_tweet.json', 'bitcoin_tweet2.json', 'bitcoin_tweet3.json', 'bitcoin_tweet4.json']

for f in files:
    with open(f, 'r') as read_file:
        for line in read_file:
            data.append(json.loads(line))

combined_data = []

# convert tweet text to text blob and get sentiment
for tweet in data:

    tb = TextBlob(tweet['text'])
    
    # get timestamp
    ts = tweet["created_at"]
    ts = datetime.datetime.strptime(ts, '%a %b %d %H:%M:%S %z %Y')
    ts = datetime.datetime.strftime(ts, '%Y-%m-%d %H:%M:%S')  
    
    # note: sentiment is a Sentiment object in form:
    # Sentiment(polarity = -1 <= n <= 1, subjectivity = 0 <= n <= 1)
    sent = tb.sentiment

    data = {"timestamp": ts, "tweet" : tb, "sentiment" : sent }
    combined_data.append(data)


# should try different experiemnts for tokenization and n-grams. 
# n = 2 or 3
# tb.ngrams(n = 3)
# returns Wordlist object
