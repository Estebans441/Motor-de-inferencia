grammar Sentencia;

/* Reglas de la gramática */
sentencia   : ALL ID sentencia      #Forall
            | EXISTS ID sentencia   #Exists
            | exp                   #Expr
            ;

exp         : exp BICOND exp        #Bicond
            | exp IMPLY exp         #Impl
            | '(' exp ')'           #Paren
            | exp AND exp           #And
            | exp OR exp            #Or
            | NOT exp               #Neg
            | predicado             #Pred
            ;

predicado : PRED '(' op=(ID | PRED) ')'     #Uni
          | PRED '('ID','ID')'              #IDID
          | PRED '('ID','PRED')'            #IDP
          | PRED '('PRED','ID')'            #PID
          | PRED '('PRED','PRED')'          #PP
          ;

/* Definición de tokens */
ALL : '∀'|'/all' ;
EXISTS : '∃'|'/exists' ;
IMPLY : '=>' ;
BICOND : '<=>';
OR : '∨'|'/or' ;
AND : '∧'|'/and' ;
NOT : '-' ;
ID : [a-z] ;
PRED : [A-Z][a-zA-Z]* ;
WS : [ \t\n\r]+ -> skip ;

