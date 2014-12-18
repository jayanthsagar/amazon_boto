import json
fp = open("i-b5f66354.json")
data = fp.read()
spec = json.loads(data)
print spec
print spec['Reservations'][0]
print foo