import json

def get_skinport_price(item):
    with open("skinport_prices.json","r",encoding="utf-8") as f:
        content = f.read()
        json_content = json.loads(content)

        for count in range(len(json_content)):
            if(json_content[count]["market_hash_name"] == str(item).strip()):
                x1 = json_content[count]["last_90_days"]["max"]
                if x1 == None:
                    x1 = 0
    return x1