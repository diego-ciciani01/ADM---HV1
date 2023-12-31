# -*- coding: utf-8 -*-
"""Homework_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ga53kvDMfQJNxOedCJbtEujHSL5sfugm

Exercise_1  Say "Hello, World!" With Python
"""

my_string = "Hello, World!"
print(my_string)

"""Exercise_2 Python If-Else

"""

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

if n % 2 != 0 :
    #situation in which n is odd
    print("Weird")
elif n % 2 == 0:
    #situation in which n is even
    if n in range(2,5) or n > 20:
        print("Not Weird")
    elif n in range(6,20) or n == 20:
        print("Weird")

"""Exercise_3  Arithmetic Operators"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())

if a in range(1, 10**10) and b in range(1, 10**10):
    x = a+b
    y = a-b
    z = a*b

    print(x)
    print(y)
    print(z)

"""Exercise_4 Python Division:"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())

x = a//b
y = a/b
print(x)
print(y)

"""Exercise_5 Loops"""

if __name__ == '__main__':
    n = int(input())

if n in range(1,20) or n == 20:
    for i in range(0,n):
        print(i**2)

"""Exercise_6 Write a function"""

def is_leap(year):
    leap = False

    if year in range(1900, 10**5):
        # Write your logic here
        if year % 4 == 0:
          leap = True
          if year % 100 == 0:
            leap = False
            if year %400 == 0:
              leap = True

    else:
        return

    return leap

year = int(input())
print(is_leap(year))

"""Exercise_7 Print Function"""

if __name__ == '__main__':
    n = int(input())
l = []
if n in range(1,150):
  for i in range(1,n+1):
    print(i, end="")

"""Exercise_8 Basic Data Types List"""

if __name__ == '__main__':
    N = int(input())

my_list = []

for j in range(N):
  comand = input().split()
  action = comand[0]

  if action == "insert" :
    i = int (comand[1])
    e = int (comand[2])
    my_list.insert(i, e)
  elif action == "print" :
    print(my_list)
  elif action == "remove" :
    e = int (comand[1])
    my_list.remove(e)
  elif action == "append":
    e = int(comand[1])
    my_list.append(e)
  elif action == "sort":
    my_list.sort()
  elif action == "pop":
    my_list.pop()
  elif action == "reverse":
    my_list.reverse()

"""Exercise_9 Basic Data Types Tuple

"""

n = int(input())
my_list = []
integers =  list(map(int, input().split()))

tuple_of_integers = tuple(integers)

hash_value = hash(tuple_of_integers)

print(hash_value)

"""Exercise_10 Basic Data Finding the percentage

"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    if n in range(2,10):
      for _ in range(n):
          name, *line = input().split()
          scores = list(map(float, line))
          res = all(ele >= 0 and ele <= 100 for ele in scores)
          if res == True:
            student_marks[name] = scores
          else:
            break
      #inserisci comando
      query_name = input()
      sum   = 0.00
      for d in student_marks[query_name]:
        sum += d

      print(format(sum/3, '.2f'))

"""Exercise_11 Basic Data Nested List"""

if __name__ == '__main__':
    n = int(input())
    my_records = []
    if n in range(2,6):
      for _ in range(n):
          my_list = []
          name = input()
          score = float(input())
          my_records.append([name, score])
    #compressione di lista
    scores = set([score for name, score in my_records])
    second_lowest = sorted(scores)[1]

    # second list student with second lowest grade
    second_lowest_students = [name for name, score in my_records if score == second_lowest]
    second_lowest_students.sort()

    for student in second_lowest_students:
      print(student)

"""Exercise_12 Basic Data Nested List"""

if __name__ == '__main__':
    n = int(input())
    my_list= []
    if n in range(2,11):
      data =  set(map(int, input().split()))
      if len(data) in range(-100, 101):
        my_list = [i for i in data]
        my_list.sort()
        print(my_list[-2])

"""Exercise_13 Strings SWAP cASE"""

def swap_case(s):
    return

if __name__ == '__main__':
  text = str(input())
  my_list = []
  if len(text) in range(0,1001):
    for letter in text:
      my_list.append(letter)

text

"""Exercise_20 Sets Introduction to **Sets**"""

def average(array):
    # your code goes here
    heights = set(array)
    avg = sum(heights)/len(heights)
    out= "{:.3f}".format(avg)
    return out
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

"""Exercise_21 Sets Symmetric Difference"""

M = int(input())
set_A = set(map(int, input().split()))
N = int(input())
set_B = set(map(int, input().split()))

# Calculate symmetric difference and sort
symmetric_diff = sorted(set_A.symmetric_difference(set_B))

for element in symmetric_diff:
    print(element)

"""Exercise_22 Set.add()"""

n = int(input())
my_list = []
if n in range(0, 1000):
  for number in range(0,n):
    country = str(input())
    my_list.append(country)

  countries = set(my_list)
  print(len(countries))

"""Exercise_22 Set .discard(), .remove() & .pop()"""

n = int(input())
s = set(map(int, input().split()))

num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))

"""Exercise_23 Set .union() Operation

