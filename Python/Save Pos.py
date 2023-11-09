file = open("L_log.txt", "r")
data = file.read()
sides = data.split("\n")
sides.pop()
print(sides)
file.close()

file = open("R_log.txt", "w")
items = ['123456','123456','123456','123456','123456','123456']
for item in items:
	file.write(item+"\n")
file.close()