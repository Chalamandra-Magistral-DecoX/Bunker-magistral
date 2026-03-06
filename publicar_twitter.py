#!/usr/bin/env python3
import tweepy
import os
import random
from dotenv import load_dotenv

load_dotenv(os.path.expanduser('~/microcosmos_elite/.env'))

auth = tweepy.OAuth1UserHandler(
    os.getenv('TWITTER_API_KEY'),
    os.getenv('TWITTER_API_SECRET'),
    os.getenv('TWITTER_ACCESS_TOKEN'),
    os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
)
api = tweepy.API(auth)

textos = [
    "🦎 Convertí un Celeron de $100 en un búnker de ingresos. Código y manual aquí: https://ko-fi.com/s/4b5cae46ca",
    "Automatiza pagos, caza dominios premium y genera ingresos pasivos con mi búnker digital. https://ko-fi.com/s/4b5cae46ca",
    "¿Una Chromebook vieja? Puede ser tu servidor de ingresos. Te enseño cómo. https://ko-fi.com/s/4b5cae46ca",
]

texto = random.choice(textos)
api.update_status(texto)
print(f"Publicado: {texto}")
