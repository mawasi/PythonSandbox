
import random

# ユーザーからの整数の入力を取得する
# msg		ユーザー入力時に表示するメッセージ
# minimum	整数の最小値を指定
# default	無入力だった場合のデフォルト整数値
def get_int(msg, minimum, default):
	while True:
		try:
			line = input(msg)
			if not line and default is not None:
				return default
			i = int(line)
			if i < minimum:
				print("must be >=", minimum)
			else:
				return i
		except VauleError as err:
			print(err)




# 以下メイン
rows = get_int("row:", 1, None) # デフォルト値なし
columns = get_int("columns:", 1, None) # デフォルト値なし

minimum = get_int("minimums (or Enter for 0):", -10000, 0)

maximumdefault = 10000
# 最大デフォルト値が最小値より小さかった場合の対処
if maximumdefault < minimum:
	maximumdefault = 2* minimum

maximum = get_int("maximum (or Enter for " + str(maximumdefault) + "):", minimum, maximumdefault)

print("gatherInfo Complete")

row = 0
while row < rows:
	line = ""
	column = 0
	while column < columns:
		i = random.randint(minimum, maximum)
		s = str(i)
		while len(s) < 10:
			s = " " + s	# 前にスペースを挿入
		line += s
		column += 1
	print(line)
	row += 1
	
	
