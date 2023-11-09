from .Image import Image
from .Text import Text
import os
import numpy as np

class Stegano():

	def __init__(self):
		print("Stegano")

	def merge(self,textpath,imagepath):
		si = Image(imagepath)
		st = Text()
		
		content = st.read(textpath)
		pixels = si.pixels

		if(si.numberbits < len(content)):
			print('Message so Large!')
			return None

		#save text to png
		for i in range(si.width):
			for j in range (si.height):
				(r,g,b) = pixels[i,j]
				if len(content)<3:
					if len(content)==2:
						r = content[0]
						g = content[1]
						b = b%2
					elif len(content)==1:
						r =content[0]
						g = g%2
						b = b%2
					else:
						break
				else:	
					(r,g,b) = content[:3]

				si.set_pixel((i,j),si.merge_block_lsb((r,g,b),pixels[i,j]))
				content = content[3:]
			#endfor
				
			if(len(content)<=0):
				break

		si.save(imagepath)
		os.remove(textpath)

	def expand(self,imagepath):
		si = Image(imagepath)
		pixels = si.pixels
		header = si.header

		bintape = ''
		for i in range(si.width):
			for j in range(si.height):
				bintape+=''.join([str(e) for e in si.get_lsb(pixels[i,j])])
				header-=3
				if header<=0:
					break
			if header<=0:
				break

		if header<0:
			bintape=bintape[:header]

		return bintape
#end