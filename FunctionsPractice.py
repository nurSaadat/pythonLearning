def is_even(x):
  if (x % 2 == 0):
    return True
  else:
    return False
    
def is_int(x):
  if x - int(x) == 0:
    return True
  else:
    return False
    
def digit_sum(n):
  total = 0
  while n > 0:
    temp = n % 10
    n = n / 10
    total += temp    
  return total
  
def factorial(x):
  fact = 1
  while x > 0:
    fact *= x
    x -= 1
  return fact
  
def is_prime(x):
  if (x < 2):
    return False
  div = x - 1
  while div > 1:
    if (x % div == 0):
      return False
    div -= 1
  else: 
    return True
    
def reverse(text):
  rev = ""
  i = len(text)
  while i != 0:
    c = text[i-1]
    rev = rev + c
    i -= 1
  return rev
  
def anti_vowel(text):
  i = 0
  result = ""
  while i < len(text):
    if text[i] == "a" or text[i] == "A" or text[i] == "e" or text[i] == "E" or text[i] == "i" or text[i] == "I" or text[i] == "o" or text[i] == "O" or text[i] == "u" or text[i] == "U":
      div=5
    else:
      result = result + text[i]    
    i += 1
  return result
  
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  word = word.lower()
  total = 0
  c = word[0]
  print score[c]
  for i in range(0, len(word)):
    c = word[i]
    print c
    total = total + score[c]
  return total
  
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
    
def count(sequence, item):
  counter = 0
  for element in sequence:
    if element == item:
      counter += 1
  return counter
  
def purify(lst):
  pure = []
  for element in lst:
    if (element % 2 == 0):
      pure.append(element)
  return pure
  
def product(lst):
  prod = 1
  for element in lst:
    prod = prod * element
  return prod

def median(lst):
  lst = sorted(lst)
  if len(lst) % 2 == 1:
    x = len(lst)/2
    return lst[x]
  else:
    x = len(lst)/2
    return (float(lst[x]+lst[x-1])/2)
