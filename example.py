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


#27
import re
from collections import defaultdict

def frequency_count(input_str):
    input_str = input_str.lower()
    input_str = re.sub(r'[^\w\s]','',input_str)
    words = input_str.split()
    word_count = defaultdict(int)

    for word in words:
        word_count[word]  += 1
    return dict(word_count)

input_string = "Hello world! Hello everyone. Welcome to the world of Python."
result = frequency_count(input_string)
print(result)


#28
from collections import defaultdict 

def group_by_length(words):
    length_dict = defaultdict(list)
    for word in words:
        length_dict[len(word)].append(word)
    return dict(length_dict)

words = ["apple", "bat", "ball", "cat", "dog", "elephant", "fish"]
result = group_by_length(words)
print(result)


#29
import pickle

class Book:
    def __init__(self, title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title:{self.title} ,  Author:{self.author} , ISBN :{self.isbn}"
    
class Library():
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        try:
            with open("books.pkl", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []
        
    def save_books(self):
        with open("books.pkl","wb") as file:
            pickle.dump(self.books,file)

    def add_books(self,book):
        self.books.append(book)
        self.save_books()

    def display_books(self):
        if self.books:
            print("books in library")
            for book in self.books:
                print(book)
        else:
            print("no books available in the library")

def main():
    library = Library()
    while True:
        print("Library management System")
        print("1.add books")
        print("2.view books")
        print("3.exit")
        choice = input("enter the choice: ")
        if choice == "1":
            title = input("enter the title : ")
            author = input("enter thr author : ")
            isbn = input("enter the isbn : ") 
            book = Book(title,author,isbn)
            library.add_books(book)
            print("books added")
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            exit
        else:
            print("enter the valid input")
    
main()

#30
print("Hi! I am chatbot, print 'exit' to end the conversation")

while True:
    user_input = input("you: ").lower()

    if 'hello' in user_input:
        print("chatbot: hi")
    elif 'how are you' in user_input:
        print("I'm good , thank you")
    elif 'exit' in user_input:
        print("byeeee")
        break
    else:
        print("error")

#31
import re

def check_password_strength(password):
    if len(password) < 8:
        return "weak:password length should be more then 8 character"
    if not re.search("[A-Z]",password):
        return "weak:password shouls contain atleast one uppercase letter"
    if not re.search("[a-z]",password):
        return "weak:password should contain atleast one lowercase letter"
    if not re.search("[0-9]",password):
        return "weak:password should contain atleast one number"
    if not re.search("[@#$%^&+=]",password):
        return "weak:password should contain atleast one special character"
    return  "Strong: Password is strong."

password = input("Enter your password: ")
print(check_password_strength(password))   

#32
class MenuItem:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.category}): ${self.price:.2f}"

class Drink(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, "Drink", price)
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.size}): ${self.price:.2f}"

class Dish(MenuItem):
    def __init__(self, name, price, ingredients):
        super().__init__(name, "Dish", price)
        self.ingredients = ingredients

    def __str__(self):
        return f"{self.name} (Ingredients: {', '.join(self.ingredients)}): ${self.price:.2f}"

class Order:
    def __init__(self):
        self.items = []
        self.is_complete = False

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def complete_order(self):
        self.is_complete = True

class Customer:
    def __init__(self, name):
        self.name = name
        self.order = Order()

    def place_order(self, menu_items):
        for item in menu_items:
            self.order.add_item(item)

    def view_order(self):
        for item in self.order.items:
            print(item)
        print(f"Total: ${self.order.calculate_total():.2f}")

class Restaurant:
    def __init__(self):
        self.tables = {}
        self.menu = []

    def add_table(self, number, customer):
        self.tables[number] = customer

    def remove_table(self, number):
        if number in self.tables:
            customer = self.tables[number]
            customer.order.complete_order()
            print(f"Table {number} completed order for {customer.name}.")
            del self.tables[number]

    def view_menu(self):
        print("Menu:")
        for item in self.menu:
            print(item)

    def add_menu_item(self, item):
        self.menu.append(item)

