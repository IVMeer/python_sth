# map(function, iterable, *iterables)
"""
iterable→iterator
"""
def square(x):
    return x ** 2

numbers = [1, 2, 3]

squared_numbers = map(square, numbers)
print(squared_numbers)
print(list(squared_numbers))

# lambda()