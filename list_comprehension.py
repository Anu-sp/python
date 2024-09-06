#syntax = [expression for item in iterable if condition]

#Basic List Comprehension:
squares = [x**2 for x in range(10)]
print(squares)

#List Comprehension with Condition:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

#Applying a Function:
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)

#Filtering with Multiple Conditions:
divisible_by_2_and_3 = [x for x in range(20) if x%2 == 0 and x%3 == 0]
print(divisible_by_2_and_3)

#Creating a Dictionary from Two Lists:
keys = ['name','age','location']
values = ['Alice', 25, 'New York']

my_dict = {keys[i]:values[i] for i in range(len(keys))}
print(my_dict)

#List Comprehension with Nested Loops:
list1 = [1,2,3]
list2 = ['a','b','c']

pairs = [(x,y) for x in list1 for y in list2]
print(pairs)

