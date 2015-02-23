#! usr/bin/env python3
# ↑はshebang. windowsでは機能しない。

print("ハロー", "ワールド!")

countries = ["Denmark", "Finland", "Norway", "Sweden"]

for country in countries:
	print(country)

i = 0
num = len(countries)
print(num)
while (i < num):
	country2 = countries[i]
	print(country2)
	i+=1

print("Type integers, each followed by Enter; or just Enter to finish")

total = 0
count = 0

while True:
	line = input()
	if line:
		try:
			number = int(line)
		except ValueError as err:
			print(err)
			continue
		total += number
		count += 1
	else:
		break

if count:
	print("count =", count, "total =", total, "mean =", total/count)

