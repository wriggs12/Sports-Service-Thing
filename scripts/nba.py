import pandas as pd
import requests
import numpy as np

from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.static import teams

SEASON_YEAR = 2023
NBA_SCH_URL = f"https://data.nba.com/data/10s/v2015/json/mobile_teams/nba/{SEASON_YEAR}/league/00_full_schedule.json"

def get_schedule(team):
    global NBA_SCH_URL

    games = []

    schedule = requests.get(NBA_SCH_URL).json()['lscd']
    for month in schedule:
        month_games = month['mscd']['g']
        for game in month_games:
            home_team = game['h']['ta']
            away_team = game['v']['ta']
            if home_team == team or away_team == team:
                games.append(game['gdte'])

    games.sort()

    return games

def get_games():
    gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=teams.find_team_by_abbreviation('nyk')['id'])
    games = gamefinder.get_data_frames()[0]
    print(games.iloc[0])
    # games = teamgamelog.TeamGameLog(team_id=teams.find_team_by_abbreviation('nyk')['id'])
    # games.get_request()
    # print(games.get_json())

if __name__ == "__main__":
    # get_games()
    games = get_schedule('NYK')
    print(games)