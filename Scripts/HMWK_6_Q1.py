# 2 Finding largest number in list

mylist = [1,2,3,4,5,6]
mylist.remove(max(mylist))
print max(mylist)

# 3 Finding absolute value

n = input("integer?")
if n<0:
    print "The absolute value of", n, "is", -n
else:
    print "The absolute value of", n, "is", n

# 4 Asks for numbers and prints if the number is even or odd

num = int(input("What is the number?: "))
if (num % 2) == 0:
 	print "%d is an even number" % (num)
else:
 	print "%d is an odd number" % (num)
 	
# 5 Finds average value of numbers

num = int(input('How many numbers: '))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)

# 6 Averages number with each new number added

print "Welcome to the Average Calculator, please insert a number"
currentAverage = 0
numofnums = 0
while True:
    newNumber = int(input("New number: "))
    numofnums = numofnums + 1
    currentAverage = (round((((currentAverage * (numofnums - 1)) + newNumber) / numofnums), 3))
    print "The current average is " + str((round(currentAverage, 3)))

# 7 Calculated factorial
num = int(raw_input("Enter number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = i * factorial
print "Factorial of", num, "is", factorial    

# 8 List Items and loop

import math
singer_name = ["John", "Paul", "Ringo", "George"]
Rank = ["First", "Second", "Third", "Fourth"]
x=0
y=0
while x < 4:
 	print Rank[x], "Beatles member is", singer_name[y]
 	x+=1
 	y+=1

# 9 generate random number

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






