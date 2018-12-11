# pythonLearning
My first programs on Python

* module names should be lowercase with underscore (_) between words

### 5/12/2018
* to get input type `input("some input, please")`

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
`for i in range(10):`
`for i in 2,3,5:`

* range() function
`range(start = 0, to, step = 1)`
```python
for i in range(n):
	print('*' * n)
```
* print() function

  `print() #by default goes on the next line`
  `print(end = '') #will not go on the next line`

* list comprehension
`a, b =(int(i) for i in input().split())`

* strings are not mutable

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
* string functions
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

* slicing
```python
dna[1:-1:2]
dna[start: finish: step]
dna[::-1] #reverse
```

* lists
```python
students = ['Dave', 'John', 'Rose', 'Jade']
for student in students:
	print('Hello ' + student + '!')
#same indexation as strings
len(students) #4
#can add and mutiply. original list don't change
fruit = [kiwi, apple, orange, pineapple]
newlist = students + fruits
newstudents = students * 4
#adding elements can be done 
```
