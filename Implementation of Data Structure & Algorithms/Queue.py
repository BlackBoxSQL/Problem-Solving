class Queue:

	def __init__(self):
		self.items = []

	def is_empty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		self.items.pop()

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[-1]

	def the_queue(self):
		for item in self.items:
			print(item)


q = Queue()
q.enqueue(4)
q.enqueue(2)
q.enqueue(2)
q.enqueue(5)
q.enqueue(6)
q.enqueue(1)
q.enqueue(1)
q.the_queue()
print("the peek item is : "+str(q.peek()))
