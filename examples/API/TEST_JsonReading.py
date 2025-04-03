import json as js


content: str = ""
with open("data.json", "r", encoding="utf-8") as file:
    js.loads(file, content)
