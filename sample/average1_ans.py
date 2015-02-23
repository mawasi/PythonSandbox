
numbers = []
sum = 0
lowest = None
highest = None
while True:
	try:
		line = input("enter a number or push Enterkey to finish:")
		if not line:
			break
		number = int(line)
		numbers.append(number)
		sum += number
		if lowest is None or lowest > number:
			lowest = number
		if highest is None or highest < number:
			highest = number
	except ValueError as err:
		print(err)

print("numbers:", numbers)
print("count =", len(numbers), "sum =", sum, "lowest =", lowest, 
		"highest =", highest, "mean =", sum/len(numbers))
