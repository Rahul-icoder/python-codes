import math
class Node:
	def __init__(self,value=None,node=None):
		self.data = value
		self.next = node

class LinkList:
	def __init__(self):
		self.head = None

	def insert_at_first(self,value):
		node = Node(value,self.head)
		self.head = node

	def print_linklist(self):
		if self.head is None:
			print('LinkList is empty')
		itr = self.head
		linklist_str = ""
		while itr:
			linklist_str += str(itr.data) + '-->'
			itr = itr.next
		print(linklist_str)
	def insert_at_last(self,value):
		if self.head is None:
			node = Node(value,None)
			self.head = node
			return
		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(value,None)
	def list_to_linklist(self,list):
		self.head = None
		for elem in list:
			self.insert_at_last(elem)

	def linklist_length(self):
		counter = 0
		itr = self.head
		while itr:
			counter += 1
			itr = itr.next
		return counter
	def linklist_mid_element(self):
		mid_index = math.floor(self.linklist_length()/2)
		if mid_index == 0:
			print('Epty linklist')
		itr = self.head
		counter = 0
		while itr:
			print(counter)
			if counter == mid_index:
				print(itr.data)
				return
			itr = itr.next
			counter += 1
	def insert_at(self,index,value):
		if index < 0 or index > self.linklist_length():
			print('please provide valid index')
			return
		if index==0:
			self.head = Node(value,self.head)
			return
		itr = self.head
		counter = 0
		while itr:
			if counter == index-1:
				itr.next = Node(value,itr.next.next)
			itr = itr.next
			counter += 1

link_obj = LinkList()
link_obj.list_to_linklist(['rahul','vicky','anish','manish','ankita','uttam'])
# print(link_obj.linklist_length())
# link_obj.linklist_mid_element()
link_obj.insert_at(0,'prashant')
link_obj.print_linklist()