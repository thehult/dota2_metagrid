import json

data = {}
with open('heroes.json') as f:
    data = json.load(f)

heroes = {}

for hero in data:
    heroes[hero['localized_name']] = hero