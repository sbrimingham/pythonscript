# Cherry-O Game
# Scarlett Bouzeid 10/01/19

#variable is cherry


import random # Random spin
spinnerChoice = [-1,-2,-3,-4,2,2,10]
spinIndex = random.randrange(0,len(spinnerChoice))
spinResult = spinnerChoice[spinIndex] # This is the output
print spinResult



turnsToWin = []

for i in range(100): 
    turns = 0
   
    cherryOnTree = 10
    while cherryOnTree > 0:
        spinIndex = random.randrange(0,len(spinnerChoice))
        spinResult = spinnerChoice[spinIndex] 
        # print "You spun", spinResult
        cherryOnTree = spinResult + cherryOnTree # Could also use cherryOnTree += spinResult
        if cherryOnTree > 10: # These conditions constrain the cherry amounts to only 0-10
            cherryOnTree = 10
        elif cherryOnTree < 0:
            cherryOnTree = 0
        
    
        turns += 1 # Every spin needs to add 'turns' by 1, should use turn += 1 in a for/while loop
        print "You spun ", turns, "times."
    turnsToWin.append(turns)
print turnsToWin
print sum(turnsToWin)/len(turnsToWin) 
print "It took an average of", sum(turnsToWin)/len(turnsToWin), "times to win the game out of 100 games."

# find prime number

max = int(input('Enter the max integer: '))
possiblePrime = 2
while possiblePrime < max+1: 
    isPrime = True
    num = 2
    while num < possiblePrime:
        if possiblePrime % num == 0:
            isPrime = False
            break
        num += 1

    if isPrime:
        print(possiblePrime)

    possiblePrime += 1