restaurant = Restaurant()

restaurant.add_menu_item(Dish("Pasta", 12.99, ["tomato", "basil", "cheese"]))
restaurant.add_menu_item(Dish("Burger", 9.99, ["beef", "lettuce", "cheese"]))
restaurant.add_menu_item(Drink("Coffee", 2.99, "Medium"))
restaurant.add_menu_item(Drink("Orange Juice", 3.99, "Large"))

restaurant.view_menu()

customer1 = Customer("Alice")
restaurant.add_table(1, customer1)

customer1.place_order([restaurant.menu[0], restaurant.menu[2]])

print("\nAlice's Order:")
customer1.view_order()

restaurant.remove_table(1)

#33
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name}, Email: {self.email}, Phone: {self.phone}"


class Student(Person):
    def __init__(self, name, email, phone, student_id):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"Student {self.name}, ID: {self.student_id}, Courses: {[c.course_name for c in self.courses]}"


class Teacher(Person):
    def __init__(self, name, email, phone, teacher_id):
        super().__init__(name, email, phone)
        self.teacher_id = teacher_id
        self.assigned_courses = []

    def assign_grade(self, student, course, grade):
        print(f"Assigning grade {grade} to {student.name} in {course.course_name}")

    def __str__(self):
        return f"Teacher {self.name}, ID: {self.teacher_id}, Courses: {[c.course_name for c in self.assigned_courses]}"

class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)
        student.enroll(self) 

    def assign_teacher(self, teacher):
        self.teachers.append(teacher)
        teacher.assigned_courses.append(self)  

    def __str__(self):
        return f"Course: {self.course_name}, Code: {self.course_code}, Students: {[s.name for s in self.students]}, Teachers: {[t.name for t in self.teachers]}"


class School:
    def __init__(self, name):
        self.name = name
        self.students = {}
        self.teachers = {}
        self.courses = {}

    def add_student(self, student):
        self.students[student.student_id] = student

    def add_teacher(self, teacher):
        self.teachers[teacher.teacher_id] = teacher

    def add_course(self, course):
        self.courses[course.course_code] = course

    def enroll_student_in_course(self, student_id, course_code):
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            course.add_student(student)
        else:
            print("Invalid student ID or course code")

    def assign_teacher_to_course(self, teacher_id, course_code):
        if teacher_id in self.teachers and course_code in self.courses:
            teacher = self.teachers[teacher_id]
            course = self.courses[course_code]
            course.assign_teacher(teacher)
        else:
            print("Invalid teacher ID or course code")

    def __str__(self):
        return (f"School: {self.name}, Students: {[s.name for s in self.students.values()]}, "
                f"Teachers: {[t.name for t in self.teachers.values()]}, Courses: {[c.course_name for c in self.courses.values()]}")
    


if __name__ == "__main__":
    school = School("Greenfield High")

    student1 = Student("Alice", "alice@example.com", "1234567890", "S001")
    student2 = Student("Bob", "bob@example.com", "0987654321", "S002")

    teacher1 = Teacher("Dr. Smith", "smith@example.com", "5551234567", "T001")
    teacher2 = Teacher("Ms. Johnson", "johnson@example.com", "5559876543", "T002")

    course1 = Course("Math 101", "M101")
    course2 = Course("History 201", "H201")

    school.add_student(student1)
    school.add_student(student2)
    school.add_teacher(teacher1)
    school.add_teacher(teacher2)

    school.add_course(course1)
    school.add_course(course2)

    school.enroll_student_in_course("S001", "M101")
    school.enroll_student_in_course("S002", "H201")

    school.assign_teacher_to_course("T001", "M101")
    school.assign_teacher_to_course("T002", "H201")

    print(school)
    
    print(course1)
    print(course2)
    
    teacher1.assign_grade(student1, course1, "A")

