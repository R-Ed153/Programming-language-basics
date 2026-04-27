import pandas as pd

scientists = pd.DataFrame(
    data={
        "Name": ["Rosaline Franklin", "William Gosset"],
        "Occupation": ["Chemist", "Statistician"],
        "Born": ["1920-07-25", "1876-06-13"],
        "Died": ["1958-04-16", "1937-10-16"],
        "Age": [37, 61],
    },
    index=["Chemist", "Statistician"],
    columns=["Name", "Age", "Born", "Died"],
)


print(scientists)
