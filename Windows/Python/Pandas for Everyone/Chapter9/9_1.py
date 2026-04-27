import pandas as pd

visitedFile = "data/survey_visited.csv"

print(pd.read_csv(visitedFile,na_filter=False))
print(pd.read_csv(visitedFile,keep_default_na=False))
print(pd.read_csv(visitedFile,na_values=[""],keep_default_na=False))