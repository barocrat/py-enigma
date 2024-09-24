# enigma machine using python

## basic overview of files
main.py: creates an instance of the enigma class from impl; handles input/output as well\
parts.py: contains objects that each simulate a component of the enigma machine\
impl.py: puts together the components from parts.py; handles rotation as well

## notes on settings configuration
<sub>all briefly explained in main.py</sub>\
<sub>see <a href='https://en.wikipedia.org/wiki/Enigma_machine'>wikipedia</a> for more info on the internal workings</sub>

### plugboard switches
group letters to be switched into pairs\
join them into a single string and separate with spaces\
letters that are not to be switched are ignored

**ex**: if i wanted to switch a<->b and c<->d,
* combine into 'ab' and 'cd'
* then into 'ab cd'.
* since e is not switched, it is not included

### rotor settings
first set of values is for rotor 1, or the fastest one\
second set is for rotor 2, etc.

**for each rotor's values:**\
first letter shows ring setting (ie: offset) as a letter\
second letter shows initial position as a letter\
third string shows offset relative to its position in the string (ex: 'ABC...' = no shift, 'BCD...' = shift once, etc.)\
fourth letter shows notch (aka: turnover)

**ex**: if i wanted a rotor that
* no offset
* initial position of three
* shifted all letters backward by one
* and turnover at C

then it would be shown as 'A', 'C', 'ZABC...', 'C'

### reflector settings
string which shows offset relative to its position in the string (ex: 'ABC...' = no shift, 'BCD...' = shift once, etc.)\
can be thought of as a rotor which doesn't move, which maps two inputs together so they output as each other

**ex**: if i wanted a reflector that mimicked the atbash cipher,
* the string would be 'ZYX...CBA'
* since each input is mapped to its output

## 
