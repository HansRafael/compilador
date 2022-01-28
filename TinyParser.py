# Generated from Tiny.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

if 1:
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
    


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\37")
        buf.write("\u0098\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\'\n\3")
        buf.write("\f\3\16\3*\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\64")
        buf.write("\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7J\n\7\f\7\16\7M\13\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\7\bW\n\b\f\b\16\bZ\13")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\7\ba\n\b\f\b\16\bd\13\b\3\b\5\b")
        buf.write("g\n\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\7\13{\n\13\f\13\16\13~\13")
        buf.write("\13\3\f\3\f\3\f\3\f\3\f\7\f\u0085\n\f\f\f\16\f\u0088\13")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r")
        buf.write("\u0096\n\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2")
        buf.write("\5\3\2\r\22\3\2\3\4\3\2\5\7\2\u0099\2\32\3\2\2\2\4\37")
        buf.write("\3\2\2\2\6\63\3\2\2\2\b\65\3\2\2\2\n<\3\2\2\2\fC\3\2\2")
        buf.write("\2\16Q\3\2\2\2\20j\3\2\2\2\22o\3\2\2\2\24u\3\2\2\2\26")
        buf.write("\177\3\2\2\2\30\u0095\3\2\2\2\32\33\7\25\2\2\33\34\7\33")
        buf.write("\2\2\34\35\b\2\1\2\35\36\5\4\3\2\36\3\3\2\2\2\37 \7\24")
        buf.write("\2\2 !\7\33\2\2!\"\7\b\2\2\"#\7\t\2\2#$\7\n\2\2$(\b\3")
        buf.write("\1\2%\'\5\6\4\2&%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2")
        buf.write("\2)+\3\2\2\2*(\3\2\2\2+,\b\3\1\2,-\7\13\2\2-\5\3\2\2\2")
        buf.write(".\64\5\b\5\2/\64\5\n\6\2\60\64\5\22\n\2\61\64\5\f\7\2")
        buf.write("\62\64\5\16\b\2\63.\3\2\2\2\63/\3\2\2\2\63\60\3\2\2\2")
        buf.write("\63\61\3\2\2\2\63\62\3\2\2\2\64\7\3\2\2\2\65\66\7\23\2")
        buf.write("\2\66\67\7\b\2\2\678\b\5\1\289\5\24\13\29:\b\5\1\2:;\7")
        buf.write("\t\2\2;\t\3\2\2\2<=\7\26\2\2=>\7\35\2\2>?\b\6\1\2?@\7")
        buf.write("\f\2\2@A\5\24\13\2AB\b\6\1\2B\13\3\2\2\2CD\b\7\1\2DE\7")
        buf.write("\30\2\2EF\5\20\t\2FG\b\7\1\2GK\7\n\2\2HJ\5\6\4\2IH\3\2")
        buf.write("\2\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2LN\3\2\2\2MK\3\2\2\2")
        buf.write("NO\7\13\2\2OP\b\7\1\2P\r\3\2\2\2QR\7\31\2\2RS\5\20\t\2")
        buf.write("ST\b\b\1\2TX\7\n\2\2UW\5\6\4\2VU\3\2\2\2WZ\3\2\2\2XV\3")
        buf.write("\2\2\2XY\3\2\2\2Y[\3\2\2\2ZX\3\2\2\2[f\7\13\2\2\\]\b\b")
        buf.write("\1\2]^\7\32\2\2^b\7\n\2\2_a\5\6\4\2`_\3\2\2\2ad\3\2\2")
        buf.write("\2b`\3\2\2\2bc\3\2\2\2ce\3\2\2\2db\3\2\2\2eg\7\13\2\2")
        buf.write("f\\\3\2\2\2fg\3\2\2\2gh\3\2\2\2hi\b\b\1\2i\17\3\2\2\2")
        buf.write("jk\5\24\13\2kl\t\2\2\2lm\5\24\13\2mn\b\t\1\2n\21\3\2\2")
        buf.write("\2op\7\35\2\2pq\b\n\1\2qr\7\f\2\2rs\5\24\13\2st\b\n\1")
        buf.write("\2t\23\3\2\2\2u|\5\26\f\2vw\t\3\2\2wx\5\26\f\2xy\b\13")
        buf.write("\1\2y{\3\2\2\2zv\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2")
        buf.write("}\25\3\2\2\2~|\3\2\2\2\177\u0086\5\30\r\2\u0080\u0081")
        buf.write("\t\4\2\2\u0081\u0082\5\30\r\2\u0082\u0083\b\f\1\2\u0083")
        buf.write("\u0085\3\2\2\2\u0084\u0080\3\2\2\2\u0085\u0088\3\2\2\2")
        buf.write("\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\27\3\2")
        buf.write("\2\2\u0088\u0086\3\2\2\2\u0089\u008a\7\34\2\2\u008a\u0096")
        buf.write("\b\r\1\2\u008b\u008c\7\b\2\2\u008c\u008d\5\24\13\2\u008d")
        buf.write("\u008e\7\t\2\2\u008e\u0096\3\2\2\2\u008f\u0090\7\35\2")
        buf.write("\2\u0090\u0096\b\r\1\2\u0091\u0092\7\27\2\2\u0092\u0093")
        buf.write("\7\b\2\2\u0093\u0094\7\t\2\2\u0094\u0096\b\r\1\2\u0095")
        buf.write("\u0089\3\2\2\2\u0095\u008b\3\2\2\2\u0095\u008f\3\2\2\2")
        buf.write("\u0095\u0091\3\2\2\2\u0096\31\3\2\2\2\13(\63KXbf|\u0086")
        buf.write("\u0095")
        return buf.getvalue()


