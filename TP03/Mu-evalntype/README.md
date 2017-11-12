# Mu-evulator project
## Developper
Bryan Boni 11405588

## Contents
The folowing archive contain:
	- "../ex/" contains example files and unit test (for the functions that 
		as been added in "MyMuVisitor.py"),
	- Mu.g4 : the gammar for the Mu language,
	- MyMuVisitor.py : contains a code folowing the visitor pattern in order 
		to add verification and behavior,
	- MyMuTypingVisitor.py : same as MyMuVisitor with a Mu verificator goal 
		for a given Mu file,
	- Main.py,
	- test_evaluator.py,


## Code functionnality


## how to use it
make run FOO=../ex/test01.mu for a single run
make tests to test all the file in ex/ according to EXPECTED results 
(you can select the files you want to test by modifying the variable ALL\_FILES in test\_evaluator.py)

## Design choices
- for the unassigned value used in a log I chose to print :varName + "has no value yet!" and raise an exception.

## Bugs


## Exercice 6
<table>
<td>if b then S1 else S2 </td>
<td>
	let v = b.visit() <br />
 	#if the condition is false, then jump to else <br />
 	if v == 1:	<br/>
 		  S1.visit() #then <br /> 
 	else:<br />
 		  S2.visit() #else <br />
</td>
</table>
<table>
<td>while b to S done</td>
<td>
	#réevalue la valeur de b à chaque boucle pour pouvoir sortir. <br />
	while b.visit() == 1:	<br />
		S.visit()	<br />
</td>
</table>