#34
class Flight:
    def __init__(self, flight_number, destination, departure_time, seats_available):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.seats_available = seats_available
        self.capacity = seats_available 

    def check_availability(self):
        return self.seats_available > 0

    def book_seat(self):
        if self.check_availability():
            self.seats_available -= 1
            return True
        else:
            return False

    def cancel_seat(self):
        if self.seats_available < self.capacity:
            self.seats_available += 1
            return True
        else:
            return False

    def __str__(self):
        return (f"Flight {self.flight_number} to {self.destination} at {self.departure_time}, "
                f"Seats available: {self.seats_available}/{self.capacity}")


class Passenger:
    def __init__(self, name, passport_number):
        self.name = name
        self.passport_number = passport_number
        self.booked_flights = []

    def add_booking(self, flight):
        self.booked_flights.append(flight)

    def remove_booking(self, flight):
        if flight in self.booked_flights:
            self.booked_flights.remove(flight)

    def __str__(self):
        booked_flight_numbers = [flight.flight_number for flight in self.booked_flights]
        return f"Passenger {self.name}, Passport: {self.passport_number}, Booked flights: {booked_flight_numbers}"


class Reservation:
    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight

    def reserve_seat(self):
        if self.flight.book_seat():
            self.passenger.add_booking(self.flight)
            print(f"Reservation successful for {self.passenger.name} on flight {self.flight.flight_number}.")
            return True
        else:
            print(f"No seats available on flight {self.flight.flight_number}.")
            return False

    def cancel_reservation(self):
        if self.flight.cancel_seat():
            self.passenger.remove_booking(self.flight)
            print(f"Reservation canceled for {self.passenger.name} on flight {self.flight.flight_number}.")
            return True
        else:
            print(f"Cannot cancel reservation. No seat was reserved.")
            return False


class FlightSystem:
    def __init__(self):
        self.flights = {}
        self.passengers = {}
        self.reservations = []

    def add_flight(self, flight):
        self.flights[flight.flight_number] = flight

    def register_passenger(self, passenger):
        self.passengers[passenger.passport_number] = passenger

    def make_reservation(self, passport_number, flight_number):
        passenger = self.passengers.get(passport_number)
        flight = self.flights.get(flight_number)

        if not passenger:
            print(f"Passenger with passport {passport_number} not found.")
            return None
        if not flight:
            print(f"Flight {flight_number} not found.")
            return None

        reservation = Reservation(passenger, flight)
        if reservation.reserve_seat():
            self.reservations.append(reservation)
            return reservation
        return None

    def cancel_reservation(self, passport_number, flight_number):
        for reservation in self.reservations:
            if (reservation.passenger.passport_number == passport_number and
                    reservation.flight.flight_number == flight_number):
                if reservation.cancel_reservation():
                    self.reservations.remove(reservation)
                return

        print("Reservation not found.")

    def __str__(self):
        flights_info = "\n".join(str(flight) for flight in self.flights.values())
        passengers_info = "\n".join(str(passenger) for passenger in self.passengers.values())
        return f"Flights:\n{flights_info}\n\nPassengers:\n{passengers_info}"

if __name__ == "__main__":
    system = FlightSystem()

    flight1 = Flight("AI101", "New York", "2024-11-10 14:00", 10)
    flight2 = Flight("BA202", "London", "2024-11-11 16:00", 5)
    system.add_flight(flight1)
    system.add_flight(flight2)

    passenger1 = Passenger("Alice Smith", "P001")
    passenger2 = Passenger("Bob Johnson", "P002")
    system.register_passenger(passenger1)
    system.register_passenger(passenger2)

    system.make_reservation("P001", "AI101")
    system.make_reservation("P002", "BA202")
    system.make_reservation("P001", "BA202")  

    print("\nSystem state after bookings:")
    print(system)

    system.cancel_reservation("P001", "AI101")

    print("\nSystem state after cancellation:")
    print(system)

