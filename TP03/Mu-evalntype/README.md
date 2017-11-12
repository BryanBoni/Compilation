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
make run FOO=../ex/test01.mu for a single run
make tests to test all the file in ex/ according to EXPECTED results (you can select the files you want to test by modifying the variable ALL\_FILES in test\_evaluator.py)

## how to use it

## Design choices
- for the unassigned value used in a log I chose to print :varName + "has no value yet!" and raise an exception.

## Bugs

##Exercice 6

 if b then S1 else S2  
 							let v = b.visit()
 							#if the condition is false, then jump to else
 							if v == 1:
 								S1.visit() #then 
 							else:
 								S2.visit() #else

while b to S done
							#réevalue la valeur de b à chaque boucle pour pouvoir sortir.
							while b.visit() == 1:
								S.visit()