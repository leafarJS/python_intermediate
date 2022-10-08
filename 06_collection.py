#collections, counter, namedtuple, ordereddict, defaultdict, deque
from collections import Counter 

a = "aaaabbbbccccc"
my_count = Counter(a)
print(my_count)
print(my_count.keys())
print(my_count.values())
print(my_count.most_common(2))
print(my_count.most_common(1))#mas comun
print(my_count.most_common(1)[0])
print(my_count.most_common(1)[0][0])
print(list(my_count.elements()))
print(len(list(my_count.elements())))

from collections import namedtuple

Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

from collections import OrderedDict

ordered_dict = OrderedDict()#3.7 {} 3.10
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(ordered_dict)

from collections import defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d)
print(d['a'])
print(d['z'])#0

from collections import deque

a = deque()
a.append(1)
a.append(2)
a.append(3)
print(a)

a.pop()
print(a)


a.appendleft(4)
print(a)

a.popleft()
print(a)

a.extend([10,11,12])
print(a)

a.extendleft([7,8,9])
print(a)

a.rotate()
print(a)

a.rotate(-1)
print(a)

a.clear()
print(a)

