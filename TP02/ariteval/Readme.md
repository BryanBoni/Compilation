# Compiling project
Here is the readme about 
all you need to know about this project.


## Developer 
#### Bryan Boni 11405588



## Functionality of the code (Arit2.g4)

### The grammar 
	PROG  		-> EXPR;
	PROG  		-> AFFECTATION;
	EXPR  		-> EXPR + TARTE
	EXPR  		-> TARTE
	TARTE 		-> TARTE * FRITE
	TARTE           -> TARTE / FRITE
	TARTE       	-> FRITE
	FRITE       	-> id
	FRITE       	-> int
	FRITE       	-> (EXPR)
	FRITE       	-> -FRITE
	AFFECTATION     -> id = EXPR

### The code
- the operations ' * ' and '/' are create at the end of
the grammar in order to be calculated first, 
following the rules of mathematics.

- right now the code does not treat doubles, 
only integers, even if it can treat division,
it will return an integer.

## How to use it
### Installation and first test
Open a prompt on the root of the project and type:
	
	* $ make ; python3 arit2.py testfiles/test01.txt
### Execution
In order to use the application type:

	* $ python3 arit2.py /dev/stdin
(to quit and see the results, use ctr+D twice)

### To do your own tests
Go on the folder "testfiles/" and create a text file 
and when you tape your comand to run the code, change projectTest01.txt"
by your text file, like this:

	* $ make ; python3 arit2.py testfiles/YourFile.txt
or to exexute more than one file type:

	* $ make tests
	
## Design choices


## Bugs 
### "normal" Bugs
- Dividing by 0 shutdown the application
-  
