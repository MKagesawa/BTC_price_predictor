from ast import literal_eval
import json
from pprint import pprint

with open('labeled_tweets.json') as t:
    tile = t.readlines()

#a = json.loads(tile[0])
print(tile[0])
print(len(tile[1]))
for tweet in tile:
    b = json.loads(tile[1])
    print(b['timestamp'])
print(len(tile[100]))

"""
a = tile[0].replace("'", "\"")[1:-1]
b = json.loads(json.dumps(a))
print(type(b))
import json
s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
json_acceptable_string = s.replace("'", "\"")
d = json.loads(json_acceptable_string)
# d = {u'muffin': u'lolz', u'foo': u'kitty'}
"""