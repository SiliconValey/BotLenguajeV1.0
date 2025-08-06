import os
import requests
from dotenv import load_dotenv
from collections import Counter
from database import guardar_lenguajes

# Cargar variables desde security.env
load_dotenv(dotenv_path="security.env")

def obtener_lenguajes_top():
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"} if token else {}

    url = "https://api.github.com/search/repositories?q=stars:%3E10000&sort=stars&order=desc&per_page=50"
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    repos = data.get("items", [])
    lenguajes = [repo["language"] for repo in repos if repo["language"]]

    conteo = Counter(lenguajes)
    top = conteo.most_common()

    guardar_lenguajes(top)

    return top
