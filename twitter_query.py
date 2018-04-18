import tweepy
import requests
import json
import pickle
from textblob import TextBlob
from searchtweets import ResultStream, gen_rule_payload, load_credentials, collect_results

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

app = tweepy.AppAuthHandler(consumer_key, consumer_secret)
myBearer = "Bearer " + app.openBearer
api = tweepy.API(auth)
"""
public_tweets = api.search('bitcoin')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
"""
#curl -X POST "https://api.twitter.com/1.1/tweets/search/30days/dev.json" -d '{"query":"bitcoin "search api"","maxResults":"100","fromDate":"<201804160000>","toDate":"<201804170000>"}' -H "Authorization: Bearer"


url = "https://api.twitter.com/1.1/search/tweets.json?q=bitcoin&result_type=popular"
data_input = '{"query":"bitcoin "search api"","maxResults":"100","fromDate":"<201601010000>","toDate":"<201804160000>"}'
next_token = ''
req = requests.post(url, data=data_input, headers={"Authorization": myBearer})
jsonRespond = print(req)
with open("./1.json", "w") as f:
    f.write(json.dumps(jsonRespond, indent=4))


# Alternative: Python Client Search Tweets API
"""
premium_search_args = load_credentials("twitter_keys.yaml",
                                       yaml_key="search_tweets_premium",
                                       env_overwrite=False)

rule = gen_rule_payload("bitcoin", results_per_call=100) # testing with a sandbox account
tweets = collect_results(rule,
                         max_results=100,
                         result_stream_args=premium_search_args)

[print(tweet, end='\n\n') for tweet in tweets]

with open("./1.pkl", "a") as f:
    for tweet in tweets:
        f.write(pickle.dumps(tweet))
"""