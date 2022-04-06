import api
from credentials import access_key, private_key

def zebitex_price(market="btceur"):
    client = api.Zebitex(access_key, private_key, False)
    response = client.public_trade_history(market).json()
    return float(response[0]["price"])