"""

n =  int(input())
roll_student_n = set(map(int, input().split()))
b = int(input())
roll_student_b = set(map(int, input().split()))

total_student= len(roll_student_n.intersection(roll_student_b))
print(total_student)

"""Exercise_23 Sets  Set .difference() Operation"""

n =  int(input())
roll_student_n = set(map(int, input().split()))
b = int(input())
roll_student_b = set(map(int, input().split()))

total_student= len(roll_student_n.difference(roll_student_b))
print(total_student)

"""Exercise_24 Sets Set .symmetric_difference() Operation"""

n =  int(input())
roll_student_n = set(map(int, input().split()))
b = int(input())
roll_student_b = set(map(int, input().split()))

total_student= len(roll_student_n.symmetric_difference(roll_student_b))
print(total_student)

"""Exercise_24 Sets Set Mutations"""

n = int(input())
s = set(map(int, input().split()))
num_operations = int(input())

for _ in range(num_operations):
    operation, num_elements = input().split()
    other_set = set(map(int, input().split()))

    if operation == "intersection_update":
        s.intersection_update(other_set)
    elif operation == "update":
        s.update(other_set)
    elif operation == "symmetric_difference_update":
        s.symmetric_difference_update(other_set)
    elif operation == "difference_update":
        s.difference_update(other_set)


print(sum(s))

"""Exercise_25 Sets The Captain's Room

"""

group_size = int(input())
room_numbers = list(map(int, input().split()))
room_count = {}

for room in room_numbers:
    if room in room_count:
        room_count[room] += 1
    else:
        room_count[room] = 1

for room, count in room_count.items():
    if count == 1:
        captain_room = room
        break

print(captain_room)

"""Exercise_26 Sets Check Subset"""

num_test_cases = int(input())

for i in range(num_test_cases):
    i = input()
    set_a = set(map(int, input().split()))

    i = input()
    set_b = set(map(int, input().split()))

    is_subset = set_a.issubset(set_b)

    print(is_subset)

"""Exercise_27 Sets No Idea"""

n, m = map(int, input().split())
array = list(map(int, input().split()))
like_set = set(map(int, input().split()))
dislike_set = set(map(int, input().split()))


happiness = 0


for element in array:
    if element in like_set:
        happiness += 1
    if element in dislike_set:
        happiness -= 1


print(happiness)

"""Exercise_28 Date And Time Calendar Module

