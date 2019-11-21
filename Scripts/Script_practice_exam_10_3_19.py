# Scarlett Bouzeid
# practice exam 10/03/19

# 2 Factorial of numbers
math.factorial(5)
120

>>> num = 5 # other way to calculate factorial
>>> factorial = 1 * 2 * 3 * 4 * 5
>>> print "Factorial of ", num, "is", factorial
Factorial of  5 is 120
>>> for i in range(1,6):
... 	print i	
... 	factorial = i * factorial
... 	
1
2
3
4
5
>>> print factorial
14400

#num = 5 # other way to calculate factorial
#factorial = 1 * 2 * 3 * 4 * 5
factorial = 1
for i in range(1,6): #i is new variable
... 	factorial = i * factorial
print factorial

# 1 average
num_list = [1,2,3]
num_value = int(raw_input("3:")) # ask user for inputf

                      