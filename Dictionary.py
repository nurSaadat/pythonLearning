inventory = {
  'gold' : 500,
  'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
  'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]
  
total = 0
for x in prices:
  cost = prices[x] * stock[x]
  print "%s" % cost
  total += cost
  
print "%s" % (total)

shopping_list = ["banana", "orange", "apple"]

def compute_bill(food):
  total = 0
  for item in food:
    if (stock[item] > 0):
      total += prices[item]
      stock[item] -= 1
  return total

print "%d" % total
