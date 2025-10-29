import os
import requests

data_dir = "data/raw"
os.makedirs(data_dir, exist_ok=True)

urls = {
    "cyclones": "https://example.com/cyclones.csv",
    "antilles_shapefile": "https://example.com/antilles_shapefile.zip"
}

for name, url in urls.items():
    filename = os.path.join(data_dir, url.split("/")[-1])
    if not os.path.exists(filename):
        print(f"Téléchargement de {name}...")
        r = requests.get(url)
        with open(filename, "wb") as f:
            f.write(r.content)
    else:
        print(f"{name} déjà téléchargé.")
