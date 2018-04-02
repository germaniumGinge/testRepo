print("Testing out GIT")

teststr = ""

while (1):
	teststr = input ("How hungry are you on a scale of 1 to 10? ")
	if teststr == "quit":
		quit()
	else:
		print("You are exactly " + teststr + " hungry.")
