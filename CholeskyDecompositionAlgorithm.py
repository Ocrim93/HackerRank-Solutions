import math


def CholeskyDecompositio(matrix):
	#lower triangular
	n = len(matrix[0]) 
	lower = [ [0 for _ in range(n)]
				for _ in range (n)  ]

	for i in range(n):
		for j in range(i+1):

			if i==j:
				sumL = 0
				for k in range(i):
					sumL += math.pow(lower[i][k],2)

				lower[i][i] = math.sqrt(matrix[i][i] - sumL)
			else:
				sumL = 0
				for k in range(j):
					sumL += lower[i][k]*lower[j][k]
				lower[i][j] = (matrix[i][j] - sumL)/lower[j][j]		

	return lower


if __name__ == '__main__':
	print('hello Mirco')

matrix = [[1, 2, 3],
          [2, 5, 11],
          [3, 11, 35]]

lower =CholeskyDecompositio(matrix)

print("Lower Triangular\t\tTranspose");
for i in range(len(matrix[0])):
    
    for j in range(len(matrix[0])):
    	print(lower[i][j], end = "\t")
       
    for j in range(len(matrix[0])):
    	print(lower[j][i], end = "\t")
    print(' ', end = '\n')
    
    print("\n");
