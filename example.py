#1
def sum(x,y):
    return x+y

x=int(input("enter x: "))
y=int(input("enter y: "))

print(sum(x,y))

#2
def even_odd(x):
    if x % 2 == 0:
        print("x is even")
    else :
        print("x is odd")

x= int(input("enter x : "))
print(even_odd(x))

#3
def temp_convert(x):
    return (x * 9 / 5 )+ 32

x= int(input("enter x: "))
print(temp_convert(x))

#4
def factorial(x):
    if x==0:
        return 1
    else:
        return x * factorial(x-1)

x= int(input("enter x: "))
print(factorial(x))   

#5
def simple_interest(p,r,t):
    return (p*r*t) / 100

p = int(input("enter principal amount: "))
r = int(input("enter rate: "))
t = int(input("enter time: "))

print(simple_interest(p,r,t))

#6
def count_vowles(input):
    vowles = "aeiouAEIOU"
    count = 0
    for char in input:
        if char in vowles:
            count += 1
    return count

input= input("enter the string: ")
print(count_vowles(input))

#7
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("enter the number: "))
if prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


#8
def palindrome(s):
    s = s.lower().replace(" ","")
    return s == s [::-1]

input = input("enter the string: ")
if palindrome(input):
    print(f"{input} is a palindrome.")
else:
    print(f"{input} is not a palindrome.")


#9
def find_largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("The largest number is:", find_largest(a, b, c))

#10
def calculator(a,b,op):
    if op == "+" :
        return a + b
    elif op == "-" :
        return a - b
    elif op == "*" :
        return a * b
    elif op == "/" :
        if b != 0:
            return a / b
        else :
            return "Error: Division by zero"
    else:
        return "Invalid operation"

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

result = calculator(a, b, operation)


#11
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))


#12 Armstrong Number Checker
def armstrong(n):
    power = len(str(n))
    sum_of_power = sum(int(digit) ** power for digit in str(n))
    return n == sum_of_power

number = int(input("Enter a number: "))
if armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


#13 Reverse of string
def reverse(s):
    return s[::-1]

input_string = input("enter the string: ")
print(reverse(input))


#14 Count Words in a Sentence
def count_words(setence):
    words = setence.split()
    return len(words)

input_sen = input("enter the sentence: ")
print(count_words(input_sen))

#15 

