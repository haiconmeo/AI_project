from matrix import *
from ope import toantu
import numpy as np
def _start(a):
	for i in range(10):
		a._swap_di((np.random.random_integers(3),np.random.random_integers(3)),(np.random.random_integers(3),np.random.random_integers(3)))
		return a
a = status()
#a = _start(a)
for i in range(10):
	(i1,j1) = (np.random.random_integers(3)-1,np.random.random_integers(3)-1)
	(i2,j2) = (np.random.random_integers(3)-1,np.random.random_integers(3)-1)
	a._swap_di((i1,j1),(i2,j2))
	#print (i1,j1)
dic ={}
dic[a._get_name()] = a._get_list()
print dic
b = toantu(a)
print len(dic)
while len(dic)>0:
	x = str(dic.items()[0][0])
	print x
	if x=='123456780':
		print ok
		break
	dic.pop(x)
	#print dic 
	#break
	for i in range(3):
		x2=b.move(i)
		if x2._get_name() not in dic.keys():
			dic[x2._get_name()] = x2._get_list()
			print dic 
			break
		#b.move(i)._get_list()

	#print dic
#print b.move(0)._get_list()