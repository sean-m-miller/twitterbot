import random

file = open("quotes.txt", "r")
i = file.read(1)
newstring = ""
numlines = 0
x = random.randint(1, 3099)
z = 0
print(numlines)
print("wtf")
print(x)
#line = file[0]
for line in file:
	z+=1
	if z == x:
		for i in range(len(line)):
			while line[i] != "%":
				newstring+=line[i]
			if len(newstring) == 0:
				print("haha loser")

