text = input()
n = len(text)
index = 0

while index < n:
    print(text[index:index + 10])
    index += 10