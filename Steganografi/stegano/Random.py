class BBS():
	def __init__(self):
		self.p = 11351
		self.q = 11987
		self.n = self.p*self.q
		self.bit = pow(2,5)

	def seed(self,s):
		self.prec = pow(s,2) % self.n

	def rand(self,x,y):
		nxt = pow(self.prec,2) % self.n
		self.prec = nxt
		return bin((x + (nxt-x)%(y-x))%self.bit)[2:]

def main():
	bbs = BBS()
	bbs.seed(10)
	tape = ''
	for i in range(1,100):
		tape+=(bbs.rand(40,100))
	print(tape)
	

if __name__ == '__main__':
	main()
