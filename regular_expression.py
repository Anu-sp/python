#re.match(): Checks for a match only at the beginning of the string.

import re

pattern = r'hello'
text = 'hello world'
match = re.match(pattern,text)

if match:
    print("match found!")
else:
    print("not found")


#re.search(): Searches for a match anywhere in the string.

import re

pattern1 = r'hello'
text1 = 'hello world'
search = re.search(pattern1,text1)

if search:
    print("search found!")
else:
    print("not found")


#re.findall(): Finds all occurrences of the pattern in the string.

import re

pattern3 = r'\d+'
text3 = 'There are 24 apples and 42 oranges.'
numbers = re.findall(pattern3, text3)

print(numbers)


#re.sub(): Replaces occurrences of the pattern with a replacement string.
import re

pattern4 = r'apples'
replacement = 'bananas'
text4 = 'There are apples and oranges.'
new_text = re.sub(pattern4, replacement, text4)

print(new_text)


#Email Validation

import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = 'example@example.com'
if re.match(email_pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")


#1
import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)


#2
import re

txt = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)


#3
import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x = re.findall("he..o", txt)
print(x)

#4
import re

txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#C:\Users\DELL\data.docx


#-----------------------------------------------------------------------------------------------------------------

import re

phone_pattern = re.compile(r'\+?\d{1,4}?[-.\s]?\(?\d{1,4}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}')
email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')

def extract_patterns(filename):
    with open(filename,'r') as file:
        content = file.read()

    phone_numbers = phone_pattern.findall(content)
    emails = email_pattern.findall(content)

    return phone_numbers, emails


filename = "C:\\Users\\DELL\\Downloads\\data.txt"
phone_numbers, emails = extract_patterns(filename)

print("Phone Numbers:")
for phone in phone_numbers:
    print(phone)

print("\nEmail Addresses:")
for email in emails:
    print(email)

