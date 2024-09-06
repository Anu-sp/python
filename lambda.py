#Basic Syntax
# lambda arguments: expression


# Simple Lambda Function:
add = lambda x,y : x+y
print(add(2,3))


#Simple Lambda Function:
numbers = [1,2,3,4,5]
squared_number = map(lambda x : x ** 2, numbers)
print(list(squared_number))


#Lambda Function in a filter() Function:
number = [1,2,3,4,5,6,7,8,9,10]
even_number = filter(lambda x : x%2 == 0, number)
print(list(even_number)) 


#Lambda Function in a sorted() Function:
points = [(1, 2), (4, 1), (3, 5), (2, 4)]
points_sorted = sorted(points, key=lambda x: x[0])
print(points_sorted)