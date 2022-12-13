# compute pi value by using Monte Carlo simulation



import random
import math

def pi_MC(number_of_trial):
	
	success = 0
	for i in range(number_of_trial):
		x = 2*random.random()-1   #generates random number between 0-1
		y = 2*random.random()-1
		x = random.uniform(0, 1)
		y = random.uniform(0, 1)
		if math.sqrt(x*x + y*y) <= 1:
			success +=1
		else:
			continue 

	return 4*success/(number_of_trial)

number_of_trial = 10000000
pi = pi_MC(number_of_trial)
print(pi)
print(math.pi - pi)