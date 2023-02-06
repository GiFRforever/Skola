import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/Thermal_expansion"
html = requests.get(url).content
df_list = pd.read_html(html)  # type: ignore
for i, df in enumerate(df_list):
    print(df)
    df.to_csv(f"my data {i}.csv")
