grammar Sentencia;

/* Reglas de la gramática */
sentencia   : ALL ID sentencia      #Forall
            | EXISTS ID sentencia   #Exists
            | exp                   #Expr
            ;

exp         : '(' exp ')'           #Paren
            | exp BICOND exp        #Bicondicional
            | exp IMPLY exp         #Cond
            | exp AND exp           #And
            | exp OR exp            #Or
            | NOT exp               #Neg
            | predicado             #Pred
            ;

predicado : PRED '(' (ID | PRED) ')'            #Preduni
          | PRED '('(ID|PRED)','(ID|PRED)')'    #Predmult
          ;

/* Definición de tokens */
ALL : '∀'|'all' ;
EXISTS : '∃'|'exists' ;
IMPLY : '=>' ;
BICOND : '<=>';
OR : '∨'|'OR' ;
AND : '∧'|'AND' ;
NOT : '-' ;
ID : [a-z] ;
PRED : [A-Z][a-zA-Z]* ;
WS : [ \t\n\r]+ -> skip ;

