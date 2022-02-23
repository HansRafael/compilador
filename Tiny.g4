grammar Tiny;

/*---------------- cometário PARSER INTERNALS ----------------*/
/*---------------- HANS RAFAEL RUEBENICH 132775 ----------------*/
/*------------------------  FUNCTIONS ----------------------------*/

@parser::header
{if 1:
    counterIf = -1
    countFor = -1
    beginFor = 'BEGIN_FOR_'
    endFor = 'END_FOR_'

    symbol_table = []
    type_table = []
    func_table = []
    usedVars = []
    stackMax = 0
    stackCur = 0

    def plusCount(value):
        global countFor
        countFor += 1
    def emit(bytecode, delta):
        global stackMax
        global stackCur
        global counterIf
        global countFor
        print(bytecode)
        stackCur += delta
        if(delta == -5):
            stackMax = 0
            stackCur = 0
            counterIf = -1
            countFor = -1
        elif (stackCur > stackMax):
            stackMax = stackCur
        #imprimir bytecode
        #atualizar 
    
}

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
READ_STR: 'read_str';
RETURN: 'return'    ;

FOR:  'for'         ;
IF: 'if';
ELSE: 'else';


MAIN:   'main'      ;
FUNCTION: 'function';
INT: 'int'          ;

NUMBER: '0'..'9'+ ;
NAME  : 'a'..'z'+ ; 
STRING: '"' ~('"')* '"';//string

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
    (function)*
    main
    ;


function:
    FUNC NAME OP_PAR
    {if 1:
        if $NAME.text in func_table:
            print("error: function " + $NAME.text + " already declared",file=sys.stderr)
        else:
            print('.method public static ' + $NAME.text +'(I)I\n')
            func_table.append($NAME.text)
    }
    NAME
    {if 1:
        symbol_table.append($NAME.text)
        usedVars.append(False)
        type_table.append('i')
    } 
    
    INT CL_PAR INT OP_CUR 

    (e = statement)* 
    {if 1:
        if($e.type == 'function'):
            aux = False

            for i in range (len(usedVars)):
                if (usedVars[i] == False):
                    print("Warning: " + symbol_table[i] + " is defined but never used",file=sys.stderr)

                    aux = True
            if ($e.type == 'error'):
                sys.exit()

            print('    return')
            print('.limit stack ' + str(stackMax))
            if len(symbol_table):
                print('.limit locals',(len(symbol_table)))
            print('.end method')
            print('; symbol_table:', symbol_table)
            print('; type_table:', type_table)
            print('; usedVars:', usedVars)
            
            emit(' ',-5)
            symbol_table.clear()
            type_table.clear()
            usedVars.clear()
        else:
            print('error: missing return statement in function',file=sys.stderr)
        
        
    }
    
    CL_CUR
    ;
        
main:
    FUNC MAIN OP_PAR CL_PAR OP_CUR
    {if 1:
        print('.method public static main([Ljava/lang/String;)V\n')
    }
    (e = statement )*
    {if 1:
        if($e.type != 'function'):
            aux = False

            for i in range (len(usedVars)):
                if (usedVars[i] == False):
                    print("Warning: " + symbol_table[i] + " is defined but never used",file=sys.stderr)

                    aux = True
            if ($e.type == 'error'):
                sys.exit()

            print('    return')
            print('.limit stack ' + str(stackMax))
            if len(symbol_table):
                print('.limit locals',(len(symbol_table)))
            print('.end method')
            print('\n; symbol_table:', symbol_table)
            print('; type_table:', type_table)
            print('; usedVars:', usedVars)
            print('; func_table:', func_table)
        elif($e.type == 'function'):
            print('error: return statement cannot be used inside main',file=sys.stderr)
            sys.exit()
    }
    CL_CUR
    ;

statement returns[type]:
    st_print | st_decl | st_attrib | st_for | st_if | ef = st_return
    {if 1:
        $type = $ef.typeFuc
    }
    ;

st_print:
    PRINTLN OP_PAR 
    {if 1:
        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', 1)
        #+1 na pilha
    }
    
    e = expression 


    {if 1:
        if ($e.type == 'i'):
            emit('    invokevirtual java/io/PrintStream/println(I)V\n', -2)
            
        elif ($e.type == 's'):
            emit('    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V\n', -2)
        else:
            print($e.type)
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
                print("Variable " + $NAME.text + " redeclared in this block.",file=sys.stderr)
                sys.exit()
            else:
                symbol_table.append($NAME.text)

        #se existe, gera erro de redeclaracao e para
    }
    ATTRIB e = expression 

    {if 1:
        if($e.type == 'i'):            #type of int
            index = symbol_table.index($NAME.text)
            usedVars.append(False)
            type_table.append('i')
            store = '    istore ' + str(index)  + '\n'
            emit(store, -1)            #istore ==> -1 na pilha
                                       
        if($e.type == 's'):            #type of string
            index = symbol_table.index($NAME.text)
            type_table.append('s')
            usedVars.append(False)
            store = '    astore ' + str(index) + '\n'
            emit(store, -1)
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
        if $op.bytecode == 'error':
            print('error: FOR operands must be integers!!!',file=sys.stderr)
            sys.exit()
        else:
            emit('    ' + $op.bytecode + ' ' + endFor + str(localCount),-2)
    }
    OP_CUR (statement )* CL_CUR
    {if 1:
        emit('    goto   ' + beginFor + str(localCount), 0)
        print(endFor + str(localCount) + ':')
    }
    ;


