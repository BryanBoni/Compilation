//define a tiny grammar for arith expressions with identifiers

grammar wf;

r: expr ';' ;

expr: expr op expr
    | ID {print('oh an id : '+$ID.text);}
    | paranthese
    | INT 
    ;
paranthese : '[' expr ']'
	| '(' expr ')'
	;

op : '+'| '*' | '-' | '/' ;
INT :   '0'..'9'+ ;
ID :   ('a'..'z'|'A'..'Z')+ ;
WS : [ \t\r\n]+ -> skip ;          // skip spaces, tabs, newlines
