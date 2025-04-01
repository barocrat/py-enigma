from parts import plugboard, rotor, reflector
alphabet='abcdefghijklmnopqrstuvwxyz'

class enigma:
	def __init__(self, settings):
		#initialize the components
		self.plugboard=plugboard(settings[0][0])
		self.rotor1=rotor(settings[1][0], settings[1][1], settings[1][2], settings[1][3])
		self.rotor2=rotor(settings[2][0], settings[2][1], settings[2][2], settings[2][3])
		self.rotor3=rotor(settings[3][0], settings[3][1], settings[3][2], settings[3][3])
		self.reflector=reflector(settings[4][0])
	def run(self, char):
		#initialization
		u=char==char.upper()
		char=char.lower()

		#running char through machine
		char=self.plugboard.run(char)
		char=self.rotor1.runfw(char)
		char=self.rotor2.runfw(char)
		char=self.rotor3.runfw(char)
		char=self.reflector.run(char)
		char=self.rotor3.runbw(char)
		char=self.rotor2.runbw(char)
		char=self.rotor1.runbw(char)
		char=self.plugboard.run(char)

		#return
		if u:
			return char.upper()
		return char
	def rotate(self):
		self.rotor1.rotate()
		if self.rotor1.pos==self.rotor2.notch:
			self.rotor2.rotate()
			if self.rotor2.pos==self.rotor3.notch:
				self.rotor3.rotate()