#itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators 

#herramienta para mejorar los iteradores

from itertools import product

a = [1,2]
b = [3,4]
prod = product(a, b)
print(prod)
print(list(prod))

prod1 = product(a,b, repeat=2)
print(list(prod1))

print("*=" * 10)

from itertools import permutations

a = [10,20,30,40]
permutaciones = permutations(a)
print(list(permutaciones))

permutaciones1 = permutations(a, 2)
print(list(permutaciones1))

print("*=" * 10)

from itertools import combinations, combinations_with_replacement 

x = [1,2,3,4]
comb = combinations(x, 2)
print(comb)
print(list(comb))

y = [1,2,3,4]
comb_wr = combinations_with_replacement(y, 2)
print(comb_wr)
print(list(comb_wr))
print("*=" * 10)


from itertools import accumulate
import operator

z = [1,2,3,4,5]
acum = accumulate(z)
print(z)
print(list(acum))

x = [1,2,3,4]
acum = accumulate(x, func = operator.mul)
print(x)
print(list(acum))

x = [1,2,5,3,4]
acum = accumulate(x, func = max)
print(x)
print(list(acum))

print("*=" * 10)
from itertools import groupby 

def smaller_than_3(x):
  return x < 3

a = [-1,0,1,2,3,4]
group_obj = groupby(a, key = smaller_than_3)

print(a)
print(list(group_obj))

for key, value in group_obj:
  print(key, list(value))
  
persons = [{'name':'tam', 'age':25}, {'name':'tem', 'age':26}, {'name':'tim', 'age':27},{'name':'tom', 'age':28},{'name':'tum', 'age':29}]
  
group_obj = groupby(persons, key=lambda x:x['age'])

for key, value in group_obj:
  print(key, list(value))
  
  
print("*=" * 10)
from itertools import count, cycle, repeat

a = [1, 2, 3, 4, 5]

for i in count(10): # no se detiene es infinito
  print(i)
  if i == 250:
    print("Yeah!")
    break
  
for i in cycle(a):
  print(i)
  if i == a[3]:
    print("The end")
    break
  
for i in repeat(1, 4):
  print(i);