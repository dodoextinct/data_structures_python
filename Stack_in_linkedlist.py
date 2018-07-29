class LinkedStack():
	class _Node:
		__slot__='_element','_next'

		def __init__(self, element, next):
			self._element= element
			self._next = next

	def __init__(self):
		self._head =None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def push(self, e):
		self._head = self._Node(e, self._head)
		self._size +=1
	

	def pop(self):
		if self.is_empty():
			raise ValueError
		answer  =self._head._element
		self._head = self._head._next
		self._size -=1
		return answer

	def top(self):
		if self.is_empty():
			raise ValueError
		return self._head._element

	def show(self):
		current =self._head
		while current is not None:
			print(current._element)
			current = current._next

S = LinkedStack()
S.push(2)
S.push(1)
S.push(3)
S.show()
print(S.top())

