//grammar Pam;
//
//progr 		    :	    series NEWLINE;
//series		    : 	    stmt (';' stmt)*;
//
//stmt		    :	    input_stmt | output_stmt | assign_stmt | cond_stmt | loop;
//input_stmt	    :	    'read' varlist;
//output_stmt	    :	    'write' varlist;
//assign_stmt	    :	    VARNAME ':=' expr;
//cond_stmt	    :	    'if' compar_stmt 'then' series ('else' series)?  'fi';
//loop		    :	    'while' compar_stmt 'do' series 'od';
//
//compar_stmt     :       comparison (condis comparison)*;
//condis          :       CONJUNCTION | DISCJUNCTION;
//comparison      :       (NOT)? compar | (NOT)? BOOL;
//compar		    :	    expr RELATION expr;
//
//
//varlist		    :	    VARNAME (',' VARNAME)*;
//expr		    :	    term (WEAKOP term)*;
//term		    :	    elem (STRONGOP elem)*;
//elem		    :	    NUMBER | VARNAME | '(' expr ')' | BOOL;
//
//NEWLINE	        :	    '\r' ? '\n';
//WEAKOP		    :	    '+' | '-';
//STRONGOP	    :	    '*' | '/';
//RELATION	    :	    '<>' | '=<' | '>='| '=' | '<' | '>';
//BOOL            :       'true' | 'false';
//CONJUNCTION     :       'and';
//DISCJUNCTION    :       'or';
//NOT             :       'not';
//NUMBER		    :	    [1-9][0-9]* ;
//VARNAME	        :	    ([a-z]|[A-Z]|'_') ([a-z]|[A-Z]|[0-9]|'_')*;
//WS      		:       [ \t\r\n]+ -> skip;

/**
Pamata Uzsākšanas Komanda
*/

<progr>               ::= <series>

/**
Pamata struktūras
*/

<series>              ::= <stmt> |  <series><SEMICOLON> <stmt>
<stmt>                ::= <assign_stmt> | <input_stmt> | <output_stmt> | <cond_stmt> | <loop>
<assign_stmt>         ::= <VARNAME> := <expr>

/*
Read un Write struktūras
*/

<input_stmt>          ::= read <varlist>
<output_stmt>         ::= write <varlist>
<varlist>             ::= <VARNAME> | <varlist> , <VARNAME>

/*
If un While struktūras
*/

<cond_stmt>           ::= if <log_expr> then <series> fi | if <log_expr> then <series> else <series> fi
<loop>                ::= while <log_expr> do <series> end

/**
Loģiskās saites: "and" "or", konjunkcija saista ciešāk par disjunkciju
*/

<log_expr>            ::= <log_term> | <log_expr><DISCJUNCTION><log_term>
<log_term>            ::= <log_elem> | <log_term><DISCJUNCTION><log_expr>
<log_elem>            ::= <condition> | <BOOL> | <NOT BOOL> | ( <log_expr> )

/**
Negācijas nodrošinājums
*/

<condition>           ::= <pos_condition> | <neg_condition>
<neg_condition>       ::= <NO><pos_condition>
<pos_condition>       ::= <expr><RELATION><expr>

/**
Pamata matemātiskās darbības: "+"  "-"  "*"  "/"
*/

<expr>		          ::= <term> | <expr><WEAKOP><term>
<term>		          ::= <elem>| <term><STRONGOP><elem>
<elem>		          ::= <NUMBER> | <VARNAME> | (<expr>) | <BOOL>;

/**
Variables
*/

<WEAKOP>  		      ::= + | -
<STRONGOP>	          ::= * | /
<RELATION>	          ::= <> | =< | >= | = | < | >
<BOOL>                ::= true | false
<CONJUNCTION>         ::= and
<DISCJUNCTION>        ::= or
<NOT>                 ::= not
<SEMICOLON>           ::= ;

<WS>      		      ::= [ \t\r\n]+ -> skip;

<CHARNUM>             ::= <CHAR> | <NUMBER>
<CHAR>                ::= <LETTER> | _

<NUMBER>		      ::= <DIGIT> | <NUMBER><DIGIT>
<VARNAME>	          ::= <CHAR> | <VARNAME><CHARNUM>

<DIGIT>               ::= 0 | 1 | ... | 9
<LETTER>              ::= a | b | ... | z


<var> ::= <letter> | <var><letter>