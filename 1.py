def simple_gen():
    yield 10
    yield 20
    yield 30

gen = simple_gen()
print(next(gen))

#10