class Person:
	def __init__(self, name, mobile, nid, pay=0, job=None):
		self.name = name
		self.mobile = mobile
		self.nid = nid
		self.pay = pay
		self.job = job

	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)

