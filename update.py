import requests
import json

def update_price():
    params = {
        "app_id": 730,
        "currency": "USD"
    }
    r = requests.get("https://api.skinport.com/v1/sales/history", params = params).text
    parsed =json.loads(r)
    r = json.dumps(parsed, indent=4)

    with open("skinport_prices.json", "w", encoding="utf-8") as f:
        f.write(r)

    with open("skinport_prices.json", "r",encoding="utf-8") as f:
        x = f.read()
        y = json.loads(x)
        t = len(y)

    open("weapons.txt","w",encoding="utf-8").close()
    with open("weapons.txt", "a", encoding="utf-8") as f:   
        for x in range(t):
            f.write(y[x]["market_hash_name"] + "\n")
    print("Update successful!")