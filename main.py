import requests
import pandas as pd



DataCenter = "https://universalis.app/api/v2/data-centers"
DataCenterResponce = requests.get(DataCenter)
DataCenterOutput = DataCenterResponce.json()

print("")

for m in DataCenterOutput:

    print(f"Data Center: {m['name']}")

print("")

ChosenDataCenter = input("Enter Data Center name: ")

print("")


OutputWorlds = []

for g in DataCenterOutput:
    if ChosenDataCenter == g['name']:
        OutputWorlds = g['worlds']






WorldsApi = "https://universalis.app/api/v2/worlds"
WorldsResponse = requests.get(WorldsApi)
WorldsOutput = WorldsResponse.json()


WorldNames = [w['name'] for w in WorldsOutput if w['id'] in OutputWorlds]

for worldname in WorldNames:
    print(worldname)
print("")


# df = pd.read_csv("Items.csv")

# ItemName = input("Enter item name: ")


# ItemIdUnformatted = df[df["str"] == ItemName][["int32"]]
# ItemId = ItemIdUnformatted.iloc[0, 0]



World = input("Enter world name: ")

print("")

ItemName = input("Enter item name: ")


df = pd.read_csv("Items.csv")

ItemIdUnformatted = df[df["str"] == ItemName][["int32"]]
ItemId = ItemIdUnformatted.iloc[0, 0]


Market = f"https://universalis.app/api/v2/{World}/{ItemId}"

response = requests.get(Market)

# print(response.json())

Output = response.json()

print("")
print("-" * 30)

for i in Output["listings"]:
    print("")
    print(f"Price: {i['pricePerUnit']}")
    print(f"Quantity: {i['quantity']}")
    print(f"Total: {i['total']}")
    print(f"Retainer: {i['retainerName']}")
    print("")
    print("-" * 30)