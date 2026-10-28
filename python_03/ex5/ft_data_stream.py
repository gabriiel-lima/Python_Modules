def gen():
    yield 1
    yield 2

fun = gen()

print(next(fun))
print(next(fun))
print(next(fun))