"""

import calendar
date = input().split()
month, day, year = map(int, date)
day_name = calendar.day_name[calendar.weekday(year, month, day)]
print(day_name.upper())

"""Exercise_29 Date and Time Time Delta"""

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

def time_delta(t1, t2):
    format_str = "%a %d %b %Y %H:%M:%S %z"

    time1 = datetime.strptime(t1, format_str)
    time2 = datetime.strptime(t2, format_str)

    delta = abs(int((time1 - time2).total_seconds()))

    return str(delta)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

"""*Exercise_30 Built-ins Zipped!*"""

n, m = map(int, input().split())

marks = []

for i in range(m):
    subject_marks = list(map(float, input().split()))
    marks.append(subject_marks)

student_marks = zip(*marks)

for student in student_marks:
    average_mark = sum(student) / len(student)
    print("{:.1f}".format(average_mark))



"""Exercise_31 Built_Ins Athletic Sort"""

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    sorted_arr = sorted(arr, key=lambda x: x[k])

    for row in sorted_arr:
        print(" ".join(map(str, row)))

"""Exercise_31 Built_Ins ginortS"""

s = input()

# Define custom sorting functions
def custom_key(char):
    if char.islower():
        return (0, char)
    elif char.isupper():
        return (1, char)
    elif char.isdigit():
        if int(char) % 2 == 1:
            return (2, char)
        else:
            return (3, char)

sorted_string = sorted(s, key=custom_key)

result = "".join(sorted_string)

print(result)

"""Exercise_32 Map and Lambda Function"""

cube = lambda x: x**3

def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

"""Exercise_35 Regex and Parsing Re.split()"""

regex_pattern = r"\W+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

"""Exercise_36 Regex and Parsing Group(), Groups() & Groupdict()"""

s = str(input())

for i in range(len(s)):
  if i == len(s)-1:
    print(-1)
    break
  if s[i].isalnum() and s[i] == s[i+1]:
    print(s[i])
    break
else:
  print(-1)



"""Exercise_37 Regex and Parsing Re.findall() & Re.finditer()"""

import re

save = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)

if save:
    for i in save:
        print(i)
else:
    print(-1)

"""Exercise_38 Regex and Parsing Re.start() & Re.end()"""

def find_substring_indices(string, substring):
    start = 0
    if substring in string :
      while start < len(string):
          start = string.find(substring, start)
          if start == -1:
              break
          end = start + len(substring) - 1
          print(f'({start}, {end})')
          start += 1
    else:
      print(f'({-1}, {-1})')



# Input
string = input()
substring = input()

# Find and print the indices of the substring in the string
find_substring_indices(string, substring)

"""Exercise_38 Regex and Parsing Regex Substitution

"""

import re

line = int(input())
text = ""
for i in range(line):
  changes = re.sub(r"(?<=\s)&&(?=\s)", "and", re.sub(r'\s\|\|\s', ' or ', input()))
  print(changes)

"""Exercise_39 Regex and Parsing Validating Roman Numerals"""

import re
#
regex_pattern = r"(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
print(str(bool(re.match(regex_pattern, input()))))

"""Exercise_39 Regex and Parsing Validating phone numbers"""

import re

regex_pattern = r"^[789]\d{9}$"
n= int(input())
my_arr = []
for i in range(n):
  my_arr.append(str(input()))

for j in my_arr:
  if bool(re.match(regex_pattern, j)) :
    print("YES")
  else :
    print("NO")

"""Exercise_40 Regex and Parsing Validating and Parsing Email Addresses"""

import re
n = int(input())
ok_emails = []
for i in range(n):
   name, email = input().split()
   pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
   if bool(re.match(pattern, email)):
      print(name, email)

"""Exercise_41 Regex and Parsing Hex Color Code"""

import re

n = int(input())
css_code = ""

for i in range(n):
    css_code += input()

color_codes = re.findall(r'{[^}]*}', css_code)

for code in color_codes:
    color_matches = re.findall(r'#([0-9a-fA-F]{3,6})', code)
    for color in color_matches:
        print("#" + color)

"""Exercise_42 Regex and Parsing HTML Parser - Part 1"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

n = int(input())
html_code =""
for i in range(n):
    html_code += input() + "\n"

html_code = html_code.rstrip()
parser = MyHTMLParser()
parser.feed(html_code)

"""Exercise_43 Regex and Parsing HTML Parser - Part 2"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' not in data:
            print('>>> Single-line Comment')
        else:
            print('>>> Multi-line Comment')
        print(data)

    def handle_data(self, data):
        if data.strip():
            print('>>> Data')
            print(data)

n = int(input())
html = ""
for _ in range(n):
    line = input()
    html += line.rstrip() + '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

"""Exercise_43 Regex and Parsing Detect HTML Tags, Attributes and Attribute Values