#35
#Given a number n, find the sum of the product of each pair of its digits, repeatedly until you get a single-digit answer.

def sum_of_products(n):
    digits = [int(d) for d in str(n)]
    while len(digits) > 1 or sum(digits) >= 10:
        products = [digits[i] * digits[j] for i in range(len(digits)) for j in range(i + 1, len(digits))]
        digits = [int(d) for d in str(sum(products))]
    return digits[0]

print(sum_of_products(123))        

#36
# Given a number n, create two numbers: one from arranging digits in ascending order and one in descending order. 
# Subtract the smaller from the larger and repeat until you reach a single-digit.

def sum(n):
    while n >= 10:
        digits = sorted(str(n))
        asc = int("".join(digits))
        desc = int("".join(digits[::-1]))
        n = desc - asc
    return n

print(sum(324)) 

#37 Longest Consecutive Sequence
def longest_consecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

nums = [100, 4, 200, 1, 3, 2]
print("Longest Consecutive Sequence Length:", longest_consecutive(nums))

#38  Find Missing Number in Array
def find_missing_number(arr):
    n = len(arr) + 1  
    
    expected_sum = n * (n + 1) // 2
   
    actual_sum = sum(arr)
    
    missing_number = expected_sum - actual_sum
    
    return missing_number

arr = [1, 2, 4, 6, 3, 7, 8]
print("The missing number is:", find_missing_number(arr))

#39
import calendar

def calendar(year, month):
    print(calendar.month(year, month))

try:
    year = int(input("Enter the year (e.g., 2023): "))
    month = int(input("Enter the month (1-12): "))

    if 1 <= month <= 12:
        calendar(year, month)
    else:
        print("Invalid month. Please enter a number between 1 and 12.")
except ValueError:
    print("Invalid input. Please enter a valid year and month.")

#40 FizzBuzz
#Print numbers from 1 to 100, replacing multiples of 3 with "Fizz" and multiples of 5 with "Buzz."

for i in range(1, 101):  
    if i % 3 == 0 and i % 5 == 0:  
        print("FizzBuzz")
    elif i % 3 == 0: 
        print("Fizz")
    elif i % 5 == 0:  
        print("Buzz")
    else:
        print(i) 

#41  Expense Tracker
class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def show_summary(self):
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")

tracker = ExpenseTracker()
tracker.add_expense("Groceries", 150)
tracker.add_expense("Travel", 80)
tracker.add_expense("Groceries", 50)
tracker.show_summary()

#42 Find Pairs with Given Sum in List
def pairs(nums,sum):
    seen = set()
    pairs = []
    for num in nums:
        complement = sum - num
        if complement in seen :
            pairs.append((num,complement))
        seen.add(num)
    return pairs

nums = [1,2,3,4,5,6]
print(pairs(nums, 7))
    
#43 Hospital management system
class Patient:
    def __init__ (self,name,age):
        self.name = name 
        self.age = age
        self.medical_history = []
        self.current_appointments = []

    def add_medical_record(self,record):
        self.medical_history.append(record)

    def view_medical_history(self):
        print(f"medical history for {self.name}")
        for record in self.medical_history:
            print(f"-{record}")

class Doctor:
    def __init__(self,name,specialization):
        self.name = name 
        self.specialization = specialization
        self.schedule = {}

    def add_availability(self,day,time):
        if day not in self.schedule:
            self.schedule[day] = []
        self.schedule[day].append(time)

    def view_schedule(self):
        print(f"Schedule for Dr. {self.name} ({self.specialization}):")
        for day, times in self.schedule.items():
            print(f"  {day}: {', '.join(times)}")

class Appointment:
    def __init__(self,date,time,doctor,patient):
        self.date = date
        self.time = time
        self.doctor =  doctor
        self.patient = patient

    def details(self):
        return f"Appointement on {self.date} and {self.time} -Doctor:{self.doctor} , Patient:{self.patient}"

