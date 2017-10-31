#Compiling project
	Here is the readme about 
	all you need to know about this project.


## Developer 
	Bryan Boni 11405588



## Functionality of the code (Arit2.g4)

### The grammar 
	PROG  		-> EXPR;
	PROG  		-> AFFECTATION;
	EXPR  		-> EXPR + TARTE
	EXPR  		-> TARTE
	TARTE 		-> TARTE * FRITE
	TARTE       -> TARTE / FRITE
	TARTE       -> FRITE
	FRITE       -> id
	FRITE       -> int
	FRITE       -> (EXPR)
	FRITE       -> -FRITE
	AFFECTATION -> id = EXPR

### The code
<p>
	- the operations ' * ' and '/' are create at the end of
	the grammar in order to be calculated first, 
	following the rules of mathematics 

	- right now the code does not treat doubles, 
	only integers, even if it can treat division, 
	it will return an integer
</p>

## How to use it
### Execution
	Open a prompt on the root of the project and tape:
	- $ make ; python3 arit2.py testfiles/projectTest01.txt
### To do your own tests
	Go on the folder "testfiles/" and create a text file 
	and when you tape your comand to run the code, change projectTest01.txt"
	by your text file, like this:
	- $ make ; python3 arit2.py testfiles/YourFile.txt

	
## Design choices


## Bugs 
### "normal" Bugs
<p>
	- Dividing by 0 shutdown the application
	- 
</p> 