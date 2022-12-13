


def formattingString(lis):
	lis_number = []
	for el in lis:
		lis_number.append(ord(el)- ord('a'))
	return lis_number	

def step2Func(unsorted,sortedList):

	minn = 999
	minn_pos = 999

	if len(unsorted) ==1:
		sortedList.append(unsorted.pop())
		return ([],sortedList)

	for i,el in enumerate(unsorted):
			
		if i == 0:
			continue
		if el > unsorted[i-1] and  el < minn:
			minn = el
			minn_pos = i
					
	if minn == 999:
		return (0,0)
	else:
		unsorted.pop(minn_pos)
		sortedList.append(minn)
		
		return(unsorted,sortedList)	
				


def step3Func(unsorted,sortedList):
	maxx = -999
	maxx_pos = 999
	if len(unsorted) ==1:
		sortedList.append(unsorted.pop())
		return ([],sortedList)

	for i,el in enumerate(unsorted):
		if i == 0:
			continue
		if el < unsorted[i-1] and el > maxx:
			maxx = el
			maxx_pos = i
	if maxx == -999:
		return (0,0)
	else:
		unsorted.pop(maxx_pos)
		sortedList.append(maxx)
		return(unsorted,sortedList)	
				
			

def sorting(unsorted):
	unsorted = formattingString(unsorted)
	print(unsorted)
	sortedList = sortingUt(unsorted)
	
	return  list(chr(i+ord('a')) for i in sortedList)
	
def sortingUt(unsorted):
	
	sortedList = []
	starting_number = 0
	starting_position = 0
	for i,el in enumerate(unsorted):
		
		if i == 0:
			starting_number = el
			starting_position = i
			continue 
		if el < starting_number:
			starting_number = el
			starting_position = i
		
	unsorted.pop(starting_position)
	sortedList.append(starting_number)
	
	

	result2 = step2Func(unsorted,sortedList)

	while result2 != (0,0):

		unsorted =result2[0]
		sortedList = result2[1]
		
		print('w',unsorted,sortedList)
		result2 =  step2Func(unsorted,sortedList)
	
	result3 = step3Func(unsorted,sortedList)

	while result3 != (0,0):
		unsorted =result3[0]
		sortedList = result3[1]
		print('d',unsorted,sortedList)
		result3 =  step3Func(unsorted,sortedList)
	
	if len(unsorted) == 0:
		return sortedList

	else:
		return sortedList + sortingUt(unsorted)





if __name__ == '__main__':
	print('hello')
	s = 'geabcdf'
	print(sorting(s))