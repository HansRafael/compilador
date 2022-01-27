grammar Tiny;

/*---------------- cometário PARSER INTERNALS ----------------*/

@parser::header
{if 1:
    symbol_table = []
    usedVars = []
    stackMax = 10
    stackCur = 0

    def emit(bytecode, delta):
        print('    ' + bytecode)
        stackCur += delta
        if stackCur > stackMax:
            stackMax = stackCur
        #imprimir bytecode
        #atualizar 
    
}

/*----------------  FUNCTIONS ----------------*/


/*---------------- LEXER RULES ----------------*/

PLUS:   '+';
MINUS:  '-';
TIMES:  '*';
OVER:  '/' ;
REM:  '%'  ;
OP_PAR: '(' ;
CL_PAR: ')' ;
OP_CUR: '{' ;
CL_CUR: '}' ;
ATTRIB: '=' ;

PRINTLN:   'println'; 
FUNC:   'func'      ;
PACKAGE:   'package';
VAR:   'var'        ;
READ_INT: 'read_int';
MAIN:   'main'      ;

NUMBER: '0'..'9'+ ;
NAME  : 'a'..'z'+ ; //string

SPACE: (' '|'\t'|'\r'|'\n')+ -> skip ;
COMMENT: '//' ~('\n')*       -> skip ;

/*---------------- PARSER RULES ----------------*/

program:
    PACKAGE MAIN
    {if 1:
        print('.source Test.src')
        print('.class  public Test')
        print('.super  java/lang/Object\n')
        print('.method public <init>()V')
        print('    aload_0')
        print('    invokenonvirtual java/lang/Object/<init>()V')
        print('    return')
        print('.end method\n')
    }
    main
    ;

        
main:
    FUNC MAIN OP_PAR CL_PAR OP_CUR
    {if 1:
        print('.method public static main([Ljava/lang/String;)V\n')
    }
    (statement )*
    {if 1:
        aux = False
        for i in range (len(usedVars)):
            if (usedVars[i] == False):
                print("Warning: " + symbol_table[i] + " is defined but never used")
                aux = True
        if aux:
            sys.exit()
        print('    return')
        print('.limit stack ' + str(stackMax))
        if len(symbol_table):
            print('.limit locals',(len(symbol_table)))
        print('.end method')
        print('\n; symbol_table:', symbol_table)
        print('\n; usedVars:', usedVars)
    }
    CL_CUR
    ;

statement:
    st_print | st_decl | st_attrib
    ;

st_print:
    PRINTLN OP_PAR 
    {if 1:
        print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
        #+1 na pilha
    }
    
    expression 

    {if 1:
    #-2 na pilha
    print('    invokevirtual java/io/PrintStream/println(I)V\n')
    }
    
    CL_PAR
    ;

st_decl:
    VAR NAME
    {if 1:
        if (len(symbol_table) == 0):
            symbol_table.append($NAME.text)
        else:
            if $NAME.text in symbol_table:
                print("Variable " + $NAME.text + " redeclared in this block.")
                sys.exit()
            else:
                symbol_table.append($NAME.text)

        #se existe, gera erro de redeclaracao e para
    }
    ATTRIB expression 
    {if 1:
        index = symbol_table.index($NAME.text)
        usedVars.append(False)
        print('    istore ' + str(index))
        #istore ==> -1 na pilha
    }
    ;

st_attrib: //atribui a uma variavel
    NAME 
    {if 1:
        if $NAME.text in symbol_table:
            pass
        else:
            print("error: Variable " + $NAME.text + " is not declared.")
            sys.exit()
    }
    ATTRIB expression
    {if 1:
        index = symbol_table.index($NAME.text)
        print('    istore ' + str(index))
    }
    ;

/* ()? ->> valor é opcional 0 ou 1 vez */
/* ()* ->> valor repete     0 ou mais vezes */
/* ()+ ->> valor repete     1 ou mais vezes */
/* dessa maneira, faz o agrupamento a esquerda primeiro  (associatividade)*/
expression: /*guarda a variavel OP  */
    term ( op = (PLUS | MINUS) term
    {if 1:
        if $op.type == TinyParser.PLUS:
            print('    iadd')
        if $op.type == TinyParser.MINUS:
            print('    isub')
    }
    )*
    ;

term: factor ( op = (TIMES | OVER | REM) factor
    {if 1:
        #lcd,imul,idiv,irem ==> -1 na pilha
        if $op.type == TinyParser.TIMES:
            print('    imul')
        if $op.type == TinyParser.OVER:
            print('    idiv')
        if $op.type == TinyParser.REM:
            print('    irem')
    }
    )*
    ;

factor: NUMBER
    {if 1:
        #  emit('ldc ' + $NUMBER.text, +1)
        print('    ldc ' + $NUMBER.text)
        # symbol_table.append($NUMBER.text)
    }
    | OP_PAR expression CL_PAR
    | NAME
    {if 1:
        #verificar se NAME existe
        if $NAME.text in symbol_table:
            index = symbol_table.index($NAME.text)
            usedVars[index] = True
            print('    iload ' + str(index))
        #iload +1 ==> na piha aumenta, visto que carrega o valor 
        #se nao existe, gera erro e para
        else:
            print("error: Variable " + $NAME.text + " is not declared.")
            sys.exit()
    }

    | READ_INT OP_PAR CL_PAR
    {if 1:
        print('    invokestatic Runtime/readInt()I')
        #+1 na pilha
        #comando da biblioteca Runtime.java
    }

    ;
