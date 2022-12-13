
from collections import defaultdict
def mergeSort(unsorted):

	if len(unsorted) == 1:
		return unsorted

	mid = int(len(unsorted)/2)

	firstHalf = unsorted[:mid]
	secondHalf = unsorted[mid:]

	return merge(mergeSort(firstHalf),mergeSort(secondHalf))

def merge(list1,list2):
	sortedList = []

	while (len(list1) > 0 or len(list2) >0):
		if len(list1) == 0:
			
			return  list2 + list(reversed(sortedList))
		elif len(list2) == 0:
			return  list1 + list(reversed(sortedList))
		else:
			if list1[-1] >= list2[-1]:
				sortedList.append(list1.pop())
			else:
				sortedList.append(list2.pop())	
		
		


if __name__ == '__main__':
	unsorted = [2,3,4,5,1,0]
	result = mergeSort(unsorted)

	print(result)
	
	d= defaultdict(lambda  : 'Non present')
	d[1] = 2
	d[2] = 3

	print(d[3])