# %%
import pandas as pd

# %%
df = pd.read_csv("datasets/matches.csv")
all_pkmn = df.pokemon.drop_duplicates().to_list()

# %%
clust = pd.read_csv("datasets/clusters.csv")
# all_clust = clust.cluster.drop_duplicates().to_list()
all_clust = {e["pokemon"]: e["cluster"] for _, e in clust.iterrows()}

# %%
for e in all_clust:
    df[e] = 0

for e in set(all_clust.values()):
    df[e] = 0

# %%
for i, row in df.iterrows():
    pkmn = row.pokemon
    df.loc[i, pkmn] = 1
    df.loc[i, all_clust[pkmn]] = 1

# %%
df = (
    df.groupby(
        [
            "id_match",
            "win",
        ]
    )
    .agg(sum)
    .reset_index()
)

# # %%
# for e in set(all_clust.values()):
#     df[e + "_pw2"] = df[e] ** 2

# %%
df.to_csv("datasets/pivot.group.matches.csv", index=False)

# %%
