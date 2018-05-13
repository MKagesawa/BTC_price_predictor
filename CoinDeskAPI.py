import requests
import json
import sched, time

url = "https://api.coindesk.com/v1/bpi/currentprice.json"


s = sched.scheduler(time.time, time.sleep)
def collect_data(sc):
    req = requests.get(url)
    jsonRespond = req.json()
    print(jsonRespond)
    with open("./BPI9.json", "a+") as f:
        f.write(json.dumps(jsonRespond) + '\n')
    s.enter(60, 1, collect_data, (sc,))


s.enter(60, 1, collect_data, (s,))
s.run()
