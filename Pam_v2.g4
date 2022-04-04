grammar Pam_v2;

/**
Pamata Uzsākšanas Komanda
*/

progr               :       series;

/**
Pamata struktūras
*/

series              :       stmt (SEMICOLON stmt)*;
stmt                :       assign_stmt | input_stmt | output_stmt | cond_stmt | loop;
assign_stmt         :       VARNAME ':=' ( log_expr | expr);

/*
Read un Write struktūras
*/

input_stmt          :       'read' varlist;
output_stmt         :       'write' varlist;
varlist             :       VARNAME (',' VARNAME)*;

/*
If un While struktūras
*/

cond_stmt           :       'if' log_expr 'then' series ('else' series)? 'fi';
loop                :       'while' log_expr 'do' series 'end';

/**
Loģiskās saites: "and" "or", konjunkcija saista ciešāk par disjunkciju
*/

log_expr            :       log_term (DISCJUNCTION log_term)*;
log_term            :       log_elem (CONJUNCTION log_elem)*;
log_elem            :       (NOT)? ( condition | BOOL | LPARENTHESIS log_expr RPARENTHESIS | VARNAME );

/**
Negācijas nodrošinājums
*/

condition           :       expr RELATION expr;

/**
Pamata matemātiskās darbības: "+"  "-"  "*"  "/"
*/

expr		        :	    term (WEAKOP term)*;
term		        :	    elem (STRONGOP elem)*;
elem		        :	    NUMBER | VARNAME | LPARENTHESIS expr RPARENTHESIS;

/**
Variables
*/

//NEWLINE	            :	    '\r' ? '\n';
WEAKOP		        :	    '+' | '-';
STRONGOP	        :	    '*' | '/';
RELATION	        :	    '<>' | '=<' | '>='| '=' | '<' | '>';
BOOL                :       'True' | 'False';
CONJUNCTION         :       'and';
DISCJUNCTION        :       'or';
NOT                 :       'not';
SEMICOLON           :       ';';
LPARENTHESIS         :       '(';
RPARENTHESIS         :       ')';

NUMBER		        :	    [1-9][0-9]* ;
VARNAME	            :	    ([a-z]|[A-Z]|'_') ([a-z]|[A-Z]|[0-9]|'_')*;

WS      		    :       [ \t\r\n]+ -> skip;
