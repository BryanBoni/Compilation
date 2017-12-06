# -*- coding: utf-8 -*-
"""
if i%2 == 0:
	print("well done bitch !")
else :
	print("to bad idiot")

a = i;
b = int(input("entré la valeur de B"));

while a%b !=0 :
	a, b = b, a%b

print(b)

for i in range(2,43):
	a +=i;
print(a);
"""
"""
li = list()
li = [1,8,9,7,5,4998,4]
a=0
for i in li:
	a+=i
"""

t=[1,2,8,9,6,65]
#valeur de clé pour a comme pour un dictionnaire
ids="a"
#{} = type dict
while ids in t:
	ids = t[ids]

print(ids)

#compile te factorial of a number
def fact(nb):
	if(nb < 2):
		return 1
	else:
		return nb*fact(nb-1)

print(fact(3))
#help(fact)
