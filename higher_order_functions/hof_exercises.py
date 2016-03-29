import operator as op
from functools import reduce
import re
import math
import collections as col

# Uloha 1:
def square(iterable):
    return list(map(lambda x: x*x, iterable))


# Uloha 2:
def even(iterable):
    return list(filter(lambda x: x%2 == 0, iterable))


# Uloha 3:
def to_fahrenheit(iterable):
    return list(map(lambda x: (float(9)/5)*x + 32, iterable))


# Uloha 4:
def arthur_speaking(file_path):
    return list(filter(lambda x: x.strip().startswith("ARTHUR"), open(file_path)))


# Uloha 5:
def arthur_speaking_clear(file_path):
    # return list(map(lambda x: x.strip()[9:], arthur_speaking(file_path)))
    pattern = re.compile(r'[^:]+:\s+')
    return list(map(lambda x: pattern.sub('', x.strip()), arthur_speaking(file_path)))


# Uloha 6:
def line_count(file_path):
    return reduce(op.add, map(lambda x: 1, open(file_path)))


# Uloha 7:
def word_count(file_path):
    return list(map(lambda line: len(line.split()), open(file_path)))


# Uloha 8:
def total_words(file_path):
    return reduce(op.add, word_count(file_path))


# Uloha 9:
def my_max(iterable):
    return reduce(lambda x,y: x if x > y else y, iterable)


# Uloha 10:
def my_mean(iterable):
    return reduce(op.add, iterable) / len(iterable)


# Uloha 11:
def my_std(iterable):
    mean = my_mean(iterable)
    return math.sqrt(reduce(op.add, map(lambda x: (x-mean)**2, iterable)) / len(iterable))

# Uloha 12:
def flatten(iterable):
    return reduce(op.add, iterable)

# Uloha 13:
def histogram(file_path):
    words = filter(lambda x: len(x) > 0, flatten(map(lambda line: re.split('\W+', line.lower()), open(file_path))))
    return reduce(lambda result, x: result + col.Counter([x]), words, col.Counter())


# Uloha 14:


# Uloha 15:


# Uloha 16:


# Uloha 17:

