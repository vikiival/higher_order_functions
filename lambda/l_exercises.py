# Lambda funkcie
#
# Tato sekcia sluzi na precvicenie si lambda vyrazov
#

# Uloha 1:
def make_square():
    return(lambda x: x*x)


# Uloha 2:
def make_upper():
    return(lambda x: x.upper())


# Uloha 3:
def make_power():
    return(lambda x, N: x ** N)


# Uloha 4:
def make_power2(N):
    return(lambda x: x ** N)


# Uloha 5:
def call_name():
    return(lambda x, name: getattr(x, name)())