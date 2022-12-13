regex_integer_in_range = r"\b[1-9][0-9][0-9][0-9][0-9][0-9]\b"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=((\d)\d\2))"	# Do not delete 'r'.


import re
P = str(4542867)

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)





def count_substring(string, sub_string):
    c = 0
    x = re.search(sub_string, string)
    print(x)
    while x!= None:
        
       string = string[x.span()[0]+1:]
       x = re.search(sub_string, string)
       c += 1
    print(c)
    

count_substring('ABCDCDC','CDC')    


# Complete the solve function below.
def solve(s):
    names = s.split(' ')
    result = ''
    d = []
    for i in names:
        i = list(i)
        d.append(i)
    print(d)    
    for i in d:

        if re.search("[0-9]",''.join(i)) != None:
            continue
        if len(i) == 0 :
        	continue    
           
        c= i[0].upper()
        i.pop(0)
        i.insert(0,c)
       
    for i in d:
        result += ''.join(i)+ ' '
    
    return  result[:-1]

print(solve('q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'))    