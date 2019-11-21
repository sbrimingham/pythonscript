#Scarlett Bouzeid 09/30/2019
#Homework exercise 4

#1 %s in print statements
name = "Scarlett"
print("Hello, %s!" % name)
Hello, Scarlett!
name = "Scarlett"
age = 30
print("%s is %d years old." % (name, age))
print("%s is %d years old." % (name, age))


#2 Use /n and /t in print statements
#this skips five lines down
print(5 * "\n")
print "\t I am hungry."

#3 rock, paper, scissors played 100 times
import random

result = []
for i in range(100):
    option = ["R", "P", "S"]
    choice = random.randrange(0,2)
    comp = option[choice]
    print comp
    user = random.randrange(0,2)
    if (user == "R" and comp == "S") or (user == "P" or comp == "R") \
        or (user == "S" and comp == "P"):
            print "User wins!"
            results.append ("W")
    elif (user == "R" and comp == "P") or (user == "P" and comp == "S") \
        or (user == "S" and comp == "R"):
            print "Computer wins!"
            results.append("L")
    else:
        print "Tie"
        results.append("T")
    if len(results) >= 3:
        for i in range(2,len(results)):
            if results[i] == results[i-1] == results[i-2] =="W":
                print "You win three times in a row"

print results