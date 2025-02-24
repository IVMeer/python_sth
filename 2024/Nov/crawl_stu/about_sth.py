# map(function, iterable, *iterables)
"""
iterable→iterator
"""
def square(x):
    return x ** 2

numbers = [1, 2, 3]

squared_numbers = map(square, numbers)
# 会返回一个迭代器对象（iterator object）
print(squared_numbers)
print(list(squared_numbers))

# lambda()