class Stack:

	def __init__(self):
	    self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[-1]

	def showstack(self):
		for item in reversed(self.items):
			print(item)

	def is_empty(self):
		print(self.items == []) 


s1 = Stack()
s1.push(1)
s1.push("Karim")
s1.push(3)
s1.push(4)
s1.push("Hamish")
print("before pop : "+str(s1.size()))
s1.pop()
print("after pop : "+str(s1.size()))
s1.is_empty()
s1.showstack()
print("the peek value is "+str(s1.peek()))
