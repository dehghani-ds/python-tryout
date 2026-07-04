ff = open('ex01.py')
print(
    ff.readlines()
)
ff.close()

with open('ex01.py') as f:
    print(f.readlines())

open('ex01.py', 'a').write(
    '# this is a comment\n'
)
