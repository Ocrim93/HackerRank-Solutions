#cycles in permutations

def find_cycle(starting,fmap):
	
	cycle = []
	key = starting
	cycle.append(starting)
	
	while key != 0:
		if(fmap[key] == starting):
			key = 0
		else:
			key =  fmap[key]
			
			cycle.append(key)
	
		
	return cycle

def PrintCycles(Perm):
	fmap = {}
	for i in range(len(Perm)):
		fmap[i+1] = Perm[i]
	cycles = []

	fmap_temp = fmap	
	while len(fmap_temp.keys()) != 0:
		for key in fmap_temp.keys():
			
			cycle = find_cycle(key,fmap_temp)
			cycles.append(cycle)
			fmap_temp = {i : fmap_temp[i] for i in fmap_temp if i not in cycle}
			break
	cycles.sort(reverse = True,key= lambda x : len(x))		
	msg = ''
	result = []
	for el in cycles:
		msg = str(el).replace(",", '')
		msg = msg.replace('[','(')
		msg = msg.replace(']',')')
		result.append(msg)
		msg = ''
	return result	



if __name__ == "__main__":
	print(PrintCycles([5,4,3,6,7,8,1,2]))