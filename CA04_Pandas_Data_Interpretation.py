# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 07:43:06 2020

I used an exercise from this website as the basis of the exercise
https://realpython.com/pandas-python-explore-dataset/


@author: ciara
"""
import requests
import pandas as pd
import numpy as np

download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"

response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")


nba = pd.read_csv("nba_all_elo.csv")
type(nba)


## get the length of the data
len(nba)

## get the shape of the dataframe
nba.shape

##info on the data
nba.info()


## basic descriptive stats

nba.describe(include=np.object)


##explore the data and different values than in the online page I'm following
nba["game_id"].value_counts()
## there were 63157 games

current_decade = nba[nba["year_id"] > 2010]
current_decade.shape




nba[
...     (nba["_iscopy"] == 0) & ## exclude duplicates
...     (nba["pts"] > 100) & ## home team over 100 points
...     (nba["opp_pts"] > 100) & ## away team over 100 points
...     (nba["team_id"] == "LAL") ## team is the Lakers
... ]


## grouping by multiple columns
>>> nba[
...     (nba["fran_id"] == "Lakers") & ##tema is lakers
...     (nba["year_id"] > 2000) ##year greater than 2000
... ].groupby(["year_id", "game_result"])["game_id"].count()  ## grouping by year, result and count on game id


##plot the number of games played per team
nba["fran_id"].value_counts().head(10).plot(kind="bar")
## the plot is not appearing on my screen but I can't figure out what I need ot do in spyder for it to show





