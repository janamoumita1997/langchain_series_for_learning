import os, requests
from dotenv import load_dotenv

load_dotenv()

r = requests.get(
    "https://router.huggingface.co/v1/models",
    headers={"Authorization": f"Bearer {os.environ['HUGGINGFACEHUB_ACCESS_KEY']}"},
)
for m in r.json()["data"]:
    print(m["id"])