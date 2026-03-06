import requests

def check_profit_margin():
    # Compara el costo de procesamiento en servidor A vs lo que paga el cliente B
    cost_api_a = 0.01  # Lo que te cuesta a ti
    price_client_b = 0.05 # Lo que cobras por tu túnel optimizado
    
    margin = price_client_b - cost_api_a
    print(f"📈 Margen de Arbitraje detectado: ${margin} por transacción")
    return margin

if __name__ == "__main__":
    check_profit_margin()
