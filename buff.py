import requests
import time
import json

URL = "https://buff.163.com/api/market/goods"
def get_buff_price(line,cookies):
        params = {"game" : "csgo","page_num" : "1","search" : str(line)}
        x = requests.get(URL, params=params, cookies=cookies)
        x = check_response(x,params,cookies)
        if(x != None):
            x0 = x["data"]["items"][0]["sell_min_price"]
        else:
            x0 = 0
        return x0

def check_response(x,params,cookies):
    if x == None or x.status_code != 200:
        while(x.status_code != 200 and x != None):
            print("Sleep 10s" + "| Error Code " + str(x.status_code))
            try:
                print(x0 = x["data"]["items"][0]["sell_min_price"])
            except:
                print("no price found")
            time.sleep(10)
            x = requests.get(URL, params=params, cookies=cookies)
    else:
        return x.json()