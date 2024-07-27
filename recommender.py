import csv


import random
from collections import defaultdict

v = open('/Users/spurthy/Desktop/Restaurnt-Recommendation-System/bands.csv')
r = csv.reader(v)
d={}
flag=True
for item in r:
	if(not flag):
		d[item[0]]=item[1]
	flag=False
	



filename = "push.csv"
	
# writing to csv file 
with open(filename, 'w') as csvfile: 
	# creating a csv writer object 
	csvwriter = csv.writer(csvfile) 
	csvwriter.writerow(["Business id","Stars","Service","Cleanliness","Authenticity","Value for money"])
	for k,v in d.items():
			temp=int(v)
			if(temp>=4):
				csvwriter.writerow([k,v,random.randint(75,95),random.randint(85,95),random.randint(80,95),random.randint(77,95)]) 
			else:
				csvwriter.writerow([k,v,random.randint(15,temp*20+35),random.randint(15,temp*20+35),random.randint(15,temp*20+35),random.randint(15,temp*20+35)]) 

