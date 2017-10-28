PACKAGE = wf
MAINFILE = main
ANTLR4 = java -jar $(HOME)/lib/antlr-4.7-complete.jar

all: $(PACKAGE).g4
	$(ANTLR4) $^ -Dlanguage=Python3

run: $(MAINFILE).py
	python3 $^

clean:
	rm -rf *~ $(PACKAGE)*.py $(PACKAGE)*.pyc *.tokens  __pycache*
