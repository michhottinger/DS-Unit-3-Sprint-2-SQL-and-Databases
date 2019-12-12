def increment(x):
    return x + 1

def double(x):
    return x * 2

#how to define a function that takes an argument,
# runs it twice, and then returns an output
def run_twice(func, x):
    return func(func(x))

for i in range(10):
    print(i)

def rec_print(n):
    print(n)
    if n >= 1:
        rec_print(n-1)

def add(x,y):
    return x + y

def identity(x):
    return x

#in terminal
#help (map) in terminal shows more then q to quit
map(increment, [1, 2, 3, 4])
#what does map do here. Cast to a list
list(map(increment, [1, 2, 3, 4]))
#map applies func (increment) over the list
#map does filtering a sorting
#>>> from functools import reduce
# >>> from functools import reduce
# >>>  reduce(add, [1, 2, 3, 4])
#   File "<stdin>", line 1
#     reduce(add, [1, 2, 3, 4])
#     ^
# IndentationError: unexpected indent
# >>> reduce(add, [1, 2, 3, 4])
# 10
# >>> list(map(identity, [1, 2, 3, 4]))
# [1, 2, 3, 4]
# >>> list(map(increment, [1, 2, 3, 4]))
# [2, 3, 4, 5]
# >>> map_results = map(identity, [1, 2, 3, 4])
# >>> map_results
# <map object at 0x101b9fc50>
# >>> reduce(add, map_results)
# 10
# >>> map_results = map(increment, [1, 2, 3, 4])
# >>> reduce(add, map_results)
# 14
#ipecho.net gives local comp ip
#!curl ipecho.net/plain in colab
