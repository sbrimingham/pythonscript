# number 5 
num = int(input('How many numbers: '))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)

# number 8

import math
singer_name = ["John", "Paul", "Ringo", "George"]
Rank = ["First", "Second", "Third", "Fourth"]
x=0
y=0
while x < 4:
 	print Rank[x], "Beatles member is", singer_name[y]
 	x+=1
 	y+=1

# 9

import random 
score = random.randrange(0,100)
if 90 <= score <= 100:
 	print "your score is", score, "and grade is A"
elif 80 <= score <= 89:
 	print "your score is", score, "and grade is B"
elif 70 <= score <= 79:
 	print "your score is", score, "and grade is C"
elif 60 <= score <= 69:
 	print "your score is", score, "and grade is D"
elif 60 < score:
 	print "your score is", score, "and grade is F"

# 3 Create a script that asks for a number then print the absolute value of that number

num = int(raw_input("What is the number?: "))
if num < 0:
 	print abs(num)
else:
 	print num

# 4  Create a script that asks for a number then prints if it is even or odd number(hint: use %  to evaluate)


num = int(input("What is the number?: "))

if (num % 2) == 0:
 	print "%d is an even number" % (num)
else:
 	print "%d is an odd number" % (num)

# 5 Create a script that prints the average value of user inputs of numbers.
#    In your script you can ask users how many numbers will be entered and print the average of entered numbers.

num = int(input("How many numbers: "))
total_sum = 0
for n in range(num):
    numbers = float(input("Enter number: "))
    total_sum += numbers

avg = total_sum/num
print "Average of", num, "numbers is: ", avg

# 6 Averages number with each new number added

print "Welcome to the Average Calculator, please insert a number"
currentAverage = 0
numofnums = 0
while True:
    newNumber = int(input("New number: "))
    numofnums = numofnums + 1
    currentAverage = (round((((currentAverage * (numofnums - 1)) + newNumber) / numofnums), 3))
    print "The current average is " + str((round(currentAverage, 3)))

# 7 Factorials

num = int(raw_input("Enter your number:"))

factorial = 1
for i in range(1,num+1):
    factorial = i * factorial
print "Factorial of",num, "is", factorial