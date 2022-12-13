
mathSymbol = ('-','+','*','/')

def revPolish(aList):
	newList = aList
	for i,el in enumerate(aList):
		if el in mathSymbol:
			result = operation(aList[i-2:i+1])
			newList.pop(i)
			newList.pop(i-1)
			newList[i-2] = str(result)
		
			if len(newList) == 1:
				print('GREAT',float(newList[0]))
				return newList[0]
			else:
				revPolish(newList)
		else:
			continue 

def operation(oList):
	return eval(oList[0]+oList[2]+oList[1])
	# uselss
	operand1 = float(oList[0])
	operand2 = float(oList[1])
	if oList[2] == '-':
		return operand1- operand2
	if oList[2] == '+':
		return operand1+ operand2	
	if oList[2] == '/':
		return operand1/ operand2
	if oList[2] == '*':
		return operand1* operand2		


c = ['3','4','-','5','*']
c = ['1','2','3','4','5','+','*','+','*']
c =['3','4','5','-','*']
c = ['1','2','3','+','*']
c = ['1','2','3','4','5','+','*','+','*']
revPolish(c)	