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
	while (valid == 0):
		valid = 1
		areLion = input ("Are you a lion? Y/N")
		if areLion == 'y' or areLion == 'Y':
			print("Glad to see a fellow lion of culture round these parts")
		elif areLion == 'n' or areLion == 'N':
			print("TO THE BALLPIT WITH YOUUUU")
		else:
			valid = 0
			print("Invalid input")
		
	
