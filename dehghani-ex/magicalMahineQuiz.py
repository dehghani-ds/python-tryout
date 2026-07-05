a = int(input())

while a != 1:
    if a % 2 == 0:
        a /= 2
    else:
        a = a * 3 + 1
    print(int(a))
