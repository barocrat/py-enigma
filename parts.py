alphabet='abcdefghijklmnopqrstuvwxyz'

class plugboard:
	def __init__(self, switches):
		#checking inputs
		if False in [len(i)==2 for i in switches.split()]:
			raise ValueError('plugboard switches must be grouped in pairs')
		if False in [i in alphabet+' ' for i in switches]:
			raise ValueError('plugboard switches may only be between lowercase letters')

		#initialization
		self.switches = switches.split()
	def __repr__(self):
		return '[(plugboard) sw:%s]'%(self.switches)
	
	def run(self, char): #works symmetrically
		for isw in self.switches:
			if char in isw:
				return isw[(isw.index(char)+1)%2]
		return char

class rotor:
	def __init__(self, pos, setting, vals, notch):
		#checking inputs
		if len(vals)!=26:
			raise ValueError('rotor vals must be of length 26')
		if False in [i in alphabet for i in vals]:
			raise ValueError('rotor vals must consist of all lowercase letters')
		if pos not in alphabet:
			raise ValueError('rotor pos must be a lowercase letter')
		if notch not in alphabet:
			raise ValueError('rotor notch must be a lowercase letter')
		if setting not in alphabet:
			raise ValueError('rotor setting must be a lowercase letter')

		#initialization
		self.pos = alphabet.index(pos)
		self.stg = alphabet.index(setting)
		self.notch = alphabet.index(notch)

		#vals for forward operation
		vals = [(alphabet.index(vals[i])-i)%26 for i in range(26)] #not shifted yet
		self.vals = vals[self.pos:]+vals[:self.pos] #defined and shifted

		#vals for backwards operation
		self.revvals=[-1 for i in range(26)]
		for i in range(len(self.vals)):
			self.revvals[(i+self.vals[i])%26] = (-self.vals[i])%26

		#checking revvals is configured properly
		if -1 in self.revvals:
			raise ValueError('rotor vals has impossible configuration')
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
		#checking inputs
		if len(switches)!=26:
			raise ValueError('reflector switches must be of length 26')
		if False in [i in alphabet for i in switches]:
			raise ValueError('reflector switches must consist of all lowercase letters')

		#initialization
		self.switches=switches
	def __repr__(self):
		return '[(reflector) sw:%s]'%self.switches
	
	def run(self, char): #works symmetrically
		return self.switches[alphabet.index(char)]