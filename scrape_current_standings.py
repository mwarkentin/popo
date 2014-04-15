#!/usr/bin/env python

import json
from pprint import pprint

import requests


def retinafy(image):
    parts = image.split('.')
    parts[-2] += '@2x'
    return ".".join(parts)


if __name__ == "__main__":
    r = requests.get('http://api.thescore.com/nhl/standings')
    standings = r.json()

    teams = []

    for team in standings:
        name = team['team']['abbreviation']
        logo_tiny = team['team']['logos']['tiny']
        conference = team['team']['conference']
        points = team['points']
        games_remaining = 82 - team['games_played']
        potential_points = points + (games_remaining * 2)

        team_dict = {
            'name': name,
            'points': points,
            'potential_points': potential_points,
            'logo_tiny': retinafy(logo_tiny),
            'conference': conference,
        }

        teams.append(team_dict)

    pprint(teams)

    json_dict = {
        'teams': teams,
    }

    with open('data.json', 'wb') as fp:
        json.dump(json_dict, fp, indent=2)