class Hospital:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self,patient):
        self.patients.append(patient)

    def add_doctor(self,doctor):
        self.doctors.append(doctor)

    def book_appointment(self,patient_name,doctor_name,date,time):
        patient = next((p for p in self.patients if p.name == patient_name), None)
        doctor = next((q for q in self.doctors if q.name == doctor_name), None)

        if not patient:
            print(f"Error :Patient {patient_name} not found")
            return
        if not doctor:
            print(f"Error :Doctor {doctor_name} not found")
            return
        if date not in doctor.schedule or time not in doctor.schedule[date]:
            print(f"Error: Dr. {doctor_name} is not available at {time} on {date}.")
            return

        appointment = Appointment(date,time,doctor,patient)
        self.appointments.append(appointment)
        patient.current_appointments.append(appointment)
        doctor.schedule[date].remove(time)

        print(f"Appointment booked successfully: {appointment.details()}")

    def view_all_appointments(self):
        print("All Appointments:")
        for appointment in self.appointments:
            print(appointment.details())

if __name__ == "__main__":
    hospital = Hospital()

    doctor1 = Doctor("Smith", "Cardiology")
    doctor1.add_availability("Monday", "10:00 AM")
    doctor1.add_availability("Monday", "11:00 AM")
    hospital.add_doctor(doctor1)

    doctor2 = Doctor("Johnson", "Dermatology")
    doctor2.add_availability("Tuesday", "2:00 PM")
    hospital.add_doctor(doctor2)

    patient1 = Patient("Alice", 30)
    patient1.add_medical_record("2022: General check-up")
    patient1.add_medical_record("2023: Follow-up on blood tests")
    hospital.add_patient(patient1)

    patient2 = Patient("Bob", 45)
    hospital.add_patient(patient2)

    hospital.book_appointment("Alice", "Smith", "Monday", "10:00 AM")
    hospital.book_appointment("Bob", "Johnson", "Tuesday", "2:00 PM")
    hospital.book_appointment("Alice", "Smith", "Monday", "12:00 PM")  

    hospital.view_all_appointments()

    doctor1.view_schedule()

    patient1.view_medical_history()

#44
class VendingMachine:
    def __init__ (self):
        self.items = {
            "chips":20,
            "chocolate":30,
            "soda":25,
            "juice":35
        }
        self.balance = 0

    def display_items(self):
        print("Available items")
        for items,price in self.items.items:
            print(f"{items}: ${price}")

    def insert_money(self,amount):
        self.balance += amount
        print(f"Current balance : ${self.balance}")

    def select_items(self,item):
        if item not in self.items:
            print("item not available")
            return
        if self.balance < self.items[item]:
            print(f"Not enough balance")
            return
        self.balance -= self.items[item]
        print(f"Dispensed {item}. Remaining balance: ${self.balance}")

    def return_change(self):
        print(f"Returning change: ${self.balance}")
        self.balance = 0

machine = VendingMachine()
machine.display_items()
machine.insert_money(50)
machine.select_items("chips")
machine.return_change()

#45
def length_encoder(text):
    if not text:
        return ""
    
    compressed = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count  += 1
        else:
            compressed.append(str(count) + text[i-1])
            count = 1

    compressed.append(str(count) + text [-1])
    return ''.join(compressed)

print(length_encoder("AAABBBCCCA"))

#46
def parentheses(n):
    def backtrack(s,left,right):
        if len(s) == 2*n:
            result.append(s)
            return
        if left < n:
            backtrack(s + "(", left+1, right)
        if right < left:
            backtrack(s + ")" , left , right+1)

    result = []
    backtrack("",0,0)
    return result

print(parentheses(2))

#47
def count_island(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0

    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return
        grid[r][c] = "0" 
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                dfs(r, c)

    return count

island_grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print(count_island(island_grid))

#48
def find_pair(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)

    return list(pairs)

print(find_pair([1, 2, 3, 4, 5, 6], 7))

#49
