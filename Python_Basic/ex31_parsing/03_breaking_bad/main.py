import requests
import json

req = requests.get('https://breakingbadapi.com/api/deaths')

data = json.loads(req.text)

with open('BreakingBad.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('BreakingBad.json', 'r') as file:
    max_death, season, episode = 0, 0, 0
    for i_unit in data:
        if i_unit.get('number_of_deaths') > max_death:
            max_death = i_unit.get('number_of_deaths')
            season = i_unit.get('season')
            episode = i_unit.get('episode')
    print(f'Maximum numbers of death ({max_death}) you can find in season: {season}, episode: {episode}.')
