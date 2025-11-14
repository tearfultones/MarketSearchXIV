import requests
import pandas as pd

df = pd.read_csv("Items.csv")

ItemName = input("Enter item name: ")


ItemIdUnformatted = df[df["str"] == ItemName][["int32"]]
ItemId = ItemIdUnformatted.iloc[0, 0]



World = input("Enter world name: ")




Market = f"https://universalis.app/api/v2/{World}/{ItemId}"

response = requests.get(Market)

print(response.json())