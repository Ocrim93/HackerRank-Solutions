#Efficnet Team

import numpy as np

def getTotalEfficiency(skill):
	n = len(skill)
	if n % 2 != 0:
		return -1
	sum = np.array(skill).sum()


	if 	2*sum/n != int(2*sum/n):
		return -1
	k = int(2*sum/n)
	#team = []
	skill_temp = skill
	efficiency = 0
	 while len(skill_temp)>0:
		element_removed = False

		for el1 in skill_temp:
			for el2  in skill_temp[1:]:
				if( el1+el2 == k):
					#team.append((el1,el2))
					skill_temp.remove(el1)
					skill_temp.remove(el2)
					efficiency += el1*el2
					element_removed = True
					break
			if element_removed:
	 			break
	
	
	
	
	return efficiency	




if __name__ == "__main__":
	skill = [1,2,3,2]
	skilss = np.array(skill)


	print(getTotalEfficiency(skill))
	