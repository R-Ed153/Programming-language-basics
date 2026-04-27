import pandas as pd
from datetime import datetime

scientists = pd.read_csv("data/scientists.csv")
firstHalf = scientists[:4]
secondHalf = scientists[4:]

#print(firstHalf)
#randomAge = scientists["Age"].sample(frac=1,random_state=45).values
#scientists["Age"] = randomAge
scientists["died_dt"],scientists["born_dt"] = (pd.to_datetime(scientists["Died"],format='%Y-%m-%d'),pd.to_datetime(scientists["Born"],format='%Y-%m-%d'))
scientists['age_days'] = (scientists["died_dt"]-scientists["born_dt"])

scientists = scientists.assign(
   age_days_assign=scientists['died_dt'] - scientists['born_dt'],
   age_years_assign = lambda df_:df_["age_days"].astype("timedelta64[Y]")
)
print(scientists)