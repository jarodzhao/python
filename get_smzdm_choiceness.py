from smzdm.faxian import FaxianItem as Item
import sqlite3
import time, random
import bs4

def test():
	for i in range(5):
		if i > 2:
			print('aaaaa')
			return i
			break
		print(str(i) + '...')
	print(str(i) + '---')


if __name__ == '__main__':
	a = True
	print(test())
