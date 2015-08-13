#

from p05_priority_queue import PriorityQueue

class Item:
	def __init__(self,name):
		self.name = name
	def __repr__(self):
		return 'Item({!r})'.format(self.name)

def main():
	q = PriorityQueue()
	q.push(Item('foo'),1)
	q.push(Item('bar'),5)
	q.push(Item('spam'),4)
	q.push(Item('grok'),1)
	print(q.pop())
	print(q.pop())
	print(q.pop())
	print(q.pop())

if __name__ == '__main__':
	main()
