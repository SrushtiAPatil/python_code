with open("data.txt", "r") as f:
    text = f.read()

words = len(text.split())
lines = text.count("\n") + 1
chars = len(text)

print("Words:", words)
print("Lines:", lines)
print("Characters:", chars)