"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"{tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_startendtag(self, tag, attrs):
        print(f"{tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

n = int(input())
html_code =""
for i in range(n):
    html_code += input() + "\n"

html_code = html_code.rstrip()
parser = MyHTMLParser()
parser.feed(html_code)

"""Exercise_44 Regex and Parsing Validating UID"""

import re

def is_valid_uid(uid):
    if len(uid) != 10:
        return "Invalid"

    if not re.match(r'^(?=(.*[A-Z]){2,})(?=(.*\d){3,})(?!.*[^a-zA-Z0-9]).*$', uid):
        return "Invalid"

    if len(set(uid)) != 10:
        return "Invalid"

    return "Valid"

# Lettura del numero di test cases
t = int(input())

# Elaborazione dei test cases
for i in range(t):
    uid = input()
    result = is_valid_uid(uid)
    print(result)

"""Exercise_45 Regex and Parsing Detect HTML Tags, Validating Credit Card Numbers"""

import re
pattern = r'^[456]\d{3}(-?\d{4}){3}$'


def is_valid_credi_card(number):
  if re.match(pattern, card) and not re.search(r'(\d)\1{3,}', card.replace("-", "")):
    return "Valid"
  else:
    return "Invalid"

n = int(input())

for i in range(n):
  card = input().strip()
  result = is_valid_credi_card(card)
  print(result)

"""Exercise_46 Regex and Parsing Validating Postal Codes"""

import re

regex_integer_in_range = r'^[1-9]\d{5}$'
regex_alternating_repetitive_digit_pair = r'(?=(\d)\d\1)'
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

"""Exercise_47 Regex and Parsing Matrix Script"""



"""Exercise_48 and XML 1 - Find the Score"""

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    score = len(node.attrib)
    for child in node:
        score += get_attr_number(child)
    return score
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

"""Exercise_49 XML2 - Find the Maximum Depth"""

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

"""Exercise X Closures and Decorations Standardize Mobile Number Using Decorators"""

def wrapper(f):
    def fun(l):
        formatted_numbers = []

        for i in l:
            if i[0] == '0' and len(i) > 10:
                i = '+91' + " " + i[1:6] + " " + i[6:]
                formatted_numbers.append(i)
            elif i[0] == '+' and len(i) > 10:
                i = '+91' + " " + i[3:8] + " " + i[8:]
                formatted_numbers.append(i)
            elif i[0] == '9' and len(i) > 10:
                i = '+91' + " " + i[2:7] + " " + i[7:]
                formatted_numbers.append(i)
            elif len(i) == 10:
                i = '+91' + " " + i[:5] + " " + i[5:]
                formatted_numbers.append(i)

        sorted_numbers = sorted(formatted_numbers)
        for i in sorted_numbers:
            print(i)

    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

"""Exercise Y Closures and Decorations

exercise 50 numpy Shape and Reshape
"""

import numpy as np

arr = list(map(int, input().split()))
new = np.array(arr)
reshaped = np.reshape(new, (3, 3))

print(reshaped)

"""Exercise_51 Numpy Transpose and Flatten"""

import numpy as np

d = list(map(int, input().split()))
arr = []

for i in range(d[0]):
    row = list(map(int, input().split()))
    arr.append(row)

new = np.array(arr)
transposed = np.transpose(new)
flattened = new.flatten()

print(transposed)
print(flattened)

"""Exercise_51 Numpy Concatenate"""

import numpy as np

d = list(map(int, input().split()))
arr1 = []
arr2 = []

for i in range(d[0]):
    row = list(map(int, input().split()))
    arr1.append(row)

new1 = np.array(arr1)

for i in range(d[1]):
    row = list(map(int, input().split()))
    arr2.append(row)

new2 = np.array(arr2)

result = np.concatenate((arr1, arr2), axis=0)

print(result)

"""Exercise_52 Numpy Zeros and Ones"""

import numpy as np

d = list(map(int, input().split()))

zeros_array = np.zeros(tuple(d), dtype=int)
ones_array = np.ones(tuple(d), dtype=int)

print(zeros_array)
print(ones_array)

"""Exercise_53 Numpy Eye and Identity"""

import numpy
numpy.set_printoptions(legacy='1.13')

d=list(map(int,input().split()))
print(numpy.eye(d[0],d[1],k=0))

"""Exercise_54 Numpy Array Mathematics"""

import numpy as np
d=list(map(int, input().split()))
arr1=[]
arr2=[]
for i in range(d[0]):
    row=list(map(int,input().split()))
    arr1.append(row)
new1=np.array(arr1,float)
for i in range(d[0]):
    row=list(map(int,input().split()))
    arr2.append(row)
new2=np.array(arr2,float)
print (np.add(arr1,arr2))
print (np.subtract(arr1,arr2))
print (np.multiply(arr1,arr2))
print (np.floor_divide(arr1,arr2))
print (np.mod(arr1,arr2))
print (np.power(arr1,arr2))

"""Exercise_55 Numpy Floor, Ceil and Rint"""

import numpy as np
np.set_printoptions(legacy='1.13')
a=list(map(float,input().split()))
arr=np.array(a, float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))

"""Exercise_56 Numpy Sum and Prod"""

import numpy as np

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
new = np.array(arr)
result = np.prod(np.sum(new, axis=0))

print(result)

"""Exercise_57 Numpy Min and Max"""

import numpy as np

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
np_array = np.array(arr)

min_values = np.min(np_array, axis=1)

result = np.max(min_values)

print(result)

"""Exercise_58 Numpy Mean, Var, and Std"""

import numpy as np
n,m=map(int,input().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))

