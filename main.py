from impl import enigma
from parts import alphabet

#settings
'''
settings list follows:
[
    plugboard settings,
	rotor1 (fastest) setting, initial position, values, notch,
	rotor2 setting, initial position, values, notch,
	rotor3 (slowest) setting, initial position, values, notch,
	reflector values
]

rer is whether the settings should reset for each input
'''
settings = [
	'ab cd ef gh',
	'a', 'a', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'.lower(), 'q',
	'a', 'e', 'AJDKSIRUXBLHWTMCQGZNPYFVOE'.lower(), 'e',
	'a', 'z', 'BDFHJLCPRTXVZNYEIWGAKMUSQO'.lower(), 'v',
	'EJMZALYXVBWFCRQUONTSPIKHGD'.lower()
]
rer = True

#io handling
machine=enigma(settings)
while True:
	i, o=input(), ''
	for j in i:
		if j in alphabet:
			o+=machine.run(j)
			machine.rotate()
		else:
			o+=j
	print(o)
	if rer:
		machine=enigma(settings)