#1
def sum(x,y):
    return x+y

x = int(input("enter x: "))
y = int(input("enter y: "))

print(sum(x,y))

#2
def even_odd(x):
    if x % 2 == 0:
        print("x is even")
    else :
        print("x is odd")

x = int(input("enter x : "))
print(even_odd(x))

#3
def temp_convert(x):
    return (x * 9 / 5 )+ 32

x = int(input("enter x: "))
print(temp_convert(x))

#4
def factorial(x):
    if x==0:
        return 1
    else:
        return x * factorial(x-1)

x = int(input("enter x: "))
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
def count_words(sentence):
    words = sentence.split()
    return len(words)

input_sen = input("enter the sentence: ")
print(count_words(input_sen))

#15
class Bankaccount:
    def __init__ (self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited"
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"{amount} withdraw"
        return f"insufficient balance"
    
    def get_balance(self):
        return f"current balance: {self.balance}"
    
acc = Bankaccount("xyz", 10000)
print(acc.deposit(200))
print(acc.withdraw(400))
print(acc.get_balance())
    

#16
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"Book borrowed sucessfully"
        return f"Book is not borrowed"
    
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"Book id returned"
        return f"book is not returned"
    
book = Book("XYZ","ABC")
print(book.borrow())
print(book.return_book())

#17
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 *( self.length + self.width)
    
rect = Rectangle(10,20)
print(rect.area())
print(rect.perimeter())

#18
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)
    
stu = Student("ABC",[78,89,98,56,57])
print(stu.average())

#19
class Employee:
    def __init__ (self,name,salary):
        self.name = name 
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12
    
    def apply_bonous(self,bonous):
        self.salary += bonous
        return self.salary
    
emp = Employee("abc", 1000)
print(emp.annual_salary())
print(emp.apply_bonous())

#20
class Shoppingcart:
    def __init__(self):
        self.items = []

    def add_items(self,item,price):
        self.items.append((item,price))
        return f"{item} added to cart"
    
    def remove_item(self,item):
        self.items = [i for i in self.items if i[0] != item]
        return f"{item} removed from cart."
    
    def total_cost(self):
        return sum(price for _, price in self.items)

cart = Shoppingcart()
print(cart.add_item("Laptop", 800))
print(cart.add_item("Phone", 400))
print(cart.total_cost())

#21
class MovieTicket:
    def __init__(self,seats=50):
        self.available_ticket = seats

    def book_ticket(self,num):
        if num <= self.available_ticket:
            self.available_ticket -= num
            return f"{num} tickets booked."
        return "Not enough seats available."
    
    def available_seats_count(self):
        return f"Available seats: {self.available_seats}"

ticket_system = MovieTicket()
print(ticket_system.book_ticket(5))
print(ticket_system.available_seats_count())

#22
def sum_of_digits(n):
    if n==0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(123456789))

#23 Power of number
def power (a,b):
    if b == 0:
        return 0
    return a * power(a,b-1)

print(power(2,5))

#24
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern,email):
        print(f"{email} : is valid")
    else:
        print(f"{email} : is not valid")

emails = ["example@example.com", "invalid-email@", "name@domain"]
for email in emails:
    validate_email(email)

#25 number guessing game
import random

def guess_no():
    number = random.randint(1,10)
    attempt = 0

    while True:
        guess = int(input("guess the number between 1 to 10: "))
        attempt += 1
        if guess > number:
            print("too high")
        elif guess < number:
            print("too low")
        else:
            print(f"Correct! You guessed it in {attempt} attempts.")
            break
guess_no()

#26
def multiplication_table(number):
    for i in range(1,11):
        print(f"{number} x {i} = {number * i}" )

num = int(input("Enter a number for the multiplication table: "))
multiplication_table(num)

