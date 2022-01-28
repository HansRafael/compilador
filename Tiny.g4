grammar Tiny;

/*---------------- cometário PARSER INTERNALS ----------------*/

@parser::header
{if 1:
    counterIf = -1
    countElse = -1
    valueElse = False
    countFor = -1
    beginFor = 'BEGIN_FOR_'
    endFor = 'END_FOR_'

    symbol_table = []
    usedVars = []
    stackMax = 0
    stackCur = 0

    def plusCount(value):
        global countFor
        countFor += 1
    def emit(bytecode, delta):
        global stackMax
        global stackCur
        print(bytecode)
        stackCur += delta
        if (stackCur > stackMax):
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

EQ:     '==';
NE:     '!=';
LT:      '<';
LE:     '<=';
GT:      '>';
GE:     '>=';

PRINTLN:   'println'; 
FUNC:   'func'      ;
PACKAGE:   'package';
VAR:   'var'        ;
READ_INT: 'read_int';

FOR:  'for'         ;
IF: 'if';
ELSE: 'else';


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
    st_print | st_decl | st_attrib | st_for | st_if 
    ;

st_print:
    PRINTLN OP_PAR 
    {if 1:
        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', 1)
        #+1 na pilha
    }
    
    expression 

    {if 1:
    #-2 na pilha
        emit('    invokevirtual java/io/PrintStream/println(I)V\n', -2)
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
        store = '    istore ' + str(index) 
        emit(store, -1)
        #istore ==> -1 na pilha
    }
    ;

st_for:
    {if 1:
        localCount = countFor
        plusCount(countFor)
        localCount += 1
        print(beginFor + str(localCount) + ':')
    }
    FOR op = comparison
    {if 1:
        emit('    ' + $op.bytecode + ' ' + endFor + str(localCount),-2)
    }
    OP_CUR (statement )* CL_CUR
    {if 1:
        emit('    goto   ' + beginFor + str(localCount), 0)
        print(endFor + str(localCount) + ':')
    }
    ;

st_if:
    IF op = comparison
    {if 1:
        global valueElse
        global counterIf
        counterIf += 1
        localCount = counterIf
        hasElse = False
        emit('    ' + $op.bytecode + ' NOT_IF_' + str(localCount),-2)

    }

    OP_CUR (statement)* CL_CUR

    ( 
    {if 1:
        hasElse = True
        emit('    goto END_ELSE_' + str(localCount),0)
        print('NOT_IF_' + str(localCount) + ':')
    }

    ELSE OP_CUR (statement)* CL_CUR

    

    )?

    {if 1:
        if(hasElse):
            emit('END_ELSE_' + str(localCount) + ':',0)
        else:
            print('NOT_IF_' + str(localCount) + ':')
    }

;


comparison returns [bytecode]:
    expression op = ( EQ | NE | LT | LE | GT | GE) expression
    {if 1:

        if $op.type == TinyParser.EQ:
            $bytecode = 'if_icmpne'         #faz uma comparacao entre dois valores interios na pilha
        elif $op.type == TinyParser.NE:
            $bytecode = 'if_icmpeq'
        elif $op.type == TinyParser.LT:
            $bytecode = 'if_icmpge'
        elif $op.type == TinyParser.LE:
            $bytecode = 'if_icmpgt'     #fazer o inverso
        elif $op.type == TinyParser.GT:
            $bytecode = 'if_icmple'
        elif $op.type == TinyParser.GE:
            $bytecode = 'if_icmplt'
    
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
        store = '    istore ' + str(index) 
        emit(store, -1)
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
            emit('    iadd', -1)
        if $op.type == TinyParser.MINUS:
            emit('    isub', -1)
    }
    )*
    ;

term: factor ( op = (TIMES | OVER | REM) factor
    {if 1:
        #lcd,imul,idiv,irem ==> -1 na pilha
        if $op.type == TinyParser.TIMES:
            emit('    imul', -1)
        if $op.type == TinyParser.OVER:
            emit('    idiv', -1)
        if $op.type == TinyParser.REM:
            emit('    irem', -1)
            
    }
    )*
    ;

factor: NUMBER
    {if 1:
        #  emit('ldc ' + $NUMBER.text, 1)
        store = '    ldc ' + $NUMBER.text
        emit(store, 1)
        # symbol_table.append($NUMBER.text)
    }
    | OP_PAR expression CL_PAR
    | NAME
    {if 1:
        #verificar se NAME existe
        if $NAME.text in symbol_table:
            index = symbol_table.index($NAME.text)
            usedVars[index] = True
            emit('    iload ' + str(index), 1)
        #iload +1 ==> na piha aumenta, visto que carrega o valor 
        #se nao existe, gera erro e para
        else:
            print("error: Variable " + $NAME.text + " is not declared.")
            sys.exit()
    }

    | READ_INT OP_PAR CL_PAR
    {if 1:
        emit('    invokestatic Runtime/readInt()I', 1)
        #+1 na pilha
        #comando da biblioteca Runtime.java
    }

    ;


