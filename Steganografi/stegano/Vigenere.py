class Vigenere():

	def __init__(self,content=''):
		print("Vigenere")
		self.__content = content

	def read(self,path):
		try:
			file = open(path,'r')
			self.__content = file.read()
			file.close()
			return self.__content
		except FileNotFoundError as e:
			print(e)

	@property
	def content(self):
		return self.__content

	def encrypt(self,content,key):
		self.__content = ''
		i = 0
		for c  in content:
			self.__content += chr((ord(c)+ord(key[i%len(key)]))%265)
			i+=1
		return self.__content
		
	def decrypt(self,content,key):
		self.__content = ''
		i = 0
		for c  in content:
			self.__content += chr(abs((ord(c)-ord(key[i%len(key)]))%265))
			i+=1

	def save(self,path):
		try:
			file = open(path,'w+')
			file.write(self.__content)
			file.close()
		except FileNotFoundError as e:
			print(e)

	def unicode_table(self,x=65,y=91):
		n = y-x
		table = list()
		column = list()
		for i in range(0,n):
			for j in range(0,n):
				column.append(chr((x+((i+j)%(y-x)))))
			table.append(column)
			column = []
		return table
