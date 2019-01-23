from matrix import status
class toantu():
	"""docstring for ClassName"""

	def __init__(self,a):
		self.trochoi =  a
				#print self.trochoi._get_list()
	def _trong(self):
		for i in range(3):
			for j in range(3):
				#print (i,j)
				#print self.trochoi._get_list()
				if self.trochoi._get_list()[i][j] == 0 :
					return (i,j)
		return (0,0)			
	def _up(self):
		(i,j)= self._trong()
		#print (i,j)
		if i !=2:
			self.trochoi._swap_di((i,j),(i+1,j))
		#print self.trochoi._get_list()
		return self.trochoi	
	def _down(self):
		(i,j)= self._trong()
		if i !=0:
			self.trochoi._swap_di((i,j),(i-1,j))
		return self.trochoi	
	def _right(self):
		(i,j)= self._trong()
		if j !=2:
			self.trochoi._swap_di((i,j),(i,j+1))
		return self.trochoi	
	def _left(self):
		(i,j)= self._trong()
		if j !=0:
			self.trochoi._swap_di((i,j),(i,j-1))
		return self.trochoi
	def move(self,a):
		if a==0:
			return self._up()
		if a==1 :
			return self._down()
		if a==2 :
			return self._right()	
		if a==3 :
			return self._left()	