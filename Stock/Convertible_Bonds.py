# __author__ = 'litongyang'
# -*- coding: utf-8 -*-

'''
可转债价值计算
'''


class BONDS():
	def __init__(self):
		self.stock_price_now = []
		self.bonds_price_now = []

	def bonds_value(self):
		stock_price = 8.5
		for j in range(0, 20):
			temp = stock_price
			for i in range(0, 10):
				k = float(i / 100.00)
				stock_price += k
				bonds_price = 100 / 8.105 * stock_price
				print stock_price
				print bonds_price
				self.stock_price_now.append(stock_price)
				self.bonds_price_now.append(bonds_price)
				print " "
				stock_price = temp
			stock_price += 0.1
		print self.stock_price_now
		print self.bonds_price_now

	def write_txt_fun(self):
		fl = open("/Users/litongyang/Desktop/test123.txt", 'a')
		for i in range(0, len(self.stock_price_now)):
			fl.write(str(self.stock_price_now[i]))
			fl.write('\t')
			fl.write(str(self.bonds_price_now[i]))
			fl.write('\n')


if __name__ == '__main__':
	bond = BONDS()
	bond.bonds_value()
	bond.write_txt_fun()