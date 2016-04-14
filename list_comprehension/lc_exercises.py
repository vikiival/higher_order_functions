# Praca so zoznamom
#
# Tato sekcia sluzi na precvicenie si pace so zoznamom
#

# Pristupovanie k prvkom zoznamu
# Uloha 1:
def first(list):
    return(list[0])


# Uloha 2:
def last(list):
    return(list[-1])


# Uloha 3:
def interval(list, a, b):
    return(list[a:(b+1)])


# Uloha 4:
def no_first_two(list):
    return list[2:]


# Uloha 5:
def no_last_three(list):
    return list[:-3]


# Uloha 6:
def every_second(list):
    return list[::2]

# List comprehension
# Uloha 7:

def square(list):
    return [x*x for x in list]


# Uloha 8:
def plus_one(list):
    return [x+1 for x in list]


# Uloha 9:
def evens(list):
    return [x for x in list if x % 2 == 0]


# Uloha 10:
def multiples(N):
    return [x for x in range(N) if x%3 == 0 and x%6 != 0]


# Uloha 11:
def first_chars(phrase):
    return [w[0] for w in phrase.split()]


# Uloha 12:
def unique_consonants(phrase):
    vowels = "aeiouy"
    punct = ".,?! '\""
    return set([c for c in phrase.lower() if c not in vowels and c not in punct])


# Uloha 13:
def replace_vowels(phrase):
    vowels = "aeiouy"
    return "".join([x if x.lower() not in vowels else '0' for x in phrase])


# Uloha 14:
def word_combinations(list1, list2):
    return [(x, y) for x in list1 for y in list2]


# Uloha 15:
def two_dices():
    return [(x, y) for x in range(1,7) for y in range(x,7)]


# Uloha 16:
def array(dim1, dim2, init=None):
    return [[init for _ in range(dim2)] for _ in range(dim1)]


# Uloha 17:
def combinations_of_two(list):
    return [[a,b] for a in list for b in list]


# Uloha 18:
def combinations_of_two_no_rep(list):
    return [[a,b] for a in list for b in list if a != b]


# Uloha 19:
def pytagoreans(N):
    return [[x, y, z] for x in range(1, N) for y in range(x, N) for z in range(y, N) if x*x + y*y == z*z]


