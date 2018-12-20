# pythonLearning
My first programs on Python

* module names should be lowercase with underscore (_) between words

### 5/12/2018
* to get input type 
```python
input("some input, please")
```
```python
X - hours / Y - minutes ==> Find total minutes
X = int(input())
Y = int(input())
print(X*60 + Y)
```

### 9/12/2018
```python
print(a, end = " ") # will print with space in the end
a,b = input().split() # if there is space or anything between a and b they will be sepaprated
a = int(a)
b = int(b)
```

### 10/12/2018
* for-cycle 
```python
for i in range(10):
for i in 2,3,5:
```
* range() function
```python
range(start = 0, to, step = 1)
```
```python
for i in range(n):
	print('*' * n)
```
* print() function
  ```python
  print() #by default goes on the next line
  print(end = '') #will not go on the next line
  ```
* list comprehension
```python
a, b =(int(i) for i in input().split())
```
* strings are not mutable
```python
s = abcd
s[1] = e #will result in error
```
* print all characters in c
```python
for c in genome:
	print(c)
```
* count all 'C' in genom
```python
genome = input()
print(genome.count('C')) 
```
### *string functions*
```python
s.count(p) #returns how many times p is in s
s.lower()
s.upper()
s.find(p) #returns index of p in s (-1 if doesn't exist)
	if p in s: #check if here
s.replace(a, b) #replace a by b. original string will not change
#can use all together
s.upper().count('gt'.upper())
```
### *slicing*
```python
dna[1:-1:2]
dna[start: finish: step]
dna[::-1] #reverse
```
### *lists*
* empty list
```python
students = []
```
```python
students = ['Dave', 'John', 'Rose', 'Jade']
for student in students:
	print('Hello ' + student + '!')
students[1] #John
students[::-1] #reverse list
len(students) #4
```
* lists can be added and mutiplied. Original lists don't change
```python
fruit = [kiwi, apple, orange, pineapple]
newlist = students + fruits
newstudents = students * 4
```
* adding lists can be done in two ways
```python
fruit.append('pear')
fruit += 'pear'
```
* inserting element at certain position
```python
fruit.insert(1, 'plum')
```
* deleting element
```python
students.remove('Jade') #will return string without 'Jade'
del students[0] #will remove 'Dave'
```
* look up for the element
```python
students = ['Dave', 'John', 'Rose', 'Jade']
if 'Dave' in students:
	print("Dave is here")
if 'Dirk' not in students:
	print("Dirk is not here")
	
ind = students.index('Rose') #returns index
ind = students.index('Roxy') #error
```
* sorting list
```python
ordered_students = sorted(students) #original list will not change
students.sort() #original list changed
students.min()
students.max()
```
* reversing list
```python
students.reverse()
rev_students = reversed(students)
students[::-1]
```
* lists are mutable
```python
a = [1, 2, 3]
b = a
a[1] = 4 #List object is shared 
# a = [1, 4, 3]
# b = [1, 4, 3]
b[2] = 5
# a = [1, 4, 5]
# b = [1, 4, 5]
```
* generating list
```python
a = [0] * 5 #[0, 0, 0, 0, 0]
#list comprehension
a = [0 for i in range(5)] #[0, 0, 0, 0, 0]
a = [i*i for i in range(5)] #[0, 1, 4, 9, 16]
a = [int(i) for i in input().split()]

n = 3
a = [[0] * n] * n
a = [[0] * n for i in range(n)]
a = [[0 for j in range(n)] for i in range(n)]
```

### *12/12/2018*
* functions
```python
def name(arguments):
	#function body
	return
```
* *function should be declared earlier than first used*
* arbitrary number of arguments
```python
def min(*a):
	m = a[0]
	for x in a:
		if m > x:
			m = x
	return m
```
* default arguments
```python
def print(a = '', end = '\n'):
	#...

print() #will print empty string and go to next line
```
* *when passing arguments without names they will be assigned in defined order*

### *15/12/2018*
* sets
```python
s = set() #empty set
basket = {'apple', 'orange', 'plum', 'pear'}
'orange' in basket #True
'cherry' in basket #False
s.add(element)
s.remove(element) #if no element then ERROR
s.discard(element) #if no element then NO ERROR
s.clear()
len(s) #number of elements in set
```
* *dictionary - key-value pairs*
* creating dictionary
```python
dict()
{}
d = {'a': 239, 10:100, 'key': 'value'}
print(d['a'])
print(d[10])
```
* operations with dictionaries
```python
dictionary = {...}
key in dictioary #True/False
key not in dictionary #True/False
dictionary[key] = value #assigning
dictionary[key] #if key is not in dictionary then ERROR
dictionary.get(key) #returns value or None
del dictionary[key]
```
* dictionaries
1. are mutable
2. have no order
3. all keys are different
4. keys are immutable

* looking through the dictionary
```python
d = {'C': 12, 'A': 23, 'T': 67, 'G': 18}
for key in d:
	print(key, end = ' ')
for key in d.keys():
	print(key, end = ' ')
for value in d.values():
	print(value, end = ' ')
for key,value in d.items():
	print(key, value, end = ';')
```
### *16/12/2018*
* *files*
* reading from file
```python
inf = open('file.txt', 'r') #open('file.txt')
s1 = inf.readline() #read first line
s2 = inf.readline() #read second line
inf.close()

with open('text.txt') as inf: #automaticly closing file
	s1 = inf.readline()
	s2 = inf.readline()
```
* file functions
```python
s = inf.readline().strip() #taking away special characters
os.path.join('.','dirname','filename.txt')
```
* reading file line-by-line
```python
with open('input.txt') as inf:
	for line in inf:
		line = line.strip()
		print(line)
```
* writing to the file
```python
ouf = open('file.txt', 'w')
ouf.write('Some text\n')
ouf.write(str(25))
ouf.close()

with open('output.txt', 'w') as ouf:
	ouf.write('Some text\n')
	ouf.write(str(25))
```
* modules
```python
import my_module
from my_module import foo
from my_module import *
from my_module import foo as my_foo
```
* requests
```python
import requests

r = requests.get('https://example.com') #GET
print(r.text)

url = 'https://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params = par) #passing parameters
print(r.url) #url GET 

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies = cookies) #sending request to the server
print(r.text)

print(r.cookies['example_cookie_name']) #using cookies from server
```
