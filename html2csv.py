# %%
import pandas as pd
from bs4 import BeautifulSoup

# %%
with open("datasets/matches.table.list.html", "rt", encoding="utf8") as f:
    raw_df = f.read()

# %%
table_list = BeautifulSoup(raw_df).find_all('table')
df = pd.DataFrame()

# %%
for i, m in enumerate(table_list):
    players = m.find_all('div', {"class":'sc-70a0e279-0 jEPysh'})
    res = [e.contents[0].split(" - ") for e in m.find_all('p') if len(e.contents) == 1 and (e.contents[0].startswith('Victory') or e.contents[0].startswith('Defeat'))]
    match = list()

    for j, p in enumerate(players):
        dt = p.find('tr').findChildren(recursive=False)

        hits = dt[5].find('p').contents[0].split('|')
        damages = dt[6].find_all("div", {"class":"sc-70a0e279-6 iPEWOE"})
        abilities = dt[7].find_all('img')


        dt_dict = {
            'pokemon' : dt[0].find('img')['src'].split('_')[-1].split('.')[0],
            'item' : dt[1].find('img')['src'].split('_')[-1].split('.')[0],
            'level' : dt[2].contents[0],
            'user' : dt[3].find('a')['href'].split('/')[-1],
            'score' : dt[4].find('p').contents[0],
            'kill' : hits[0].strip(),
            'assist' : hits[1].strip(),
            'interrupt' : hits[2].strip(),
            'damage_done' : damages[0].contents[0],
            'damage_taken' : damages[1].contents[0],
            'damage_healed' : damages[2].contents[0],
            'ability1' : abilities[0]['src'].split('kill_')[-1].split('.')[0],
            'ability2' : abilities[1]['src'].split('kill_')[-1].split('.')[0], 
            # 'team' : j//5,
            'tot_score' : res[j//5][-1],
            'win' : 1 if res[j//5][0] == 'Victory' else 0,
        }
        match.append(dt_dict)

    dfi = pd.DataFrame(match)
    dfi['id_match'] = i
    df = pd.concat([df, dfi], ignore_index=True)


# %%
df.to_csv('datasets/matches.csv', index=False)

# %%
