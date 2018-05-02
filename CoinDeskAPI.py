import requests
import json
import sched, time

url = "https://api.coindesk.com/v1/bpi/currentprice.json"


s = sched.scheduler(time.time, time.sleep)
def collect_data(sc):
    req = requests.get(url)
    jsonRespond = req.json()
    print(jsonRespond)
    with open("./BPI5.json", "a+") as f:
        f.write(json.dumps(jsonRespond) + '\n')
    s.enter(60, 1, collect_data, (sc,))


s.enter(60, 1, collect_data, (s,))
s.run()

"""
with open('BPI1.json') as f:
    file = f.readlines()

print(json.loads(file[1])['time'])
"""