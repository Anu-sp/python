#Single Iterable
def square(x):
    return x*x

numbers = [1,2,3,4,5]
squared_number = map(square,numbers)
print(type(squared_number))
print(list(squared_number))


#multipal Iterable
def add(x,y):
    return x+y

numbers1 = [1,2,3]
numbers2 = [4,5,6]
result = map(add,numbers1,numbers2)
print(list(result))


#Converting Strings to Uppercase
words = ['hello','python','map']
uppercase = map(str.upper,words)
print(list(uppercase))


#Calculating the Length of Strings
word = ["apple","banana","mango"]
length = map(len,word)
print(list(length))


#Converting a List of Integers to Strings
number = [1,2,3,4,5,6]
string_number = map(str,number)
print(list(string_number))


# Capitalizing the First Letter of Each Word
Words = ["hello", "world", "python"]
capitalized_words = map(str.capitalize, Words)
print(list(capitalized_words))

#Adding Corresponding Elements from Two Lists
list1 = [1,2,3]
list2 = [4,5,6]
sums = map(lambda x,y : x+y , list1, list2)
print(list(sums)) 

#Extracting the First Character of Each String
words = ['apple', 'banana','cheery']
first_chars = map(lambda word : word[0], words)
print(list(first_chars))

#Converting Temperatures from Celsius to Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))
