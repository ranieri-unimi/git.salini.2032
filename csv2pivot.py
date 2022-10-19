# %%
import pandas as pd

# %%
df_team = pd.read_csv("datasets/matches.csv")
all_pkmn = df_team.pokemon.drop_duplicates().to_list()

# %%
clust = pd.read_csv("datasets/clusters.csv")
# all_clust = clust.cluster.drop_duplicates().to_list()
all_clust = {e["pokemon"]: e["cluster"] for _, e in clust.iterrows()}

# %%
for e in all_clust:
    df_team[e] = 0

for e in set(all_clust.values()):
    df_team[e] = 0

# %%
for i, row in df_team.iterrows():
    pkmn = row.pokemon
    df_team.loc[i, pkmn] = 1
    df_team.loc[i, all_clust[pkmn]] = 1

# %%
df_team = (
    df_team.groupby(
        [
            "id_match",
            "win",
        ]
    )
    .agg(sum)
    .reset_index()
)

# %%
for e in set(all_clust.values()):
    df_team[e + "_pw2"] = df_team[e] ** 2

# %%
df_team.to_csv("datasets/pivot.group.matches.csv", index=False)

# %%
