ff = open('ex01.py')
print(
    ff.readlines()
)
ff.close()

with open('ex01.py') as f:
    print(f.readlines())