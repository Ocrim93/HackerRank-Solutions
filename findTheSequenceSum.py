#findTheSequenceSum
# Complete the getSequenceSum function below.
def getSequenceSum(i, j, k):
	sum = i
	while i != j:
		i += 1 
		sum += i
		
	while j != k:
		j -= 1
		sum += j 
	return sum
def getSequenceSum2(i, j, k):
	fact1 = i*(j-i+1) + (j-i)*(j-i+1)/2
	fact2 = k *(j-k+1) + (j-k)*(j-k+1)/2
	return int((2*j*j-i*i-k*k+i+k)/2)
	#return int(fact1+ fact2 -j)			 

if __name__ == '__main__':
	print(getSequenceSum(-26758517, 22438981, -80854430))
	print(getSequenceSum2(-26758517, 22438981, -80854430))
