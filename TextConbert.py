#! usr/bin/env python3

#	文字コードを変換するスクリプト
#	とりあえず見境なしにファイル読み込んでBOM付きUTF-8にするところまでできた。


import sys
import os
import TextFileIOLibrary as textioLib	# モジュール名を自分で定義しなおしながら読み込み



# 作業を行うパスを取得
executedir = sys.argv[1]

# 指定のパス内のファイル、ディレクトリをさらう
for filename in os.listdir(executedir):
	# 拾ったファイル名とパスを結合する
	fullpath = os.path.join(executedir, filename)
	print(fullpath)
	#　テキスト読み込み
	text = textioLib.readTextFile(fullpath)

	# テキスト書き込み
	textioLib.writeTextFile(fullpath, text, "utf-8-sig")


"""
以下は指定したディレクトリ内のサブフォルダを含む全ファイルに対して行いたい場合に使える。
for root, dirs, files in os.walk(executedir):
	for file in files:
		fullpath = os.path.join(root, file)
		print(fullpath)
		#　テキスト読み込み
		text = textioLib.readTextFile(fullpath)

		# テキスト書き込み
		textioLib.writeTextFile(fullpath, text, "utf-8-sig")
"""