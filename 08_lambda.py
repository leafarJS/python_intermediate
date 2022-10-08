#lambda arguments: expresssion
#la función lambda es una pequeña function anonima de una linea que se define sin nombre 

add10 = lambda x: x + 10
print(add10(15))

mult = lambda x,y : x * y
print(mult(15,7))

point2D = [(1,2),(15,1),(5,-1),(10,4)]
point2D_sort = sorted(point2D, key = lambda x: x[0] + x[1])

print(point2D)
print(point2D_sort)

a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
print(a)
print(b)
print(list(b))


c = [x*2 for x in a]
print(c)

a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
b = filter(lambda x : x%2 == 0, a)
print(list(b))

c = [x for x in a if x%2 == 0]
print(c)


from functools import reduce

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

prod_a = reduce(lambda x,y: x+y, a)
print(prod_a)

