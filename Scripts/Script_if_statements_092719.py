>>> print "How many words have you written for your term paper?"
How many words have you written for your term paper?
>>> mydata = (raw_input("How many words have you written?"))
>>> if mydata > 1499:
... 	print ("Sorry you must stay home and work on your term paper.")
... 	
Sorry you must stay home and work on your term paper.

>>> if mydata < 1500:
... 	print ("Great, you've done your homework. Enjoy the beach!")
... 	
>>> 
>>> print ("How many bags of leaves did you fill this month?")
... 
How many bags of leaves did you fill this month?
>>> bags = int(raw_input("How many bags?"))
>>> if bags < 10:
... 	print "Great you made %s" % (bags*3)
... 	
>>> if bags > 10:
... 	print "Great, you made %s" %  (20+bags*3)
... 	
>>> 
>>> w = float(input("What is you GPA?"))
>>> if w < 3.0:
... 	print "Sorry, you do not get a game system"
... elif w >= 3.0 and w < 3.5:
... 	print "You will get a Wii!"
... elif w >=3.5 and w < 3.8:
... 	print "You will get a Kinect!"
... else:
... 	print "You will get a Playstation 3!"
... 	
You will get a Wii!
>>> 
>>> 
>>>
>>> print ("Did you bring your permission slip? (yes/no)")
Did you bring your permission slip? (yes/no)
>>> answ = (raw_input("Did you bring permission slip?"))
>>> if answ ("no"):
... 	print ("Sorry, you can't go.")
... elif answ ("yes"):
... 	print ("What year did prohibition end?")
... if w == "yes":
>>> 
>>> w = input("Did you bring your permissio slip?")
>>> Q = raw_input("What year did prohibition end?")
>>> if w == "yes":
... 	print "Great, now answer a question"
... 	if Q == "1933":
... 		print "Great, you are going to the history museum."
... 	else:
... 		print "Great, you will go to the art museum."
... 		
>>> 
>>> 
>>> gpa = float(input("What is your GPA?"))
>>> sat = int(input("What is you SAT score?"))
>>> if gpa >= 3.0 and sat >= 1100:
... 	print "You qualify for the scholarship!"
... else:
... 	print "Sorry, you do not qualify for the scholarship"
... 	
You qualify for the scholarship!
>>> 
>>> gpa = float(input("What is you GPA?"))
>>> sat = int(input("What is your SAT score?"))
>>> if gpa >=3.6 or sat >=1250:
... 	print "Great, you qualify for an Honors Diploma!"
... else:
... 	print "Sorry, you do not qualify"
... 	
Great, you qualify for an Honors Diploma!
>>> 
>>> 
>>> run1 = raw_input("What is your name?")
>>> run2 = raw_input("What is your name?")
>>> run3 = raw_input("What is your name?")
>>> time1 = float(input("What was your time?"))
>>> time2 = float(input("What was your time?"))
>>> time3 = float(input("What was your time?"))
>>> if float(time1) < float (time2) and float (time1) < float(time3):
... 	print "Scarlett is the winner!"
... elif float(time2) < float (time1) and float(time2) < float(time3):
... 	print "Bonnie is the winner!"
... else:
... 	print "Eva is the winner!"
... 	
Scarlett is the winner!
>>> 