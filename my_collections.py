# namedtuple: Use when you need a lightweight object for storing data with named fields.
# deque: Use when you need fast appends and pops from both ends of a sequence.
# Counter: Use for counting occurrences of items in a collection.
# OrderedDict: Use when you need to maintain the order of items in a dictionary (especially if working with Python versions before 3.7).
# defaultdict: Use when you need a dictionary with a default value for missing keys.


from collections import namedtuple

#define a namedtuple
Person = namedtuple ('Person', ['name','age'])

#create an instance
p = Person(name='ABC', age=30)
q = Person(name='XYZ', age=20)

# Access fields by name
print(p.name) 
print(p.age)
print(q.name)
print(q.age)


from collections import deque

# Create a deque
d = deque([1, 2, 3])
print("Initial deque:", d)

# Append elements
d.append(4)
print("After append(4):", d)

d.appendleft(0)
print("After appendleft(0):", d)

# Pop elements
d.pop()
print("After pop():", d)

d.popleft()
print("After popleft():", d)
         


from collections import Counter

# Create a Counter object
c = Counter('gallahad')

# Count occurrences
print(c)            # Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})

# Access counts
print(c['a'])       
print(c['z'])      


from collections import OrderedDict

# Create an OrderedDict
od = OrderedDict(a=1, b=2, c=3)

# Access elements
print(od)          



from collections import defaultdict

# Create a defaultdict with int as the default factory (default value is 0)
dd = defaultdict(int)

# Update values
dd['key'] += 1

# Access elements
print(dd['key'])    
print(dd['missing'])  