class TinyParser ( Parser ):

    grammarFileName = "Tiny.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", 
                     "')'", "'{'", "'}'", "'='", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'println'", "'func'", "'package'", 
                     "'var'", "'read_int'", "'for'", "'if'", "'else'", "'main'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "TIMES", "OVER", "REM", 
                      "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", 
                      "EQ", "NE", "LT", "LE", "GT", "GE", "PRINTLN", "FUNC", 
                      "PACKAGE", "VAR", "READ_INT", "FOR", "IF", "ELSE", 
                      "MAIN", "NUMBER", "NAME", "SPACE", "COMMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_decl = 4
    RULE_st_for = 5
    RULE_st_if = 6
    RULE_comparison = 7
    RULE_st_attrib = 8
    RULE_expression = 9
    RULE_term = 10
    RULE_factor = 11

    ruleNames =  [ "program", "main", "statement", "st_print", "st_decl", 
                   "st_for", "st_if", "comparison", "st_attrib", "expression", 
                   "term", "factor" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    TIMES=3
    OVER=4
    REM=5
    OP_PAR=6
    CL_PAR=7
    OP_CUR=8
    CL_CUR=9
    ATTRIB=10
    EQ=11
    NE=12
    LT=13
    LE=14
    GT=15
    GE=16
    PRINTLN=17
    FUNC=18
    PACKAGE=19
    VAR=20
    READ_INT=21
    FOR=22
    IF=23
    ELSE=24
    MAIN=25
    NUMBER=26
    NAME=27
    SPACE=28
    COMMENT=29

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PACKAGE(self):
            return self.getToken(TinyParser.PACKAGE, 0)

        def MAIN(self):
            return self.getToken(TinyParser.MAIN, 0)

        def main(self):
            return self.getTypedRuleContext(TinyParser.MainContext,0)


        def getRuleIndex(self):
            return TinyParser.RULE_program




    def program(self):

        localctx = TinyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(TinyParser.PACKAGE)
            self.state = 25
            self.match(TinyParser.MAIN)
            if 1:
                    print('.source Test.src')
                    print('.class  public Test')
                    print('.super  java/lang/Object\n')
                    print('.method public <init>()V')
                    print('    aload_0')
                    print('    invokenonvirtual java/lang/Object/<init>()V')
                    print('    return')
                    print('.end method\n')
                
            self.state = 27
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(TinyParser.FUNC, 0)

        def MAIN(self):
            return self.getToken(TinyParser.MAIN, 0)

        def OP_PAR(self):
            return self.getToken(TinyParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(TinyParser.CL_PAR, 0)

        def OP_CUR(self):
            return self.getToken(TinyParser.OP_CUR, 0)

        def CL_CUR(self):
            return self.getToken(TinyParser.CL_CUR, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyParser.StatementContext)
            else:
                return self.getTypedRuleContext(TinyParser.StatementContext,i)


        def getRuleIndex(self):
            return TinyParser.RULE_main




    def main(self):

        localctx = TinyParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(TinyParser.FUNC)
            self.state = 30
            self.match(TinyParser.MAIN)
            self.state = 31
            self.match(TinyParser.OP_PAR)
            self.state = 32
            self.match(TinyParser.CL_PAR)
            self.state = 33
            self.match(TinyParser.OP_CUR)
            if 1:
                    print('.method public static main([Ljava/lang/String;)V\n')
                
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.PRINTLN) | (1 << TinyParser.VAR) | (1 << TinyParser.FOR) | (1 << TinyParser.IF) | (1 << TinyParser.NAME))) != 0):
                self.state = 35
                self.statement()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
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
                
            self.state = 42
            self.match(TinyParser.CL_CUR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def st_print(self):
            return self.getTypedRuleContext(TinyParser.St_printContext,0)


        def st_decl(self):
            return self.getTypedRuleContext(TinyParser.St_declContext,0)


        def st_attrib(self):
            return self.getTypedRuleContext(TinyParser.St_attribContext,0)


        def st_for(self):
            return self.getTypedRuleContext(TinyParser.St_forContext,0)


        def st_if(self):
            return self.getTypedRuleContext(TinyParser.St_ifContext,0)


        def getRuleIndex(self):
            return TinyParser.RULE_statement




    def statement(self):

        localctx = TinyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TinyParser.PRINTLN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.st_print()
                pass
            elif token in [TinyParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.st_decl()
                pass
            elif token in [TinyParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.st_attrib()
                pass
            elif token in [TinyParser.FOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.st_for()
                pass
            elif token in [TinyParser.IF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.st_if()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_printContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINTLN(self):
            return self.getToken(TinyParser.PRINTLN, 0)

        def OP_PAR(self):
            return self.getToken(TinyParser.OP_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(TinyParser.ExpressionContext,0)


        def CL_PAR(self):
            return self.getToken(TinyParser.CL_PAR, 0)

        def getRuleIndex(self):
            return TinyParser.RULE_st_print




    def st_print(self):

        localctx = TinyParser.St_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_st_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(TinyParser.PRINTLN)
            self.state = 52
            self.match(TinyParser.OP_PAR)
            if 1:
                    emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', 1)
                    #+1 na pilha
                
            self.state = 54
            self.expression()
            if 1:
                #-2 na pilha
                    emit('    invokevirtual java/io/PrintStream/println(I)V\n', -2)
                
            self.state = 56
            self.match(TinyParser.CL_PAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def VAR(self):
            return self.getToken(TinyParser.VAR, 0)

        def NAME(self):
            return self.getToken(TinyParser.NAME, 0)

        def ATTRIB(self):
            return self.getToken(TinyParser.ATTRIB, 0)

        def expression(self):
            return self.getTypedRuleContext(TinyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TinyParser.RULE_st_decl




    def st_decl(self):

        localctx = TinyParser.St_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_st_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(TinyParser.VAR)
            self.state = 59
            localctx._NAME = self.match(TinyParser.NAME)
            if 1:
                    if (len(symbol_table) == 0):
                        symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                    else:
                        if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                            print("Variable " + (None if localctx._NAME is None else localctx._NAME.text) + " redeclared in this block.")
                            sys.exit()
                        else:
                            symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))

                    #se existe, gera erro de redeclaracao e para
                
            self.state = 61
            self.match(TinyParser.ATTRIB)
            self.state = 62
            self.expression()
            if 1:
                    index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                    usedVars.append(False)
                    store = '    istore ' + str(index) 
                    emit(store, -1)
                    #istore ==> -1 na pilha
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_forContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # ComparisonContext

        def FOR(self):
            return self.getToken(TinyParser.FOR, 0)

        def OP_CUR(self):
            return self.getToken(TinyParser.OP_CUR, 0)

        def CL_CUR(self):
            return self.getToken(TinyParser.CL_CUR, 0)

        def comparison(self):
            return self.getTypedRuleContext(TinyParser.ComparisonContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyParser.StatementContext)
            else:
                return self.getTypedRuleContext(TinyParser.StatementContext,i)


        def getRuleIndex(self):
            return TinyParser.RULE_st_for




    def st_for(self):

        localctx = TinyParser.St_forContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_st_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            if 1:
                    localCount = countFor
                    plusCount(countFor)
                    localCount += 1
                    print(beginFor + str(localCount) + ':')
                
            self.state = 66
            self.match(TinyParser.FOR)
            self.state = 67
            localctx.op = self.comparison()
            if 1:
                    emit('    ' + localctx.op.bytecode + ' ' + endFor + str(localCount),-2)
                
            self.state = 69
            self.match(TinyParser.OP_CUR)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.PRINTLN) | (1 << TinyParser.VAR) | (1 << TinyParser.FOR) | (1 << TinyParser.IF) | (1 << TinyParser.NAME))) != 0):
                self.state = 70
                self.statement()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(TinyParser.CL_CUR)
            if 1:
                    emit('    goto   ' + beginFor + str(localCount), 0)
                    print(endFor + str(localCount) + ':')
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_ifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # ComparisonContext

        def IF(self):
            return self.getToken(TinyParser.IF, 0)

        def OP_CUR(self, i:int=None):
            if i is None:
                return self.getTokens(TinyParser.OP_CUR)
            else:
                return self.getToken(TinyParser.OP_CUR, i)

        def CL_CUR(self, i:int=None):
            if i is None:
                return self.getTokens(TinyParser.CL_CUR)
            else:
                return self.getToken(TinyParser.CL_CUR, i)

        def comparison(self):
            return self.getTypedRuleContext(TinyParser.ComparisonContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyParser.StatementContext)
            else:
                return self.getTypedRuleContext(TinyParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(TinyParser.ELSE, 0)

        def getRuleIndex(self):
            return TinyParser.RULE_st_if




    def st_if(self):

        localctx = TinyParser.St_ifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(TinyParser.IF)
            self.state = 80
            localctx.op = self.comparison()
            if 1:
                    global valueElse
                    global counterIf
                    counterIf += 1
                    localCount = counterIf
                    hasElse = False
                    emit('    ' + localctx.op.bytecode + ' NOT_IF_' + str(localCount),-2)

                
            self.state = 82
            self.match(TinyParser.OP_CUR)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.PRINTLN) | (1 << TinyParser.VAR) | (1 << TinyParser.FOR) | (1 << TinyParser.IF) | (1 << TinyParser.NAME))) != 0):
                self.state = 83
                self.statement()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(TinyParser.CL_CUR)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TinyParser.ELSE:
                if 1:
                        hasElse = True
                        emit('    goto END_ELSE_' + str(localCount),0)
                        print('NOT_IF_' + str(localCount) + ':')
                    
                self.state = 91
                self.match(TinyParser.ELSE)
                self.state = 92
                self.match(TinyParser.OP_CUR)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.PRINTLN) | (1 << TinyParser.VAR) | (1 << TinyParser.FOR) | (1 << TinyParser.IF) | (1 << TinyParser.NAME))) != 0):
                    self.state = 93
                    self.statement()
                    self.state = 98
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 99
                self.match(TinyParser.CL_CUR)


            if 1:
                    if(hasElse):
                        emit('END_ELSE_' + str(localCount) + ':',0)
                    else:
                        print('NOT_IF_' + str(localCount) + ':')
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.bytecode = None
            self.op = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TinyParser.ExpressionContext,i)


        def EQ(self):
            return self.getToken(TinyParser.EQ, 0)

        def NE(self):
            return self.getToken(TinyParser.NE, 0)

        def LT(self):
            return self.getToken(TinyParser.LT, 0)

        def LE(self):
            return self.getToken(TinyParser.LE, 0)

        def GT(self):
            return self.getToken(TinyParser.GT, 0)

        def GE(self):
            return self.getToken(TinyParser.GE, 0)

        def getRuleIndex(self):
            return TinyParser.RULE_comparison




    def comparison(self):

        localctx = TinyParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.expression()
            self.state = 105
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.EQ) | (1 << TinyParser.NE) | (1 << TinyParser.LT) | (1 << TinyParser.LE) | (1 << TinyParser.GT) | (1 << TinyParser.GE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 106
            self.expression()
            if 1:

                    if (0 if localctx.op is None else localctx.op.type) == TinyParser.EQ:
                        localctx.bytecode = 'if_icmpne'         #faz uma comparacao entre dois valores interios na pilha
                    elif (0 if localctx.op is None else localctx.op.type) == TinyParser.NE:
                        localctx.bytecode = 'if_icmpeq'
                    elif (0 if localctx.op is None else localctx.op.type) == TinyParser.LT:
                        localctx.bytecode = 'if_icmpge'
                    elif (0 if localctx.op is None else localctx.op.type) == TinyParser.LE:
                        localctx.bytecode = 'if_icmpgt'     #fazer o inverso
                    elif (0 if localctx.op is None else localctx.op.type) == TinyParser.GT:
                        localctx.bytecode = 'if_icmple'
                    elif (0 if localctx.op is None else localctx.op.type) == TinyParser.GE:
                        localctx.bytecode = 'if_icmplt'
                
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class St_attribContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token

        def NAME(self):
            return self.getToken(TinyParser.NAME, 0)

        def ATTRIB(self):
            return self.getToken(TinyParser.ATTRIB, 0)

        def expression(self):
            return self.getTypedRuleContext(TinyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TinyParser.RULE_st_attrib




    def st_attrib(self):

        localctx = TinyParser.St_attribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            localctx._NAME = self.match(TinyParser.NAME)
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                        pass
                    else:
                        print("error: Variable " + (None if localctx._NAME is None else localctx._NAME.text) + " is not declared.")
                        sys.exit()
                
            self.state = 111
            self.match(TinyParser.ATTRIB)
            self.state = 112
            self.expression()
            if 1:
                    index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                    store = '    istore ' + str(index) 
                    emit(store, -1)
                
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyParser.TermContext)
            else:
                return self.getTypedRuleContext(TinyParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(TinyParser.PLUS)
            else:
                return self.getToken(TinyParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(TinyParser.MINUS)
            else:
                return self.getToken(TinyParser.MINUS, i)

        def getRuleIndex(self):
            return TinyParser.RULE_expression




    def expression(self):

        localctx = TinyParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.term()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TinyParser.PLUS or _la==TinyParser.MINUS:
                self.state = 116
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==TinyParser.PLUS or _la==TinyParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 117
                self.term()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == TinyParser.PLUS:
                            emit('    iadd', -1)
                        if (0 if localctx.op is None else localctx.op.type) == TinyParser.MINUS:
                            emit('    isub', -1)
                    
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyParser.FactorContext)
            else:
                return self.getTypedRuleContext(TinyParser.FactorContext,i)


        def TIMES(self, i:int=None):
            if i is None:
                return self.getTokens(TinyParser.TIMES)
            else:
                return self.getToken(TinyParser.TIMES, i)

        def OVER(self, i:int=None):
            if i is None:
                return self.getTokens(TinyParser.OVER)
            else:
                return self.getToken(TinyParser.OVER, i)

        def REM(self, i:int=None):
            if i is None:
                return self.getTokens(TinyParser.REM)
            else:
                return self.getToken(TinyParser.REM, i)

        def getRuleIndex(self):
            return TinyParser.RULE_term




    def term(self):

        localctx = TinyParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.factor()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.TIMES) | (1 << TinyParser.OVER) | (1 << TinyParser.REM))) != 0):
                self.state = 126
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.TIMES) | (1 << TinyParser.OVER) | (1 << TinyParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 127
                self.factor()
                if 1:
                        #lcd,imul,idiv,irem ==> -1 na pilha
                        if (0 if localctx.op is None else localctx.op.type) == TinyParser.TIMES:
                            emit('    imul', -1)
                        if (0 if localctx.op is None else localctx.op.type) == TinyParser.OVER:
                            emit('    idiv', -1)
                        if (0 if localctx.op is None else localctx.op.type) == TinyParser.REM:
                            emit('    irem', -1)
                            
                    
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NUMBER = None # Token
            self._NAME = None # Token

        def NUMBER(self):
            return self.getToken(TinyParser.NUMBER, 0)

        def OP_PAR(self):
            return self.getToken(TinyParser.OP_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(TinyParser.ExpressionContext,0)


        def CL_PAR(self):
            return self.getToken(TinyParser.CL_PAR, 0)

        def NAME(self):
            return self.getToken(TinyParser.NAME, 0)

        def READ_INT(self):
            return self.getToken(TinyParser.READ_INT, 0)

        def getRuleIndex(self):
            return TinyParser.RULE_factor




    def factor(self):

        localctx = TinyParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_factor)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TinyParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 135
                localctx._NUMBER = self.match(TinyParser.NUMBER)
                if 1:
                        #  emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), 1)
                        store = '    ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text)
                        emit(store, 1)
                        # symbol_table.append((None if localctx._NUMBER is None else localctx._NUMBER.text))
                    
                pass
            elif token in [TinyParser.OP_PAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.match(TinyParser.OP_PAR)
                self.state = 138
                self.expression()
                self.state = 139
                self.match(TinyParser.CL_PAR)
                pass
            elif token in [TinyParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 141
                localctx._NAME = self.match(TinyParser.NAME)
                if 1:
                        #verificar se NAME existe
                        if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                            index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                            usedVars[index] = True
                            emit('    iload ' + str(index), 1)
                        #iload +1 ==> na piha aumenta, visto que carrega o valor 
                        #se nao existe, gera erro e para
                        else:
                            print("error: Variable " + (None if localctx._NAME is None else localctx._NAME.text) + " is not declared.")
                            sys.exit()
                    
                pass
            elif token in [TinyParser.READ_INT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.match(TinyParser.READ_INT)
                self.state = 144
                self.match(TinyParser.OP_PAR)
                self.state = 145
                self.match(TinyParser.CL_PAR)
                if 1:
                        emit('    invokestatic Runtime/readInt()I', 1)
                        #+1 na pilha
                        #comando da biblioteca Runtime.java
                    
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





