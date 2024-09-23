from parts import plugboard, rotor, reflector
alphabet='abcdefghijklmnopqrstuvwxyz'

class enigma:
	def __init__(self, settings):
		self.plugboard=plugboard(settings[0])
		self.rotor1=rotor(settings[1], settings[2], settings[3], settings[4])
		self.rotor2=rotor(settings[5], settings[6], settings[7], settings[8])
		self.rotor3=rotor(settings[9], settings[10], settings[11], settings[12])
		self.reflector=reflector(settings[13])
	def run(self, char):
		u=char==char.upper()
		char=char.lower()
		char=self.plugboard.run(char)
		char=self.rotor1.runfw(char)
		char=self.rotor2.runfw(char)
		char=self.rotor3.runfw(char)
		char=self.reflector.run(char)
		char=self.rotor3.runbw(char)
		char=self.rotor2.runbw(char)
		char=self.rotor1.runbw(char)
		char=self.plugboard.run(char)
		if u:
			return char.upper()
		return char
	def rotate(self):
		self.rotor1.rotate()
		if self.rotor1.pos==self.rotor2.notch:
			self.rotor2.rotate()
			if self.rotor2.pos==self.rotor3.notch:
				self.rotor3.rotate()