arr=np.array(l)
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print(round(np.std(arr),11))

"""Exercise_59 Numpy Dot anf Cross"""

import numpy as np

n = int(input())

A = []
B = []

for _ in range(n):
    row = list(map(int, input().split()))
    A.append(row)

for _ in range(n):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)
result = np.dot(A, B)

# Print the result
print(result)

"""Exercise_60 Numpy Inner and Outer"""

import numpy as np

A = np.array(list(map(int, input().split())))
B = np.array(list(map(int, input().split())))

inner_product = np.inner(A, B)

outer_product = np.outer(A, B)

print(inner_product)
print(outer_product)

"""Exercise_61 Numpy Polynomials"""

import numpy as np

coefficients = list(map(float, input().split()))

x = float(input())

result = np.polyval(coefficients, x)

print(result)

"""Exercise_62 Numpy Linear Algebra"""

import numpy as np

n = int(input())

matrix = []

for _ in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

matrix = np.array(matrix)

determinant = round(np.linalg.det(matrix), 2)

print(determinant)

"""Exercise_2_1 Birthday Cake Candles"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    from collections import Counter

    a = Counter(candles)
    return a[max(a)]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

"""Exercise_2_2 Kangaroo"""

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 in range(0, 10000) and x2 in range(0,10000):
      if v1 in range(1,10000) and v2 in range (1, 10000):
        my_list = range(10000)
        meet = "NO"
        i = 0
        #while(i <= len(my_list)):
        while(not(my_list[x1]+v1 == my_list[x2]+v2)):
          if x1 >= len(my_list) or x2 >= len(my_list) or x1+v1 >= len(my_list) or x2+v2 >= len(my_list):
            break
          x1 = my_list[x1+v1]
          x2 = my_list[x2+v2]
          if my_list[x1]+v1 == my_list[x2]+v2:
            meet = "YES"
            break
          #i +=1
        return meet

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

   #fptr.write(result + '\n')

    #fptr.close()
    print(result)

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
      if x1 == x2:
        return "YES"
      else:
        return "NO"
    elif (x2 - x1) % (v1 - v2) == 0 and (x2 - x1) // (v1 - v2) >= 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

   #fptr.write(result + '\n')

    #fptr.close()
    print(result)

"""Exercise_2_3 Viral Advertising"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    cumulate = 2
    shared = 5
    like = 2
    for i in range(1,n):

      shared = int((shared)/2) * 3
      like = int(shared/2)
      cumulate += like

    return math.trunc(cumulate)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

