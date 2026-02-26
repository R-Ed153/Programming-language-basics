import pandas as pd

person = pd.read_csv("data/survey_person.csv")
site = pd.read_csv("data/survey_site.csv")
survey = pd.read_csv("data/survey_survey.csv")
visited = pd.read_csv("data/survey_visited.csv")

visited_subset = visited.loc[[0,2,6],:]
print(visited)
print(site)

o2o_merge = site.merge(visited_subset,left_on="name",right_on="site")
#print(o2o_merge)
m2o_merge = site.merge(visited,left_on="name",right_on="site")
print(m2o_merge)

assert m2o_merge.shape[0] <= max(visited.shape[0],site.shape[0]) 