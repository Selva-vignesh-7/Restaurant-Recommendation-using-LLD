
import random
import sys

def get_list(x):
	x=int(x)
	l=[]
	for i in range(0,5):
			l.append(random.randint(15,x+35))
	return l
	

print(get_list(sys.argv[1]))




