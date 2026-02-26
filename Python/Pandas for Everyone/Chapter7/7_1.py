import pandas as  pd

billboard = pd.read_csv("data/billboard.csv")
billboard_long = billboard.melt(id_vars=["year","artist","track","time","date.entered"],
                                var_name="week",
                                value_name="rating")

#print(billboard_long.loc[billboard_long["track"] == "Loser"])

bill_board_songs = billboard_long[["year","artist","track","time"]]
print(bill_board_songs.shape)
bill_board_songs = bill_board_songs.drop_duplicates()
print(bill_board_songs.shape)
