import json

with open('BPI1.json') as f:
    file = f.readlines()
st = file[0]
combined = []
# change time format to 'month, date, time' e.g. str'Apr 17 16:13:00'
print(json.loads(st)['time']['updated'][:6] + ' ' + json.loads(st)['time']['updated'][13:21])
before = 0

for line in file:
    pair = []
    pair.append(json.loads(line)['time']['updated'][:6] + ' ' + json.loads(line)['time']['updated'][13:21])
    now = float((json.loads(line)['bpi']['USD']['rate']).replace(',', ''))
    if now > before:
        pair.append(1)
    elif now < before:
        pair.append(0)
    else:
        pair.append(-1)
    pair.append(now)
    before = now
    combined.append(pair)

print(combined)

with open("./Tick1.json", "w") as f:
    f.write(str(combined))