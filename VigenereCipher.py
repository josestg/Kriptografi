
import sys

def unicode_table():
	for i in range(0,256):
		for j in range(0,256):
			print(chr(((i+j)%256)),end=' ')
		print('')

def encrypt_text(plain,key):
	i = 0
	ch = ''
	for p  in plain:
		ch += chr((ord(p)+ord(key[i%len(key)]))%265)
		i+=1
	return ch

def decrypt_text(ch,key):
	i = 0
	plain = ''
	for c  in ch:
		plain += chr(abs((ord(c)-ord(key[i%len(key)]))%265))
		i+=1
	return plain

def save_file(ch):
	file = open('pesan.txt','w+')
	file.write(ch)
	file.close()
	
def read_file(file):
	try:
		file = open(file,'r')
		if file.mode == 'r':
			content = file.read()
			return content
	except FileNotFoundError:
		print('File ',file,' Not Found!')
		sys.exit()

def main():
	if(len(sys.argv)<=1):
		print('\n','-'*18,'HELP','-'*18)
		print(' example : ',sys.argv[0],' -e filename.txt \n')
		print(' -e || --encrypt : Encrypt Message from File')
		print(' -d || --decrypt : Decrypt Message from File')
		print(' -t : Show Table')
		print('-'*42,'\n')
	elif (sys.argv[1]=='-e' or sys.argv[1]=='--encrypt'):
		try:
			content = read_file(sys.argv[2])
			key = input('Key : ')		
			ch = encrypt_text(content,key)
			save_file(ch)
			print('Encrypt Completed!')
		except IndexError:
			print(' you need filename.txt')

	elif (sys.argv[1]=='-d' or sys.argv[1]=='--decrypt'):
		try:
			content = read_file(sys.argv[2])
			key = input('Key : ')		
			ch = decrypt_text(content,key)
			save_file(ch)
			print('Decrypt Completed!')
		except IndexError:
			print(' you need filename.txt')
	elif (sys.argv[1]=='-t'):
		unicode_table()
	else:
		sys.exit()

if __name__ == "__main__":
	main()
	