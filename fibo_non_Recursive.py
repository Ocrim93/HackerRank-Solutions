


def fibo_func(number):
	fibo_num = 0
	if number ==0 or number ==1:
		fibo_num=1
	else:
		for i in range(2,number+1):
			if i == 2:
				first = 1
				second =  1
				continue
			fibo_num = first +second
			first = second
			second =fibo_num
	return fibo_num	 



print(fibo_func(6))
