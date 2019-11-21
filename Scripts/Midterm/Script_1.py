# Scarlett Bouzeid
# Advanced GIS
# Midterm Exam 10/08/2019

# Question 1
 
num = 0
while num >= 0:
    num = int(raw_input("Please enter a temperature"))
    if num > 100:
        print "It is hot."
    elif num >=61 and num<= 99:
        print "It is just right!"
    elif num <= 60:
        print "It is too cold."

print "Good bye!"

# Question 2 - Script to generate 100 random numbers

import random

choice = random.randrange(1,1000)
sumEven = 0
sumOdd = 0
num = 0
for num in range(0,100):
    num = random.randrange(1,1000)
    if (num % 2) == 0:
        sumEven += 1
    else:
        sumOdd += 1

print "Out of 100 Random Numbers, %d were even and %d were odd" %(sumEven,sumOdd)


# 3 Rock, paper, scissor

choice = ["rock", "Paper", "Scissors"]
result = []
var= True
while var:
    User_input = input("Rock, Paper, or Scissors?")
    import random
    comp_index= random,randrange(0,len(choice))
    comp_choice= choice[comp_index]
    print "Computer chose ", comp_choice,"."
    if comp_choice ++ User_input:
        print "its a tie."
    elif (comp_choice,User_input) in {("Rock", "Paper")or("Paper","Scissors"),("Scissor","Rock")}:
        print "you win!"
    else:
        print "You lose."
        results.append("1")
    for i in range(2,len(result)):
        if result[i-2]==result[i-1]==result[i]=="1":
            print "You lose!"
            var= False
        
# I am not sure why #3 will not run 