# 1 Script from chapter 3

import arcpy
count = arcpy.GetCount_management("floodzone")
print count

# 1 Script from chapter 4

import random
x = random.randint(1,6)
print x:
if x == 6:
    print "You win!"
elif x ==5:
    print " Try again."
else:
    print "You lose!"

# 3 Script to simulate "guess the number" game

import random
n = random.randint(1,10)
guess = int(raw_input("Enter a number between 1 to 10: "))
while n != "guess":
    print
    if guess < n:
        print "guess higher!"
        guess = int(raw_input("Try again. Enter a number between 1 to 10: "))
    elif guess > n:
        print "guess lower!"
        guess = int(raw_input("Try again. Enter a number between 1 to 10: "))
    else:
        print "you guessed it!!"
        break
    print


