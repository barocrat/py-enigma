# enigma machine using python

## basic overview of files
**main.py**: creates an instance of the enigma class from impl.py, handles input/output\
**parts.py**: contains objects that each simulate a specific component of the enigma machine\
**impl.py**: implements the components from parts.py and handles internal workings

## notes on settings configuration
<sub>following notes briefly explained in main.py</sub>\
<sub>see <a href='https://en.wikipedia.org/wiki/Enigma_machine'>wikipedia</a> for more info on the internal workings</sub>

### plugboard settings
group letters to be switched into pairs\
join into a single string and separate with spaces\
letters not included in the switches won't be switched

**ex**: if i wanted to switch a with b, and c with d
* combine into "ab" and "cd"
* then add a space in between to get "ab cd"
* since e and f aren't included, they won't be switched

### rotor settings
first set of values is for rotor 1 (fastest)\
second set of values is for rotor 2\
third set of values is for rotor 3 (slowest)

**for each rotor's values:**\
first string shows ring setting (ie, offset) as a letter\
second string shows rotor initial position as a letter\
third string shows the rotor's internal shifts/wiring\
fourth string shows rotor notch (ie, turnover)

<sub>note: <a href="https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables">wikipedia</a> is a good resource to get rotor settings from</sub>

### reflector settings
string that shows the reflector's internal switches/wiring\
switches must be in pairs; if A becomes Z, Z must also become A
<br>

since the reflector is stationary, no notch, initial position, etc. is needed

**ex**: with a setting of "ZYXW...CBA",
* it would switch A into Z, B into Y, etc.
* as well as Z into A, Y into B, etc.

<sub>note: <a href="https://en.wikipedia.org/wiki/Enigma_rotor_details#Rotor_wiring_tables">wikipedia</a> is a good resource to also get reflector settings from</sub>