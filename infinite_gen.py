def infinite_integers():
    i = 1
    while True:
        yield i
        i += 1

def infinite_squares():
    for i in infinite_integers():
        yield i**2

def select(iterable, n):
    result = []
    it = iter(iterable)
    for i in range(n):
        result.append(next(it))
    return result

def pythagorean_triples():
    for c in infinite_integers():
        for b in range(1, c):
            for a in range(1, b):
                if a**2 + b**2 == c**2:
                    yield (a, b, c)

squares = select(infinite_squares(), 15)
print(squares)

triples = select(pythagorean_triples(), 15)
print(triples)
