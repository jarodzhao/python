from person import Person

class Manager(Person):
	'继承并重写了 Person 的 giveRaise 方法'
	def giveRaise(self, percent, bonus=0.1):
		# self.pay *= (1.0 + percent + bonus)	#bonus 为管理人员额外奖励，默认10%
		Person.giveRaise(self, percent + bonus)	#重构父类的方法，直接将额外的奖励与加薪系数相加

if __name__ == '__main__':
	jarod = Manager(
		name = 'jarod zhao',
		mobile='18625500030',
		nid='410823198009240854',
		pay=50000)
	jarod.giveRaise(0.1, 0.5)
	print(jarod.pay)