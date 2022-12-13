#DiceThrowingGame
import math
def expected_score(n, r):
    # Write your code here
    if n ==0:
        return 0
    if r==6 :
        return 3.5*n
    fmap = {5:1,4:math.pow(2,n),3:math.pow(3,n),2:math.pow(4,n),1:math.pow(5,n)}
    
    the_expected_round = 1/(1-fmap[r]/math.pow(6,n))
    return round(3.5*n*the_expected_round ,5)

print(expected_score(1,5))    