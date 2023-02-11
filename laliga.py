import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

laliga_url="https://fbref.com/en/comps/12/La-Liga-Stats"
years=list(range(2022,2019,-1))
laliga_data=[]
years

for year in years:
    data =requests.get(laliga_url)
    soup=BeautifulSoup(data.text)

    previous_seazon = soup.select('a.prev')[0].get("href")
    laliga_url=f"https://fbref.com{previous_seazon}"

    standings_tab =soup.select('table.stats_table')[0]
    links=standings_tab.find_all('a')
    links= [l.get("href") for l in links]
    links=[l for l in links if "/squads/"in l]
    teams_url=[f"https://fbref.com{l}" for l in links]

    for team_url in teams_url:
        team_name = team_url.split("/")[-1].replace("-Stats", "").replace("-", " ")
        data=requests.get(team_url)
        matches_results = pd.read_html(data.text, match="Scores & Fixtures")[0]
        soup=BeautifulSoup(data.text)
        shooting=soup.find_all('a')
        shooting= [l.get("href") for l in shooting]
        shooting= [l for l in shooting if l and 'all_comps/shooting' in l]
        data = requests.get(f"https://fbref.com{shooting[0]}")
        shooting_stats=pd.read_html(data.text,match="Shooting")[0]
        shooting_stats.columns=shooting_stats.columns.droplevel()
        try:
            team_stats= matches_results.merge(shooting_stats[["Date","Sh","SoT","Dist", "FK", "PK", "PKatt","xG", "npxG", "npxG/Sh", "G-xG","np:G-xG"]], on="Date")
        except ValueError:
          continue
        team_stats = team_stats[team_stats["Comp"] == "La Liga"]
        team_stats["Season"] = year
        team_stats["Team"] = team_name
        laliga_data.append(team_stats)
        time.sleep(1)

len(laliga_data)

laliga_df = pd.concat(laliga_data)


laliga_df.to_csv("laliga.csv")