st_return returns[typeFuc]:  
    RETURN e = expression
    {if 1:
        if($e.type == 'i'):
            emit('    ireturn',-1)
            $typeFuc = 'function'
        elif($e.type == 's'):
            print('error: return value must be of integer type',file=sys.stderr)
            $typeFuc = 'function'
        
    }
    ;

st_if returns[type]:
    IF op = comparison
    {if 1:
        if $op.bytecode == 'error':
            print('error: IF operands must be integers!!!',file=sys.stderr)
            $type = 'error'
            sys.exit()
        else:
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
    e1 = expression op = ( EQ | NE | LT | LE | GT | GE) e2 = expression
    {if 1:
        if($e1.type == 'i' and $e2.type == 'i'):
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
        else:
            $bytecode = 'error'
            
    
    }
    ;

st_attrib returns[type]: //atribui a uma variavel
    NAME 
    {if 1:
        if $NAME.text in symbol_table:
            pass
        else:
            print("error: Variable " + $NAME.text + " is not declared.",file=sys.stderr)
            sys.exit()
    }
    ATTRIB e = expression
    {if 1:
        index = symbol_table.index($NAME.text)
        if($e.type == 'i' and type_table[index] == 'i'):
            usedVars[index] = True
            emit('    istore ' + str(index), -1)
    
        elif($e.type == 's' and type_table[index] == 'i'):
            store = 'error: ' + $NAME.text + ' is a integer\n'
            print(store ,file=sys.stderr)
        
        elif($e.type == 's' and type_table[index] == 's'):
            usedVars[index] = True
            emit('    astore ' + str(index), -1)
        
        elif($e.type == 'i' and type_table[index] == 's'):
            store = 'error: ' + $NAME.text + ' is a string\n'
            print(store ,file=sys.stderr)



    }
    ;

/* ()? ->> valor é opcional 0 ou 1 vez */
/* ()* ->> valor repete     0 ou mais vezes */
/* ()+ ->> valor repete     1 ou mais vezes */
/* dessa maneira, faz o agrupamento a esquerda primeiro  (associatividade)*/

expression returns[type]: /*guarda a variavel OP  */
    t1 = term ( op = (PLUS | MINUS) t2 = term
    {if 1:
        if($t1.type == 'i' and $t2.type == 'i'):
            if $op.type == TinyParser.PLUS:
                emit('    iadd', -1)
            if $op.type == TinyParser.MINUS:
                emit('    isub', -1)
        else:
            $type = 'error'
            print('error: (+ and -) operands must be integers',file=sys.stderr)
    }
    )*
    {if 1:
        $type = $t1.type
    }
    ;

term returns [type]: f1 = factor ( op = (TIMES | OVER | REM) f2 = factor
    {if 1:
        if($f1.type == 'i' and $f2.type == 'i'):    
            #lcd,imul,idiv,irem ==> -1 na pilha
            if $op.type == TinyParser.TIMES:
                emit('    imul', -1)
            if $op.type == TinyParser.OVER:
                emit('    idiv', -1)
            if $op.type == TinyParser.REM:
                emit('    irem', -1)
        else:
            $type = 'error'
            print('error: (* , / and %) operands must be integers!',file=sys.stderr)
    }
    )*
    {if 1:
        $type = $f1.type

    }
    ;

factor returns [type]: NUMBER
    {if 1:
        store = '    ldc ' + $NUMBER.text
        emit(store, 1)

        $type = 'i'
        # essa regra resultou em 'inteiro'
    }
    | OP_PAR e = expression CL_PAR
    {if 1:
        $type = $e.type

    }
    |

    NAME OP_PAR e = expression CL_PAR
    {if 1:
        if($NAME.text in func_table):
            emit('    invokestatic Test/'+$NAME.text+'(I)I',0)
            $type = $e.type
            if($e.type == 's'):
                print("error: argument must be integer",file=sys.stderr)
        else:
            print("error: function " + $NAME.text + " not declared",file=sys.stderr)

        
    }

    | NAME
    {if 1:
        #verificar se NAME existe
        if $NAME.text in symbol_table:
            index = symbol_table.index($NAME.text)
            typeValue = type_table[index]

            if(typeValue == 'i'):
                usedVars[index] = True
                emit('    iload ' + str(index), 1)
                $type = 'i'

            elif(typeValue == 's'):
                usedVars[index] = True
                emit('    aload ' + str(index), 1)
                $type = 's'

        #iload +1 ==> na piha aumenta, visto que carrega o valor 
        #se nao existe, gera erro e para
        else:
            print("error: Variable " + $NAME.text + " is not declared.",file=sys.stderr)
            sys.exit()

        #verificar o tipo na tabela de tipos
        # $type = 'i' ou $type = 's'
        #$type = ???
    }

    | READ_INT OP_PAR CL_PAR
    {if 1:
        emit('    invokestatic Runtime/readInt()I', 1)
        #+1 na pilha
        #comando da biblioteca Runtime.java
        $type = 'i'
    }
    | STRING

    {if 1:
        store = '    ldc  ' + $STRING.text
        emit(store, 1)
        $type = 's'
        

    }
    //ldc $STRING.text
    // $type = 's'
    | READ_STR OP_PAR CL_PAR
    {if 1:
        emit('    invokestatic Runtime/readString()Ljava/lang/String;', 1)
        $type = 's'
    }
    // emit('    invokestatic Runtime/readString()Ljava/lang/String', 1)


    ;


