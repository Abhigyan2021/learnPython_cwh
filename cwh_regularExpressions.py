
# Regular Expressions - These are special expressions in python used for complex pattern searching
# It is done using 're' module

# NOTE : Study about metacharacters before attempting to form regular expressions.


# Example

import re

pattern = r"[A-Z]+yclone"  

#NOTE : r"..."  creates a raw string

text = '''Intense Tropical Cyclone Dumazile was a strong tropical cyclone
that brought flooding to Madagascar and Réunion in early March 2018. 
Dumazile originated from a cyclone Dyclone area of low pressure that formed in the South-West
Indian Ocean near Agaléga on 27 February. The system concentrated into a 
tropical disturbance on 2 March and was named the next day, as it 
intensified into a tropical storm. Amid conditions conducive for 
intensification, Dumazile strengthened over the next two days and reached 
peak intensity on 5 March as an intense tropical cyclone, with 10-minute 
sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h 
(125 mph), and a central pressure of 945 hPa (27.91 inHg). The system weakened 
steadily over the next couple days because of increasing wind shear as it 
tracked to the southeast. Dumazile became post-tropical on 7 March and eventually 
dissipated completely on 10 March near the Kerguelen Islands.
'''


## Finding if a pattern is present in text


# match = re.search(pattern, text)
# print(match)


## Finding all occurrences of a pattern

matches = re.finditer(pattern, text)

for match in matches:
    print(match)
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])