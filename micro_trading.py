import requests
import time

def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    return float(requests.get(url).json()['price'])

price_history = [get_btc_price()]

while True:
    current = get_btc_price()
    change = ((current - price_history[-1]) / price_history[-1]) * 100
    
    if abs(change) > 1.0: # Movimiento brusco del 1%
        print(f"⚠️ ALERTA ROJA: Movimiento de {change:.2f}% | Precio: {current}")
        # Aquí se dispararía la orden de compra si conectas tu API Key
    
    price_history.append(current)
    if len(price_history) > 10: price_history.pop(0)
    time.sleep(30)
