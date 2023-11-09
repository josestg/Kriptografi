import os
import stegano as stg

def xorbittape(key,lenght):
	#xor operation
	bbs  = stg.BBS()
	# # generate seed with odd ord(char of key)
	s = sum(list(map(lambda x: x if x%2==1 else 0, [ord(e) for e in key])))
	bbs.seed(s)
	# # build bits tape , where len(bits) = len(content)
	xortape=''
	while(len(xortape)<lenght):
		xortape+=bbs.rand(0,lenght)
	return xortape

## TEXT + IMAGE -> STEGANOIMAGE
def merge(data):

	text = os.path.join(data['basepath'],data['txtname'])
	img  = os.path.join(data['basepath'],data['imgname'])
	key = data['key']
	log = open('./log.txt','w')
	
	# Vigenere Process : Encrypt Message
	vc = stg.Vigenere()
	content = vc.read(text)
	content = vc.encrypt(content,key)
	log.write('--> {} Sudah Dienkripsi Menggunakan Algoritma Vigenere Cipher.\n'.format(data['txtname']))
	

	st = stg.Text()
	# double encrypt ( vigenere + xor )
	if data['encrypt'] :	
		# xor only content wit key
		bintape = st.get_binary_tape(content)
		#xor bitwise content and random xortape
		xortape = xorbittape(key,len(bintape))
		xorresult=''
		for x,y in zip(bintape,xortape):
			xorresult += str(int(x)^int(y))
		st.ext = text # header need extentions
		st.set_header(xorresult)
		st.save(text)
		log.write('--> Pesan Dikonpresi ke binary dan dilakukan xor dengan kunci.\n')
	else:
		print("NO XOR")
		## convert content to binary and save to the same file
		st.save_to_binary(content,text)

	# put binary content from text file to binary pixels of image file
	stegano = stg.Stegano()
	stegano.merge(text,img)
	log.write('--> Pesan Sudah disembunyikan di gambar {}\n'.format(data['imgname']))
	log.close()

## STEGANOIMAGE -> TEXT + IMAGE 
def expand(data):
	key = data['key']
	text = data['newname']
	img  = os.path.join(data['basepath'],data['imgname'])

	stegano = stg.Stegano()
	# bintape = bin(header) + bin(extention) + bin(content)
	bintape = stegano.expand(img)

	st = stg.Text()
	#expand header, extention and content
	ext 	= bintape[st.headersize : st.headersize+st.extsize]
	content = bintape[st.headersize + st.extsize :]
	ext = ''.join([ chr(int(ext[i:i+8],2)) for i in range(0,24,8) ])
	textpath = os.path.join(data['basepath'],data['newname']+'.'+ext)

	# double decrypt ( vigenere - xor )
	if data['encrypt'] :
		xortape = xorbittape(key,len(content))
		xorresult=''
		for x,y in zip(content,xortape):
			xorresult += str(int(x)^int(y))
		content = xorresult
		print("YES XOR")

	#convert binary to chiper content
	chiper = st.binary_to_content(content)
	# decrypt 
	vc = stg.Vigenere()
	vc.decrypt(chiper,key)
	vc.save(textpath)



def main():
	data = {
		'basepath':'./test/',
		'imgname':'Lenna.png',
		'txtname':'message.txt',
		'key':'kunci',
		'encrypt':True,
		'newname':"message"
	}
	expand(data)

if __name__ == '__main__':
	main()
