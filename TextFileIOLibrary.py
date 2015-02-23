#! usr/bin/env python3

#	テキストファイルの読み込み書き込みライブラリ


def readTextFile(filepath):
	fin = None
	string = None
	try:
		print("file read : ", filepath)
		# とりあえずこれでファイルを読み込み。(テキストモードで。)
		fin = open(filepath)
	except IOError as err:		# ファイルが読み込めなかった場合
	#	print("except: Cannot open", sys.argv[1])
	#	print("err [%s] msg: [%s]" )
		print(err)
	else:
		
		# 読み込んだファイルの文字列を全部stringに入れる
		string = fin.read()
		# ファイルから読み込んだ文字列の表示
	#	print(string)
	finally:
		if fin is not None:
			# 閉じる処理
			fin.close()

	return string



def writeTextFile(filepath, string, encode):
	fout = None
	try:
		print("file write")
		# 文字コードを指定して保存しなおす
		fout = open(filepath, "w", encoding=encode)
		#fin = open(sys.argv[1])
	except IOError as err:
		print(err)
		print("file write failed.\n")
	else:
		if string is not None:
			fout.write(string)
			print("file write success.\n")
	finally:
		if fout is not None:
			fout.close()
			
	

