class powerTwo:
	def __init__(self, number):
		self.num = number
	def __lshift__(self):
		return f"{self.num}th power of two is {1 << self.num}"
	def __repr__(self):
		print(f"Hello, people!\nI'm power of two, but they call me powerTwo.")
		print("Find more about me: https://docs.python.org/3/reference/expressions.html")

  
#-------------------------------------#
#p = powerTwo(100)                    |
#print(p.__lshift__())                |
#p.__repr__()                         |
#-------------------------------------#
