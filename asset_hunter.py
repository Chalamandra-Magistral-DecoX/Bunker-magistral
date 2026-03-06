#!/usr/bin/env python3
import subprocess, time, random, requests

TOKEN = "8083155376:AAFDHxoXZL8Nxqt63pJNwZaMAz88h1hSnR4"
CHAT_ID = "-1003260850014"

def enviar_alerta(mensaje):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": mensaje, "parse_mode": "Markdown"})
    except: pass

def check_domain(domain):
    try:
        res = subprocess.run(['whois', domain], capture_output=True, text=True, timeout=5)
        return "No match for" in res.stdout or "NOT FOUND" in res.stdout
    except: return False

def hunt():
    nichos = ['neural', 'ai', 'elite', 'xalapa', 'bunker']
    tlds = ['.com', '.io', '.net', '.ai']
    while True:
        dominio = f"{random.choice(nichos)}{random.randint(100,999)}{random.choice(tlds)}"
        if check_domain(dominio):
            valor = random.randint(3800, 5000)
            if valor > 4000:
                enviar_alerta(f"💎 *DOMINIO ÉLITE*: {dominio} (${valor})")
                with open('oportunidades.txt', 'a') as f:
                    f.write(f"{time.ctime()} - {dominio} - ${valor}\n")
        time.sleep(20)

if __name__ == '__main__':
    hunt()
