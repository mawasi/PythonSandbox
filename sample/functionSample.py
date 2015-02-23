


#関数化
def get_int(msg):
	while True:
		try:
			i = int(input(msg))
			return i
		except ValueError as err:
			print(err)


#関数より先にこの処理書くと関数の定義がされてないので後に書く
age = get_int("enter youer age: ")

print(age)

