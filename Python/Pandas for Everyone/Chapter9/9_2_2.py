import pandas as pd

visited = pd.read_csv("data/survey_visited.csv")
survey = pd.read_csv("data/survey_survey.csv")

print(visited)
print(survey)

print(visited.merge(survey,left_on="ident",right_on="taken"))