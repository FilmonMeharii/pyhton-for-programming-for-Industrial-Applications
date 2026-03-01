

import requests

URL = "http://localhost:11434/api/generate"
MODEL = "llama3:8b"

prompt = "Hi reply with only 'Hello World'"

r = requests.post(
    URL,
    json={"model": MODEL, "prompt": prompt, "stream": False},
    timeout=120,
)
r.raise_for_status()

data = r.json()
print(data["response"])