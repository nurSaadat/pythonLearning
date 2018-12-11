"""
In this project, we'll create a calculator that can compute the area of the following shapes:

Circle
Triangle
The program should do the following:

Prompt the user to select a shape.
Calculate the area of that shape.
Print the area of that shape to the user.
"""

print "Starting calculator..."
option = raw_input("Enter C for Circle or T for Triangle: ")

if (option == 'C'):
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * radius**2
  print "Area is %s" % str(area)
elif (option == 'T'):
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter hight: "))
  area = 0.5 * base * height
  print "Area is %s" % str(area)
else:
  print "Invalid entry!"
 
print "Exiting calculator..."
