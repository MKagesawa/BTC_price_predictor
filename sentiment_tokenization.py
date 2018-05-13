"""
Code for sentiment analysis of tweets and tokenization
"""

from textblob import TextBlob
import textblob
import json
import datetime

# read in data
data = []
files = ['bitcoin_tweet.json', 'bitcoin_tweet2.json', 'bitcoin_tweet3.json', \
         'bitcoin_tweet4.json', 'bitcoin_tweet5.json', 'bitcoin_tweet6.json']

for f in files:
    with open(f, 'r') as read_file:
        for line in read_file:
            data.append(json.loads(line))


with open('BPI9.json') as f:
    file = f.readlines()
processed_time = []
# change time format to 'month, date, time' e.g. str'Apr 17 16:13:00'
before = 0
# process BPI and add -1:lower price 0:others 1:higher price

for line in file:
    pair = []
    tm = json.loads(line)['time']['updated'][:21].replace(',', '')
    try:
        tm = datetime.datetime.strptime(tm, '%b %d %Y %H:%M:%S')
        tm = datetime.datetime.strftime(tm, '%Y-%m-%d %H:%M')
    except ValueError:
        continue
    pair.append(tm)

    now = float((json.loads(line)['bpi']['USD']['rate']).replace(',', ''))
    if now > before:
        pair.append(1)
    elif now < before:
        pair.append(-1)
    else:
        pair.append(0)
    pair.append(now)
    before = now
    processed_time.append(pair)


# convert tweet text to text blob and get sentiment
processed_tweet = []
count = 0

# initialize bpi and tweet counter
ti = 0
tw = 0

not_stop = True
ti_len = len(processed_time)
tw_len = len(processed_tweet)-1
print('number of bpi', ti_len)
for tweet in data:
    try:
        tb = TextBlob(tweet['text'])
        tt = tweet['text']
    except KeyError:
        continue
    # get timestamp
    ts = tweet["created_at"]
    ts_strp = datetime.datetime.strptime(ts, '%a %b %d %H:%M:%S %z %Y')
    ts_strf = datetime.datetime.strftime(ts_strp, '%Y-%m-%d %H:%M')

    # tweet label 0: error(do not use data), -1: price decrease, 1: price increase
    label = 0
    for i in range(ti_len-1):
        # get BPI timestamp
        tm_p = processed_time[i][0]
        tm = datetime.datetime.strptime(tm_p, '%Y-%m-%d %H:%M')
        ts_strp2 = datetime.datetime.strptime(ts_strf, '%Y-%m-%d %H:%M')
        if ts_strp2 == tm:
            label = processed_time[i][1]
            break
    # note: sentiment is a Sentiment object in form:
    # Sentiment(polarity = -1 <= n <= 1, subjectivity = 0 <= n <= 1)
    sent = tb.sentiment
    data = {'timestamp': ts_strf, 'tweet': tt, 'sentiment': sent, 'label': label}
    processed_tweet.append(data)
    count += 1
    with open("./labeled_tweets.json", "a+") as f:
        f.write(json.dumps(data) + '\n')

f.close()
print('count', count)

# should try different experiemnts for tokenization and n-grams. 
# n = 2 or 3
# tb.ngrams(n = 3)
# returns Wordlist object



