
# Nemenne objekty a funkcie vyssej urovne

# Nemenné (Immutable) objekty
----------------------------------------------------

# Nemenný objekt sa po vytvorení už nemôže meniť


```python
x = 'foo'
print(id(x))
print(id(x.upper()))
print(id(x + 'bar'))
```

    140614760027952
    140614618464584
    140614618464472


# Neznamena to, ze referencia na objekt sa nemoze menit
v cisto funkcionalnom jazyku by sa nemalo diat ani to


```python
x = 'foo'
y = x
print(x, id(x))
x = 'bar' 
print(x, id(x))# objekt foo sa nezmenil, to len x uz smeruje na iny objekt
print(y, id(y))
```

    foo 140614760027952
    bar 140614760028344
    foo 140614760027952


# Nie je to to iste ako klucove slovo *final* v Jave

Final premenna po vytvoreni nemoze smerovat na iny objekt

Objekt samtny ale moze byt zmeneny


```python
# -- JAVA --
final List<Integer> list = new ArrayList<Integer>();
list = new ArrayList<Integer>(); // toto sa neskompiluje
```


```python
# -- JAVA --
final List<Integer> list = new ArrayList<Integer>();
list.add(1); //toto prejde bez problemov
```


```python
# -- JAVA --
final List<Integer> list = Collections.unmodifiableList(new ArrayList<Integer>(...)); //toto je immutable list
```

# Imutable znamena, ze hociaka operacia nad objektom vytvori novy objekt


```python
x = 'foo'
y = x
print(x) # foo
y += 'bar'
print(x) # foo
print(y)
```

    foo
    foo
    foobar



```python
x = [1, 2, 3]
y = x
print(x)
y += [3, 2, 1]
print(x)
```

    [1, 2, 3]
    [1, 2, 3, 3, 2, 1]


# Pozor, v Pythone sa parametre funkcie predavaju referenciou
Pri mutable objektoch to moze sposobit necakane veci ak neviete, co sa vo funkcii deje


```python
def func(val):
    val += 'bar'

x = 'foo'
print(x)
func(x)
print(x)
```

    foo
    foo



```python
def func(val):
    val += [3, 2, 1]

x = [1, 2, 3]
print(x)
func(x)
print(x)
```

    [1, 2, 3]
    [1, 2, 3, 3, 2, 1]


# Ak predate immutable objekt funkcii, tak vam ho funkcia urcite nezmeni

# String je imutable
Podobne ako vsetky zakladne typy


```python
a = 'text'
print(a)
print('Adresa je: {}'.format(id(a)))
```

    text
    Adresa je: 140614800972688



```python
# Znamena to, ze neviem menit hodnotu
a[0] = 'T'
print(a)
print('Adresa je: {}'.format(id(a)))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-20-309bd94f7dc8> in <module>()
          1 # Znamena to, ze neviem menit hodnotu
    ----> 2 a[0] = 'T'
          3 print(a)
          4 print('Adresa je: {}'.format(id(a)))


    TypeError: 'str' object does not support item assignment


# List je mutable


```python
a = [1,2,3,4,5]
print(a)
print('Adresa je: {}'.format(id(a)))
```

    [1, 2, 3, 4, 5]
    Adresa je: 140614627338824



```python
# Znamena to, ze neviem menit hodnotu
a[0] = 'T'
print(a)
print('Adresa je: {}'.format(id(a)))
```

    ['T', 2, 3, 4, 5]
    Adresa je: 140614627338824


# Tuple je immutable


```python
t1 = (1, 2, 3, 4, 5)
t1
```




    (1, 2, 3, 4, 5)




```python
t1[1]
```




    2




```python
t1[1]=3
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-26-ab9dff0930da> in <module>()
    ----> 1 t1[1]=3
    

    TypeError: 'tuple' object does not support item assignment


# Nemennost moze komplikovat pracu s objektami


```python
t1 = (1, 2, 3, 4, 5)
# Ked chceme update, treba vyrobit novy objekt
t2 = t1[:2] + (17, ) + t1[3:]
t2
```




    (1, 2, 17, 4, 5)




```python
# alebo
l1 = list(t1)
l1[2] = 17
t2 = tuple(l1)
t2
```




    (1, 2, 17, 4, 5)




```python
# vs. 
a = [1,2,3,4,5]
a[2] = 17
a
```




    [1, 2, 17, 4, 5]



# Preco je nemennost dobra

# Netreba pocitat s tym, ze sa vam moze objekt zmenit

* Je to bezpecnejsie.
* vznika menej chyb
* Lahsie sa debuguje

# Lahsie sa testuje

* staci test na jednu funkciu a nie celu skupinu objektov

