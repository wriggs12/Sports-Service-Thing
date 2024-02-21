import pandas as pd
import numpy as np
import json

from utils import TEAM_IDS

from nba_api.stats.endpoints import BoxScoreSummaryV2
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import TeamGameLog
from nba_api.stats.static import teams

def get_recent_game(team_id):
    gameLogs = TeamGameLog(team_id)
    gameLog = gameLogs.get_dict()['resultSets'][0]
    
    game = {
        x: y for x, y in zip(gameLog['headers'], gameLog['rowSet'][0])
    }

    return game

def get_score(game_id):
    scoreData = BoxScoreSummaryV2(game_id)
    scoreData = scoreData.get_dict()['resultSets'][5]['rowSet']

    score = {
        scoreData[0][4]: scoreData[0][-1],
        scoreData[1][4]: scoreData[1][-1]
    }

    return score

if __name__ == "__main__":
    print(get_score(get_recent_game(TEAM_IDS['NYK'])['Game_ID']))
