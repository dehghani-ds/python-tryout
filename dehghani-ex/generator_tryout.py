def trying_yield():
    yield 1
    yield 2
    yield 3


g = trying_yield()
print(next(g))
print(next(g))

for i in g:
    print(f"generator val = [{i}]")
