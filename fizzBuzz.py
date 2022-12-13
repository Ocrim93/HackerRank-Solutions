def runn( N, M):
	print(N,M)
	sequence = []
	message = ''
	if N==M:
		sequence.append(int(N))
	else:	
		n = max(int(N),int(M))
		m = min(int(N),int(M))
		for i in range(m,n+1):
			sequence.append(i)
	print(sequence)
	for el in sequence:
		if el % 3 == 0 and el % 5 == 0:
			message = message + 'FizzBuzz,'
		elif el % 3 == 0:
			message = message + 'Fizz,'
		elif el %5 == 0 :
			message = message + 'Buzz,'
		else:
			message = message + str(el) + ','		

	return message[0:len(message)-1]

print(runn(1,5))	