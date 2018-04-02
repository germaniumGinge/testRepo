#!usr/bin/python3

def strToNum(numIn):
	try:
		return int(numIn)
	except ValueError:
		return float(numIn)
	except:
		print("Error converting string")
		return 0


print("Testing out GIT")

teststr = ""

while (1):
	teststr = input ("How hungry are you on a scale of 1 to 10? ")
	if teststr == "quit":
		quit()
	else:
		testNum = strToNum(teststr)
		
	if testNum > 7:
		print("You are extremely hungry. Eat a butterfinger")
	elif testNum > 5:
		print ("You are significantly hungry. Eat some samosa.")
	elif testNum > 3:
		print("You are mildly peckish. Eat a Snickers.")
	else:
		print("You are not hungry enough, scrub.")
	valid = 0
	lion = input("Are you a lion? Y/N ")
	while not valid:
		if lion == 'Y' or lion == 'y':
			valid = 1
			print("Glad to see a fellow lion of culture around these parts")
		elif lion == 'N' or lion == 'n':
			valid = 1
			print("Then you will be banished to AN EXTRA HOUR IN THE BALL PIT")
		else:
			print("This is a serious question, Jeremy")
		
