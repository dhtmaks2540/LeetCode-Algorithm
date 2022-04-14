import sys

while True:
    try:
        text = sys.stdin.readline().strip()
        if(text == ""):
            break
        print(text)
    except EOFError:
        exit()