![testy1](http://sevo.crabdance.com:8888/user/sevo/files/FLP/obrazky/testy1.png)

![testy2](http://sevo.crabdance.com:8888/user/sevo/files/FLP/obrazky/testy2.png)

# Toto je dovod, preco ma Test Driven Development (TDD) taky usepch

* Testy sa píšu ešte pred kódom
* Zamýšľate sa ako napísať kód tak aby bol testovateľný
* Bez toho aby ste o tom vedeli odstraňujete vedľajšie efekty
* Nazite sa o to, aby na sebe funkcie co najmenej zavyseli
* Pripravovanie objektov je pre vas zbytocnou komplikaciou
* Zmena stavu objktu sposobuje, ze musite pisat velmi vela tetsov aby ste osetrili mnozstvo hranicnych stavov


# Da sa lahsie zdielat medzi vlaknami a procesmi
* netreba synchronizovat pristup k objektom

# Da sa hashovat

* ak pouzijete objekt ako kluc, tak sa urcite nezmeni a mozete 
* hashovacia funkcia nad nim vzdy vrati rovnaku hodnotu

# Objekty mozu byt mensie. Zaberaju menej miesta v pamati a operacie nad  nimi su rychlejsie.

# Ale
* Je treba vytvarat velmi vela objektov. 
* Garbage collector sa narobi.


```python
# inspirovane https://www.youtube.com/watch?v=5qQQ3yzbKp8
employees = ['Jozo', 'Eva', 'Fero', 'Miro', 'Anna', 'Kristina']

output = '<ul>\n'

for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)
#     print('Adresa outputu je: {}'.format(id(output)))

output += '</ul>'

print(output)
```

    <ul>
    	<li>Jozo</li>
    	<li>Eva</li>
    	<li>Fero</li>
    	<li>Miro</li>
    	<li>Anna</li>
    	<li>Kristina</li>
    </ul>


# Ako zabezpecit nemennost objektov?

* konvencia
* vynutit si ju

# S vela vecami si mozeme pomoct kniznicou Pyrsistent


```python
import pyrsistent as ps
```

# List / Vektor


```python
v1 = ps.pvector([1, 2, 3, 4])
v1 == ps.v(1, 2, 3, 4)
```




    True




```python
v1[1]
```




    2




```python
v1[1:3]
```




    pvector([2, 3])




```python
v1[1] = 3
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-40-00087ab71557> in <module>()
    ----> 1 v1[1] = 3
    

    TypeError: 'pvectorc.PVector' object does not support item assignment



```python
v3 = v1.set(1, 5)
print(v3)
print(v1)
```

    pvector([1, 5, 3, 4])
    pvector([1, 2, 3, 4])


# Map / dict


```python
m1 = ps.pmap({'a':1, 'b':2})
m1 == ps.m(a=1, b=2)
```




    True




```python
m1['a']
```




    1




```python
m1.b # toto s dict nejde
```




    2




```python
print(m1.set('a', 3))
print(m1)
```

    pmap({'b': 2, 'a': 3})
    pmap({'b': 2, 'a': 1})



```python
print(id(m1), id(m1.set('a', 3)))
```

    140614615606472 140614615635848


### Transformacia mutable <=> immutable


```python
ps.freeze([1, {'a': 3}])
```




    pvector([1, pmap({'a': 3})])




```python
ps.thaw(ps.v(1, ps.m(a=3)))
```




    [1, {'a': 3}]



# ... a dalsie immutable struktury
https://github.com/tobgu/pyrsistent

* PVector, similar to a python list
* PMap, similar to dict
* PSet, similar to set
* PRecord, a PMap on steroids with fixed fields, optional type and invariant checking and much more
* PClass, a Python class fixed fields, optional type and invariant checking and much more
* Checked collections, PVector, PMap and PSet with optional type and invariance checks and more
* PBag, similar to collections.Counter
* PList, a classic singly linked list
* PDeque, similar to collections.deque
* Immutable object type (immutable) built on the named tuple
* freeze and thaw functions to convert between pythons standard collections and pyrsistent collections.
* Flexible transformations of arbitrarily complex structures built from PMaps and PVectors.

# Da sa nieco spravit s tou spotrebou pamati? 

# Po niektorych operaciach sa objekty dost podobaju


```python
v1 = ps.v(0, 1, 2, 3, 4, 5, 6, 7, 8) 
print(v1)
v2 = v1.set(5, 'beef') 
print(v2)
```

    pvector([0, 1, 2, 3, 4, 5, 6, 7, 8])
    pvector([0, 1, 2, 3, 4, 'beef', 6, 7, 8])


# Zdielanie casti datovej struktury

pvector([0, 1, 2, 3, 4, 5, 6, 7, 8])

pvector([0, 1, 2, 3, 4, 'beef', 6, 7, 8])
![zdielanie casti datovej struktury](http://hypirion.com/imgs/pvec/update.png)
http://hypirion.com/musings/understanding-persistent-vector-pt-1

# Higher order functions

# Funkcional v LISPe je funkcia, ktora ma ako argument funkciu alebo funkciu vracia
* FUNCALL - vykonanie funkcie s argumentami
* MAPCAR - zobrazenie
* REMOVE-IF/REMOVE-IF-NOT - filter
* REDUCE - redukcia
* ...

# V Pythone a inych jazykoch
* **Funkcia vyssej urovne** (Higher order function) - je funkcia, ktora distava funkciu ako parameter
* **Generator** - je funkcia, ktora vracia funkciu

# Funkcie vyssej urovne sa daju velmi dobre pouzit na spracovanie zoznamu

Najcastejsie operacie so zoznamom:
* zobrazenie
* filter
* redukcia

# Zobrazenie

Aplikovanie funkcie na vsetky prvky zoznamu a vytvorenie noveho zoznamu z transformovanych prvkov


```python
def process_item(x):
    return x*x
item_list = [1,2,3,4,5,6]
```


```python
# impertivny zapis 
collection = []
for item in item_list:
    partial_result = process_item(item)
    collection.append(partial_result)
collection
```




    [1, 4, 9, 16, 25, 36]




```python
#  C-like zapis
collection = []
index = 0
while index < len(item_list):
    partial_result = process_item(item_list[index])
    collection.append(partial_result)
    index += 1
collection
```




    [1, 4, 9, 16, 25, 36]



# Zobrazenie pomocou funkcie vyssej urovne je prehladnejsie


```python
def process_item(x):
    return x*x
item_list = [1,2,3,4,5,6]
```


```python
# funkcionalny zapis
collection = map(process_item, item_list)
collection
```

    1
    4
    9


# Dalsi priklad pouzitia funkcie map


```python
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)
 
temperatures = (36.5, 37, 37.5, 38, 39)
F = list(map(fahrenheit, temperatures))
C = list(map(celsius, F))
print(F)
print(C)
```

    [97.7, 98.60000000000001, 99.5, 100.4, 102.2]
    [36.5, 37.00000000000001, 37.5, 38.00000000000001, 39.0]


# Alebo este iny


```python
list(map(len, open('morho.txt')))
```




    [8, 1, 42, 39, 40, 39]




```python
list(map(print, open('morho.txt')))
```

    Mor ho!
    
    
    
    Zleteli orly z Tatry, tiahnu na podolia, 
    
    ponad vysoké hory, ponad rovné polia; 
    
    preleteli cez Dunaj, cez tú šíru vodu, 
    
    sadli tam za pomedzím slovenského rodu.





    [None, None, None, None, None, None]



# Funkcia *map* odstranuje potrebu udrzovat si stav

* nepotrebujem ziadnu kolekciu, ktora je v nejakom case ciastocne naplnena
* nepotrebujem ziadny index, ktory sa inkrementuje
* nestaram sa o to, ako map funguje
  * iterativne, rekurziou, paralelne, distribuovane, pomocou indexu?
* nestaram sa o vnutornu strukturu kolekcie
  * staci aby sa cez nu dalo iterovat 
  * o tomto si povieme viac nabuduce

# Funkcia map by mohla byt implementovana napriklad takto


```python
def my_map(f, seq): # Takto by to mohlo byt v pythone 2 a nie 3. Tam map vracia iterator.
    result = []
    for x in seq:
        result.append(f(x))
    return result 
```

# Filter

Zo zoznamu sa vytvara novy zoznam s tymi prvkami, ktore splnaju podmienku


```python
item_list = [1,2,3,4,5,6]
def condition(x):
    return(x % 2 == 0)
```


```python
collection = []
for item in item_list:
    if condition(item):
        collection.append(item)
collection
```




    [2, 4, 6]



# Filter pomocou funkcie vyssej urovne


```python
item_list = [1,2,3,4,5,6]
def condition(x):
    return(x % 2 == 0)
```


```python
collection = filter(condition, item_list)
list(collection)
```




    [2, 4, 6]



# Dalsi priklad pouzitia funkcie *Filter*


```python
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
def is_even(x):
    return x % 2 == 0

list(filter(is_even, fibonacci))
```




    [0, 2, 8, 34]



# Redukcia

reduce(func, seq, init) 

func(a, b)

Opakovane aplikuje funkciu na sekvenciu. 

*func* prijma dva argumenty: hodnotu akumulatora a jeden prvok mnoziny

Atributom *func* moze byt prvok sekvencie alebo navratova hodnota inej *func*

![reduce](http://www.python-course.eu/images/reduce.png)

# Typicky priklad je suma prvkov zoznamu


```python
item_list = [47,11,42,13]
def add(a,b):
    return(a+b)
```


```python
from functools import reduce

reduce(add, item_list)
```




    113



![reduce1](http://www.python-course.eu/images/reduce_diagram.png)


```python
total = 0 # Takto by to bolo imperativne
for item in item_list:
    total = add(total, item)
total
```




    21



# Dalsi priklad - nasobenie prvkov zoznamu


```python
from functools import reduce
def mul(a,b):
    return a * b

reduce(mul, [1,2,3,4,5])
```




    120



# Vela funkcii uz je predpripravenych


```python
from operator import add
```


```python
from operator import mul
```

# Da sa spracovavat aj nieco ine ako cisla


```python
from functools import reduce
from operator import add

print(reduce(add, open('morho.txt')))
```

    Mor ho!
    
    Zleteli orly z Tatry, tiahnu na podolia, 
    ponad vysoké hory, ponad rovné polia; 
    preleteli cez Dunaj, cez tú šíru vodu, 
    sadli tam za pomedzím slovenského rodu.


# Da sa napriklad pracovat s mnozinami


```python
from operator import or_
reduce(or_, ({1}, {1, 2}, {1, 3}))  # union
```




    {1, 2, 3}




```python
from operator import and_
reduce(and_, ({1}, {1, 2}, {1, 3}))
```




    {1}



# Lambda funkcia

anonymna funkcia


```python
my_sum = lambda x, y: x + y
my_sum(1,2)
```




    3



* obemdzenie na jediny riadok
* nepotrebuje return

# Lambda je celkom prakticka ako parameter funkcie


```python
item_list = [1,2,3,4,5]
print(list(map(lambda x: x**2, item_list)))
```

    [1, 4, 9, 16, 25]



```python
item_list = ["auto", "macka", "traktor"]
list(map(lambda x: x.upper(), item_list))
```




    ['AUTO', 'MACKA', 'TRAKTOR']



# Spracovanie zoznamu (list comprehension)


```python
print(list(map(lambda x: x**2, [1,2,3,4,5])))
print([x**2 for x in [1,2,3,4,5]])
```

    [1, 4, 9, 16, 25]
    [1, 4, 9, 16, 25]



```python
print(list(filter(lambda x: x % 2 == 0, [1,2,3,4,5])))
print([x for x in [1,2,3,4,5] if x % 2 == 0])
```

    [2, 4]
    [2, 4]


# Na co je to cele dobre - MapReduce

* je programovací model (framework) vyvinutý a patentovaný spoločnosťou Google, Inc. v roku 2004
* hlavným cieľom jeho vývoja bolo uľahčiť programátorom vytváranie paralelných aplikácií, ktoré spracovávajú veľké objemy dát
* zložité výpočty nad veľkým objemom dát musia byť vykonávané paralelne, niekedy až na stovkách alebo tisíckach počítačov súčasne
* pri takomto spracovaní sa treba okrem samotného výpočtu sústrediť napríklad aj na
  * rovnomerné rozdelenie záťaže všetkým dostupným počítačom
  * kontrolovanie výpadkov a porúch spolu s ich následným riešením
* MapReduce prináša ďalšiu vrstvu abstrakcie medzi výpočet, ktorý sa má realizovať paralelne a jeho vykonanie na konkrétnom hardvéri
* Keď napíšem program správne, tak sa nemusím starať na koľkých počítačoch bude bežať

![mapreduce](http://sevo.crabdance.com:8888/user/sevo/files/FLP/obrazky/mapreduce.png)

# GOTO priklad z netu
Celkom pekny priklad na jednoduchu MapReduce ulohu v Pythone.

Klasicky Word count priklad

http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/

--- pseudokod ---
function map(String name, String document):

  // name: document name
  
  // document: document contents
  
  for each word w in document:
  
    emit (w, 1)



function reduce(String word, Iterator partialCounts):

  // word: a word
  
  // partialCounts: a list of aggregated partial counts
  
  sum = 0
  
  for each pc in partialCounts:
  
    sum += pc
    
  emit (word, sum)

# GOTO Spark

# Nieco na dalsie studium

* Balicek Operator - https://docs.python.org/3/library/operator.html
* Balicek Itertools - https://docs.python.org/3/library/itertools.html
* Balicek Functools - https://docs.python.org/3/library/functools.html
