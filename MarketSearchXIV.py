import argparse
import requests
import pandas as pd

parser = argparse.ArgumentParser(description="MarketSearchXIV")
parser.add_argument("world", help="World Name or Data Center")
parser.add_argument("item_name", nargs="+", help="Item Name")

args = parser.parse_args()

ItemName = " ".join(args.item_name)

df = pd.read_csv("Items.csv")

filtered = df[df["str"].str.lower() == ItemName.lower()]

ItemId = int(filtered.iloc[0]["int32"])

url = f"https://universalis.app/api/v2/{args.world}/{ItemId}"
ItemResponse = requests.get(url)
ItemOutput = ItemResponse.json()

print("")
print("-" * 30)




for i in reversed(ItemOutput["listings"]):
    print("")
    print(f"Price: {i['pricePerUnit']}")
    print(f"Quantity: {i['quantity']}")
    print(f"Total: {i['total']}")
    print(f"Retainer: {i['retainerName']}")
    
    world_name = i.get('worldName')
    if world_name is not None:
        print("")
        print(f"World: {world_name}")
    else:
        pass

    print("")
    print("-" * 30)