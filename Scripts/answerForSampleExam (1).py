#1
# Average number

num_list = []  # blank list
num_value = int(input("How many numbers you want to add?:"))  # ask user for input
for x in range(1, num_value+1):  # using for loop to include numbers in the list from user input
    num = int(input("enter your number here:"))  # ask user for input
    num_list.append(num)  # append user input in the blank list
print "Average of your numbers is",sum(num_list)/float(len(num_list))  # if you don't consider length of list as a float, it will round up the number.

#2
# factorial number
num = int(raw_input("Enter your number:"))

factorial = 1
for i in range(1,num+1):
    factorial = i * factorial
print "Factorial of",num, "is", factorial


#3
# Beatles

singer_name = ["John Lennon", "Paul McCartney", "Ringo Starr", "George Harrison"]  # list of singer name
Rank = ["First","Second","Third", "Fourth"]  # list of ranks
x=0  # variable for singer name list
y=0  # variable for rank list
while x < 4:  # while loop within number range of singer name and rank
        print Rank[x], "member is", singer_name[y]  # indexing rank and singer name from the lists
        x+=1  # continuing while loop
        y+=1

#4
# letter grade

import random
score= random.randrange(0,100)  # Generates random number within range 0 to 100
# Applying condition to obtain letter grade as a random score generates and print both score and letter grade.
if 90 <= score <= 100:
    print "your score is", score, "and your letter grade is A"
elif 80 <= score < 90:
    print "your score is", score, "and your letter grade is B"
elif 70 <= score < 80:
    print "your score is", score, "and your letter grade is C"
elif 60 <= score < 70:
    print "your score is", score, "and your letter grade is D"
elif 60 < score:
    print "your score is", score, "and your letter grade is F"