"""Exercise_2_4 Recursion Recursion Digit Sum"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
   # if int(n) in range(1,10): i can't use it, because big number cause exception
    if len(n) == 1:
      return n

    else:
      my_sum = sum(list(map(int, n)))
      p = str(my_sum)*k

      return superDigit(p,1)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

"""Exercise_2_6 Sorting Insertion Sort - Part 2"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(1, n):
            k = arr[i]
            j = i - 1
            while j >= 0 and k < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = k
            print(" ".join(map(str, arr)))



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

"""Exercise String Swap Case"""

def swap_case(s):
    l = s.lower()
    u = s.upper()
    s_new = ""
    for i in range(len(s)):
        if s[i] == l[i]:
            s_new += s[i].upper()
        elif s[i] == u[i]:
            s_new  += s[i].lower()
        else:
          s_new += s[i]
    return s_new

"""Exercise String String Split and Join"""

def split_and_join(line):
    line= line.split(" ")
    line= "-".join(line)
    return line

if _name_ == '_main_':
    line = input()
    result = split_and_join(line)
    print(result)

"""Exercise String What's Your Name?"""

#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

"""Exercise String Mutations"""

def mutate_string(string, position, character):
    l=list(string)
    l[position]= character
    l = "".join(l)
    return l

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

"""Exercise String Text Alignment"""

odd = False
while (odd == False):
    thick = int(input())
    if (thick%2 != 0):
        odd = True
    else:
        print("Please write an odd number:")
p = 'H'

for i in range(1, thick+1):x
    print((p*(i*2-1)).center(((thick-1)*2)+1," "))
for i in range(thick+1):
    print((p*thick).center(thick*2)+(p*thick).center(thick*6))
for i in range((thick+1)//2):
    print((p*thick*5).center(thick*6))
for i in range(thick+1):
    print((p*thick).center(thick*2)+(p*thick).center(thick*6))
j = 0
i = thick
while i>0:
  print((p*(i*2-1)).rjust(thick*6-1-j))
  j+=1
  i-=1

"""Exercise String Text Alignment"""

thickness = int(input())
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))


for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))



for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))


for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))


for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

"""Exercise String Text Wrap"""

import textwrap

def wrap(string, max_width):
    wrapped_text = textwrap.fill(string, max_width)
    return wrapped_text

if __name__ == '__main__':
    string = input()
    max_width = int(input())
    result = wrap(string, max_width)
    print(result)

"""Exercise String Designer Door Mat"""

N, M = map(int, input().split())
half = (N - 1) // 2

for i in range(half):
    pattern = "-" * (3 * (half - i)) + ".|." * (2 * i + 1) + "-" * (3 * (half - i))
    print(pattern.center(M, "-"))

welcome_line = "WELCOME".center(M, "-")
print(welcome_line)

for i in reversed(range(half)):
    pattern = "-" * (3 * (half - i)) + ".|." * (2 * i + 1) + "-" * (3 * (half - i))
    print(pattern.center(M, "-"))

"""Exercise String Capitalize"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.

def solve(s):
    l_before = s.split(' ')
    l_after =[]
    for i in range(len(l_before)):
        l_after.append(l_before[i].capitalize())
    k = ' '.join(l_after)
    return k
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

"""Exercise Collection DefaultDict Tutorial"""

from collections import defaultdict

def word_indices_in_groups(n, m, group_a, group_b):
    word_indices = defaultdict(list)

    for i in range(n):
        word_indices[group_a[i]].append(i + 1)

    for word in group_b:
        if word in word_indices:
            indices = word_indices[word]
            print(" ".join(map(str, indices)))
        else:
            print(-1)

# Input
n, m = map(int, input().split())
group_a = [input().strip() for _ in range(n)]
group_b = [input().strip() for _ in range(m)]

# Call the function to find word indices
word_indices_in_groups(n, m, group_a, group_b)

"""Exercise Collection Collections.deque()"""

from collections import deque

# Create an empty deque
d = deque()

# Number of operations
n = int(input())

for _ in range(n):
    operation = input().split()

    if operation[0] == 'append':
        d.append(int(operation[1]))
    elif operation[0] == 'appendleft':
        d.appendleft(int(operation[1]))
    elif operation[0] == 'pop':
        d.pop()
    elif operation[0] == 'popleft':
        d.popleft()

# Print the space-separated elements of the deque
print(*d)

