import pandas as pd

weather = pd.read_csv("data/weather.csv")
# print(weather.iloc[:5,:11])

weather_melt = weather.melt(
    id_vars=["id", "year", "month", "element"], var_name="day", value_name="temp"
)

# print(weather_melt)

weather_tidy = weather_melt.pivot_table(
    index=["id", "year", "month", "day"], columns="element", values="temp"
)

# print(weather_tidy)

weather_tidy_flat = weather_tidy.reset_index()
print(weather_tidy_flat)
