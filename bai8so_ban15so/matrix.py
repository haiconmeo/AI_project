from array import *
class status():
	"""docstring for ClassName"""
	
	def __init__(self):
		self.dirc = [[0,2,3],[4,5,6],[7,8,1]]
		s=""
		for i in range(3):
			for j in range(3):
				s+=str(self.dirc[i][j])
		self.name=s
	def printdic(self):
		print self.dirc

	def _get_list(self):
		return self.dirc
	def sosanh(self,s):
		for i in range(3):
			for j in range(3):
				if self.dirc[i][j] != s[i][j] :
					return False
		return True		
	def _swap_di(self,(i1,j1),(i2,j2)):
		tam = self.dirc[i1][j1] 
		self.dirc[i1][j1] = self.dirc[i2][j2]
		self.dirc[i2][j2] = tam
		s=""
		for i in range(3):
			for j in range(3):
				s+=str(self.dirc[i][j])
		self.name=s

	def _get_name(self):
		return self.name







		
		