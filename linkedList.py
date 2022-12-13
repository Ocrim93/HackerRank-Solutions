# a linked list is a sequence of data elements, which are connected together via links.
# Each data element contain a connection to another data element in form of a pointer 
# Python does not have linked lists in its standard library 


class Node:
	def __init__(self,dataValue = None):
		self.dataValue = dataValue
		self.nextNode = None

class LinkedList:
	def __init__(self):
		self.headValue = None

	def printList(self):
		printValue = self.headValue

		while printValue is not None:
			print(printValue.dataValue)
			printValue = printValue.nextNode

	def pushAtBeginning(self,dataValue):
		newNode = Node(dataValue)
		# Updating
		newNode.nextNode = self.headValue
		self.headValue = newNode
	def pushAtEnd(self,dataValue):
		newNode = Node(dataValue)

		last_node = self.headValue.nextNode 
		while(last_node.nextNode is not None):
			last_node = last_node.nextNode
		last_node.nextNode = newNode	

	def pushAfterANode(self,middleNode,newData):
		newNode = Node(newData)

		item = self.headValue
		while (item is not None):
			if(item.dataValue == middleNode.dataValue):
				newNode.nextNode = item.nextNode
				item.nextNode = newNode

			item = 	item.nextNode

	def removeNode(self,removeNode):
		item = self.headValue

		while(item is not None):
			if(item.nextNode.dataValue == removeNode.dataValue):
				item.nextNode = removeNode.nextNode
				break
			item = item.nextNode
	
	def getNode(self,data):
		selectedNode = self.headValue

		while(selectedNode is not None):
			if(selectedNode.dataValue == data):
				break
			selectedNode = selectedNode.nextNode
		
		return selectedNode

	def reverseList(self):
		list_data= []
		item = self.headValue
		while(item is not None):
			list_data.append(item.dataValue)
			item = item.nextNode
		list_data.reverse()
		
		self.headValue  = Node(list_data[0])
		item = self.headValue
		for el in list_data[1:]:
			addingNode = Node(el)
			item.nextNode = addingNode
			item = item.nextNode
		
				

if __name__ == '__main__':
	list_day = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

	linkList = LinkedList()

	linkList.headValue = Node('Monday')

	n2 = Node('Tuesday')
	n3 = Node('Wednesday')

	linkList.headValue.nextNode = n2
	n2.nextNode =n3

	linkList.pushAtBeginning('Sunday')
	linkList.pushAfterANode(n2,'Friday')
	linkList.printList()
	n = linkList.getNode('Friday')
	linkList.removeNode(n)
	print('--------------')
	
	linkList.printList()
	print('--------------')
	linkList.reverseList()
	linkList.printList()





