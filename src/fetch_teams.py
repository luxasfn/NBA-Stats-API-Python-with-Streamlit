
import requests
import pandas as pd
import os

def fetch_teams(api_key, max_pages=1, season=None):
    url = "https://api.balldontlie.io/v1/teams"
    headers = {"Authorization": f"Bearer {api_key}" }
    all_data = []

    print(f"Coletando dados de times...")

    for page in range(1, max_pages + 1):
        params = {}
        params["page"] = page
        response = requests.get(url, headers=headers, params=params)
        print(f"Página {page} - Status: {response.status_code}")

        if response.status_code != 200:
            print("Erro na requisição:", response.text)
            break

        data = response.json()
        all_data.extend(data.get("data", []))

    if not os.path.exists("data"):
        os.makedirs("data")

    df = pd.DataFrame(all_data)
    df.to_csv(f"data/teams.csv", index=False)
    print(f"Dados salvos: {len(df)} registros em data/teams.csv")

if __name__ == "__main__":
    fetch_teams("ecb89db5-66cf-4054-8fc8-f4417218dd57")
