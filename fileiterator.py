file = open("sample.txt")

for line in file:
    print(line.strip())

file.close()