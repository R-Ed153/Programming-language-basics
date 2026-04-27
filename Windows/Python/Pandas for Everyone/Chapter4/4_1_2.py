import pandas as pd

billboard = pd.read_csv("data/billboard.csv")

# print(billboard.iloc[0:5, 0:16])

billboard_long = billboard.melt(
    id_vars=["year", "artist", "track", "time", "date.entered"],
    var_name="week",
    value_name="rating"
)

print(billboard_long)