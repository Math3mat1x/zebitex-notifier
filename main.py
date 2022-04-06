import api
import json
from credentials import access_key, private_key
from message import send

def zebitex_price(market="btceur"):
    client = api.Zebitex(access_key, private_key, False)
    response = client.public_trade_history(market).json()
    return float(response[0]["price"])

with open("data.json", "r") as f:
    data = json.loads(f.read())

markets = list(data.keys())
for market in markets:
    high = data[market][0]
    low  = data[market][1]
    done = data[market][2]
    
    if not done:
        price = zebitex_price(market)
        if price >= high:
            send("Price of {} is high!".format(market))
            done = True
        elif price <= low:
            send("Price of {} is low!".format(market))
            done = True
    
    if done:
        data[market] = [high, low, done]
    
        with open("data.json", "w") as f:
            f.write(json.dumps(data))
