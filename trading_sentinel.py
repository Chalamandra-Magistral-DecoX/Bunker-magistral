import requests, time

def get_price():
    # API pública de Binance para Bitcoin
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return float(data['price'])

last_price = get_price()
print("📈 SENTINEL DE TRADING INICIADO...")

while True:
    current_price = get_price()
    diff = ((current_price - last_price) / last_price) * 100
    
    if abs(diff) > 0.5: # Alerta si se mueve 0.5% en segundos
        status = "🚀 SUBIDA" if diff > 0 else "📉 CAÍDA"
        print(f"💰 ALERTA: {status} de {diff:.2f}% | Precio: {current_price}")
        # Guardar oportunidad en la Bóveda
    
    last_price = current_price
    time.sleep(10)
