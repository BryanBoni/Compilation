grammar Arit2;

// MIF08@Lyon1, LAB 02, arit evaluator

// Header in Python, comment it out to use grun
@header {
# header - mettre les variables globales 
import sys
idTab = {};

class UnknownIdentifier(Exception):
    pass
}

prog: 
    (expr ';' {print($expr.text + "=" +str($expr.output));} 
    | affectation ';')*;

expr returns [INT output]: 
    e1=expr '+' t1=tarte {$output=$e1.output + $t1.output;} 
    | e1=expr '-' t1=tarte {$output=$e1.output - $t1.output;}
    | t1=tarte {$output = $t1.output;}
    ;

tarte returns [INT output]:
    t1=tarte '*' f1=frite {$output = $t1.output * $f1.output;}
    | t1=tarte '/' f1=frite 
    {$output = $t1.output / $f1.output;}
    | f1=frite {$output = $f1.output;}
    ;

frite returns [INT output]: 
    id1=ID 
    {if ($id1.text not in idTab):
    raise UnknownIdentifier($id1.text);
else:
    $output = idTab[$id1.text];}
    | INT {$output = (int) $INT.text;}
    | '(' expr ')' {$output = $expr.output;}
    | '-' frite {$output = -$frite.output;}
    ;

affectation :
    id1=ID '=' e1=expr {idTab[$id1.text]= $e1.output; print($id1.text + "now equals" + str($e1.output));}
    ;

COMMENT: '#' ~[\r\n]* -> skip;

ID : ('a'..'z'|'A'..'Z')+;
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
INT: '0'..'9'+;
NEWLINE: [\n]+; 
