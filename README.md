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

### 12/12/2018
* functions
```python
def name(arguments):
	#function body
	return
```
* function should be declared earlier than first used
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
* when passing arguments without names they will be assigned in defined order
