
class Text():
	
	def __init__(self):
		print("Text")
		self.headersize = 32
		self.extsize = 24
	
	def read(self,path):
		try:
			self.__file = open(path,'r')
			self.__content = self.__file.read()
			self.__file.close()

			#set file extentions
			self.ext = path

			return self.__content
		except FileNotFoundError as e:
			raise e

	@property
	def ext(self):
		return self._ext

	@ext.setter
	def ext(self,path):
		self.__ext = path.split('/')[-1].split('.')[-1]

	@property
	def content(self):
		return self.__content

	@content.setter
	def content(self,content):
		self.__content = content

	def save(self,path):
		try:
			file = open(path,'w')
			file.write(self.__content)
			file.close()
		except FileNotFoundError as e:
			print(e)

	def get_binary_tape(self,content):
		binarytape = ''
		for c in content:
			binarytape+='{0:08b}'.format(int(ord(c)))
		return binarytape

	def set_header(self,bintape):
		total = int(len(bintape))+self.headersize+self.extsize
		header = '{0:032b}'.format(total) 
		ext = self.get_binary_tape(self.__ext)
		fullcontent = header + ext + bintape
		self.__content = fullcontent

	def save_to_binary(self,content,path):
		self.ext = path
		bintape = self.get_binary_tape(content)
		self.set_header(bintape)
		self.save(path)
		return bintape

	def binary_to_content(self,bintape):
		content=''
		while len(bintape)>0:
			char = bintape[:8]
			bintape = bintape[8:]
			content+=chr(int(char,2))
		self.__content = content
		return self.__content

	def expand(self):
		""" divide binary tape to header, extentions, and content.
			return bin(header), bin(ext), bin(content)
		"""
		fc = self.__content
		hz = fc[0:self.headersize]
		ext = fc[self.headersize : self.extsize+self.headersize]
		content = fc[self.headersize+self.extsize : ]
		return hz,ext,content

