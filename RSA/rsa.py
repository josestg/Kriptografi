import random as rd
from math import sqrt

# get relative prime Euclid's algorithm
def pbb(a,b):
	if b==0:
		return a
	else:
		return pbb(b,a%b)

def get_e(phi):
	# memilih e secara random akan mengakibatkan proses enkripsi semakin lama
	# karena melibatkan perpangkatan yang besar dibandingkan dengan memilih secara sequential,
	# namun akan menghasilkan nilai e yang lebih bervariasi
	# a = rd.randint(2,phi)
	a = 2
	while a< phi:
		if(pbb(a,phi)==1):
			return a
		# a =rd.randint(2,phi)
		a+=1

def get_d(phi,e):
	k=1
	while True:
		# hasil integer jika sisa bagi = 0
		d = (k*phi + 1)%(e)
		if d==0:
			return int((k*phi + 1)/(e))
		k +=1


def proses(msg,key,n):
	# decrypt and ecrypt
	cp = ''
	for c in msg:
		cp+=chr(((pow(ord(c),key))%n))
		
	return cp

def main():
	help_text="""
		Disarankan menggunakan nilai p*q >= 256 (banyak karakter ascii),
		dengan p dan q adalah bilangan prima.
		Pesan menerima spasi.
	"""

	print(help_text)
	msg = input('Pesan : ')
	p = int(input("p: "))
	q = int(input("q: "))
	n = p*q
	phi = (p-1)*(q-1)
	if phi>1 and n>=256 :
		e = get_e(phi)
		d = get_d(phi,e)
		
		print('\nPsangan Kunci')
		print("kunci publik ({e},{n})".format(e=e,n=n))
		print("kunci private ({d},{n})".format(d=d,n=n))

		print('\nBukti Kunci')
		print("ed mod phi === ",e*d%phi)

		cp = proses(msg,e,n)
		print('\nHasil Enkripsi :\n')
		print(cp)

		pl = proses(cp,d,n)
		print('\nHasil Dekripsi:\n')
		print(pl)
	else:
		print("pilih q dan p yang lain!")



if __name__ == '__main__':
	main()