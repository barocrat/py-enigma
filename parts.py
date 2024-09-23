alphabet='abcdefghijklmnopqrstuvwxyz'

class plugboard:
	def __init__(self, switches):
		#input checking
		try:
			for i in switches.split():
				assert len(i)==2
		except:
			raise ValueError('plugboard switches must be grouped in twos')
		try:
			assert switches==switches.lower()
			for i in switches.split():
				assert i in alphabet
		except:
			raise ValueError('plugboard switches must be all lowercase letters')
		#actual work
		self.switches=[i.lower() for i in switches.split()]
	def __repr__(self):
		return '[(plugboard) sw:%s]'%(self.switches)
	def run(self, char): #symmetric
		for isw in self.switches:
			if char in isw:
				return isw[(isw.index(char)+1)%2]
		return char

class rotor:
	def __init__(self, pos, setting, vals, notch):
		#input checking
		try:
			assert len(vals)==26
		except:
			raise ValueError('rotor vals must be 26 entries long')
		try:
			assert vals==vals.lower()
		except:
			raise ValueError('rotor vals must be all lowercase')
		try:
			assert pos in alphabet
		except:
			raise ValueError('rotor pos must be a lowercase letter')
		try:
			assert notch in alphabet
		except:
			raise ValueError('rotor notch must be a lowercase letter')
		try:
			assert setting in alphabet
		except:
			raise ValueError('rotor setting must be a lowercase letter')
		#actual work
		self.pos, self.stg, self.notch=alphabet.index(pos), alphabet.index(setting), alphabet.index(notch)
		vals=[(alphabet.index(vals[i])-i)%26 for i in range(26)]
		self.vals=vals[self.pos:]+vals[:self.pos]
		self.revvals=[-1 for i in range(26)]
		for i in range(len(self.vals)):
			self.revvals[(i+self.vals[i])%26]=(-self.vals[i])%26
		#checking if revvals generated properly
		try:
			assert -1 not in self.revvals
		except:
			raise ValueError('rotor vals must properly map input to output')
	def __repr__(self):
		pos, notch=alphabet[self.pos], alphabet[self.notch]
		return '[(rotor) pos:%s stg:%s vals:%s notch:%s]'%(pos, self.stg, self.vals, notch)
	def runfw(self, char): #run fowards
		ind=(alphabet.index(char)+self.stg)%26
		return alphabet[(ind+self.vals[ind])%26]
	def runbw(self, char): #run backwards
		ind=alphabet.index(char)
		return alphabet[(ind+self.revvals[ind]-self.stg)%26]
	def rotate(self): #rotate rotor
		self.pos=(self.pos+1)%26
		self.vals=self.vals[1:]+self.vals[:1]
		self.revvals=self.revvals[1:]+self.revvals[:1]

class reflector:
	def __init__(self, switches):
		#input checkng
		try:
			assert len(switches)==26
		except:
			raise ValueError('reflector switches len must be 26')
		try:
			for i in switches:
				assert i in alphabet
		except:
			raise ValueError('reflector switches must be all lowercase letters')
		#actual work
		self.switches=switches
	def __repr__(self):
		return '[(reflector) sw:%s]'%self.switches
	def run(self, char): #run()=run^-1()
		return self.switches[alphabet.index(char)]