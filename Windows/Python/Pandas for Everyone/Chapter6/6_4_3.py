import pandas as pd

person = pd.read_csv("data/survey_person.csv")
site = pd.read_csv("data/survey_site.csv")
survey = pd.read_csv("data/survey_survey.csv")
visited = pd.read_csv("data/survey_visited.csv")

ps = person.merge(survey,left_on="ident",right_on='person')
vs = visited.merge(survey,left_on="ident",right_on="taken")

ps_vs = ps.merge(vs,left_on=["person"],right_on=["person"])
print(ps.head(5))
print(vs.head(5))
print(ps_vs.head(5))

assert ps_vs.shape[0] <= max(vs.shape[0],ps.shape[0]) 