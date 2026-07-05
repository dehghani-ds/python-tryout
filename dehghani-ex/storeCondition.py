b = int(input())
off = 0
if b > 50_000:
    off = 0.2
elif 20_000 > b > 50_000:
    off = 0.1

print(int(b * (1 - off)))
