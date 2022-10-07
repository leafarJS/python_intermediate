#set unordered, mutale no duplicates
myset = {1,2,3,4,5,6,7,8,9,9,9}
print(len(myset))
print(myset)

myset = set("hello")
print(myset)
print(type(myset))

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

print(myset.pop())
print(myset)


myset = {1,2,3,4,5,6,7,8,9,9,9}

for i in myset:
  print(i)
  
if 4 in myset:
  print("Yes")
else:
  print("Not Fount!")
  

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7,11}

unions = odds.union(evens)
print(unions)

intersections = odds.intersection(evens)  
print(intersections) 

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

diff = setB.difference(setA)
print(diff)

#diffs = setA.symetric_difference(setB)
#print(diffs) #Error

#diffs = setB.symetric_difference(setA)
#print(diffs) #Error

setA.update(setB)
print(setA) #Error

setA.intersection_update(setB)
print(setA) 

setB.intersection_update(setA)
print(setB) 

setA.difference_update(setB)
print(setA)

setA.symmetric_difference_update(setB)
print(setA)



x = {1,2,3,4,5,6}
y = {1,2,3}
z = {7,8}

print(x.issubset(y)) #false
print(y.issubset(x)) #True

print(x.issuperset(y)) #True
print(y.issuperset(x)) #False

print(x.isdisjoint(y)) #False
print(y.isdisjoint(x)) #False
print(y.isdisjoint(z)) #True

conj = x
conj.add(100)
print(x)
print(conj)

conj = set(y)
conj.add(100)
print(y)
print(conj)

a = frozenset([1,2,3,4])
print(a)

a.add(6) #error
a.remove(3) #error









