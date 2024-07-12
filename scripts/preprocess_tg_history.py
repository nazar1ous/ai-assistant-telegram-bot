import json

with open("data/tg_history.json", "r") as f:
    data = json.load(f)

messages = data["messages"]

texts = []
authors = []
for message in messages:
    text = message.get("text")
    author = message.get("from")
    if author == "......":
        author = "AI"
    else:
        author = "Human"
    if text:
        texts.append(text)
        authors.append(author)

with open("data/tg_history.txt", "w") as f:
    for text, author in zip(texts, authors):
        f.write(f"{author}: {text}\n")