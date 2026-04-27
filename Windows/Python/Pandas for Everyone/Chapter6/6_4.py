import pandas as pd

person = pd.read_csv("data/survey_person.csv")
site = pd.read_csv("data/survey_site.csv")
survey = pd.read_csv("data/survey_survey.csv")
visited = pd.read_csv("data/survey_visited.csv")

print(visited["site"].value_counts())

