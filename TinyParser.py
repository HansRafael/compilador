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
    


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\5\4,\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\7\bG\n\b\f\b\16\bJ\13\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\7\tQ\n\t\f\t\16\tT\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\5\nb\n\n\3\n\2\2\13\2\4\6\b\n\f\16")
        buf.write("\20\22\2\4\3\2\3\4\3\2\5\7\2b\2\24\3\2\2\2\4\31\3\2\2")
        buf.write("\2\6+\3\2\2\2\b-\3\2\2\2\n\64\3\2\2\2\f;\3\2\2\2\16A\3")
        buf.write("\2\2\2\20K\3\2\2\2\22a\3\2\2\2\24\25\7\17\2\2\25\26\7")
        buf.write("\22\2\2\26\27\b\2\1\2\27\30\5\4\3\2\30\3\3\2\2\2\31\32")
        buf.write("\7\16\2\2\32\33\7\22\2\2\33\34\7\b\2\2\34\35\7\t\2\2\35")
        buf.write("\36\7\n\2\2\36\"\b\3\1\2\37!\5\6\4\2 \37\3\2\2\2!$\3\2")
        buf.write("\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"\3\2\2\2%&\b\3")
        buf.write("\1\2&\'\7\13\2\2\'\5\3\2\2\2(,\5\b\5\2),\5\n\6\2*,\5\f")
        buf.write("\7\2+(\3\2\2\2+)\3\2\2\2+*\3\2\2\2,\7\3\2\2\2-.\7\r\2")
        buf.write("\2./\7\b\2\2/\60\b\5\1\2\60\61\5\16\b\2\61\62\b\5\1\2")
        buf.write("\62\63\7\t\2\2\63\t\3\2\2\2\64\65\7\20\2\2\65\66\7\24")
        buf.write("\2\2\66\67\b\6\1\2\678\7\f\2\289\5\16\b\29:\b\6\1\2:\13")
        buf.write("\3\2\2\2;<\7\24\2\2<=\b\7\1\2=>\7\f\2\2>?\5\16\b\2?@\b")
        buf.write("\7\1\2@\r\3\2\2\2AH\5\20\t\2BC\t\2\2\2CD\5\20\t\2DE\b")
        buf.write("\b\1\2EG\3\2\2\2FB\3\2\2\2GJ\3\2\2\2HF\3\2\2\2HI\3\2\2")
        buf.write("\2I\17\3\2\2\2JH\3\2\2\2KR\5\22\n\2LM\t\3\2\2MN\5\22\n")
        buf.write("\2NO\b\t\1\2OQ\3\2\2\2PL\3\2\2\2QT\3\2\2\2RP\3\2\2\2R")
        buf.write("S\3\2\2\2S\21\3\2\2\2TR\3\2\2\2UV\7\23\2\2Vb\b\n\1\2W")
        buf.write("X\7\b\2\2XY\5\16\b\2YZ\7\t\2\2Zb\3\2\2\2[\\\7\24\2\2\\")
        buf.write("b\b\n\1\2]^\7\21\2\2^_\7\b\2\2_`\7\t\2\2`b\b\n\1\2aU\3")
        buf.write("\2\2\2aW\3\2\2\2a[\3\2\2\2a]\3\2\2\2b\23\3\2\2\2\7\"+")
        buf.write("HRa")
        return buf.getvalue()


class TinyParser ( Parser ):

    grammarFileName = "Tiny.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", 
                     "')'", "'{'", "'}'", "'='", "'println'", "'func'", 
                     "'package'", "'var'", "'read_int'", "'main'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "TIMES", "OVER", "REM", 
                      "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", 
                      "PRINTLN", "FUNC", "PACKAGE", "VAR", "READ_INT", "MAIN", 
                      "NUMBER", "NAME", "SPACE", "COMMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_statement = 2
    RULE_st_print = 3
    RULE_st_decl = 4
    RULE_st_attrib = 5
    RULE_expression = 6
    RULE_term = 7
    RULE_factor = 8

    ruleNames =  [ "program", "main", "statement", "st_print", "st_decl", 
                   "st_attrib", "expression", "term", "factor" ]

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
    PRINTLN=11
    FUNC=12
    PACKAGE=13
    VAR=14
    READ_INT=15
    MAIN=16
    NUMBER=17
    NAME=18
    SPACE=19
    COMMENT=20

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
            self.state = 18
            self.match(TinyParser.PACKAGE)
            self.state = 19
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
                
            self.state = 21
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
            self.state = 23
            self.match(TinyParser.FUNC)
            self.state = 24
            self.match(TinyParser.MAIN)
            self.state = 25
            self.match(TinyParser.OP_PAR)
            self.state = 26
            self.match(TinyParser.CL_PAR)
            self.state = 27
            self.match(TinyParser.OP_CUR)
            if 1:
                    print('.method public static main([Ljava/lang/String;)V\n')
                
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.PRINTLN) | (1 << TinyParser.VAR) | (1 << TinyParser.NAME))) != 0):
                self.state = 29
                self.statement()
                self.state = 34
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
                
            self.state = 36
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


        def getRuleIndex(self):
            return TinyParser.RULE_statement




    def statement(self):

        localctx = TinyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TinyParser.PRINTLN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.st_print()
                pass
            elif token in [TinyParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.st_decl()
                pass
            elif token in [TinyParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.st_attrib()
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
            self.state = 43
            self.match(TinyParser.PRINTLN)
            self.state = 44
            self.match(TinyParser.OP_PAR)
            if 1:
                    print('    getstatic java/lang/System/out Ljava/io/PrintStream;')
                    #+1 na pilha
                
            self.state = 46
            self.expression()
            if 1:
                #-2 na pilha
                print('    invokevirtual java/io/PrintStream/println(I)V\n')
                
            self.state = 48
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
            self.state = 50
            self.match(TinyParser.VAR)
            self.state = 51
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
                
            self.state = 53
            self.match(TinyParser.ATTRIB)
            self.state = 54
            self.expression()
            if 1:
                    index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                    usedVars.append(False)
                    print('    istore ' + str(index))
                    #istore ==> -1 na pilha
                
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
        self.enterRule(localctx, 10, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            localctx._NAME = self.match(TinyParser.NAME)
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                        pass
                    else:
                        print("error: Variable " + (None if localctx._NAME is None else localctx._NAME.text) + " is not declared.")
                        sys.exit()
                
            self.state = 59
            self.match(TinyParser.ATTRIB)
            self.state = 60
            self.expression()
            if 1:
                    index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                    print('    istore ' + str(index))
                
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
        self.enterRule(localctx, 12, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.term()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TinyParser.PLUS or _la==TinyParser.MINUS:
                self.state = 64
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==TinyParser.PLUS or _la==TinyParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 65
                self.term()
                if 1:
                        if (0 if localctx.op is None else localctx.op.type) == TinyParser.PLUS:
                            print('    iadd')
                        if (0 if localctx.op is None else localctx.op.type) == TinyParser.MINUS:
                            print('    isub')
                    
                self.state = 72
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
        self.enterRule(localctx, 14, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.factor()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.TIMES) | (1 << TinyParser.OVER) | (1 << TinyParser.REM))) != 0):
                self.state = 74
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.TIMES) | (1 << TinyParser.OVER) | (1 << TinyParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 75
                self.factor()
                if 1:
                        #lcd,imul,idiv,irem ==> -1 na pilha
                        if (0 if localctx.op is None else localctx.op.type) == TinyParser.TIMES:
                            print('    imul')
                        if (0 if localctx.op is None else localctx.op.type) == TinyParser.OVER:
                            print('    idiv')
                        if (0 if localctx.op is None else localctx.op.type) == TinyParser.REM:
                            print('    irem')
                    
                self.state = 82
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
        self.enterRule(localctx, 16, self.RULE_factor)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TinyParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                localctx._NUMBER = self.match(TinyParser.NUMBER)
                if 1:
                        #  emit('ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text), +1)
                        print('    ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text))
                        # symbol_table.append((None if localctx._NUMBER is None else localctx._NUMBER.text))
                    
                pass
            elif token in [TinyParser.OP_PAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 85
                self.match(TinyParser.OP_PAR)
                self.state = 86
                self.expression()
                self.state = 87
                self.match(TinyParser.CL_PAR)
                pass
            elif token in [TinyParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                localctx._NAME = self.match(TinyParser.NAME)
                if 1:
                        #verificar se NAME existe
                        if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                            index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                            usedVars[index] = True
                            print('    iload ' + str(index))
                        #iload +1 ==> na piha aumenta, visto que carrega o valor 
                        #se nao existe, gera erro e para
                        else:
                            print("error: Variable " + (None if localctx._NAME is None else localctx._NAME.text) + " is not declared.")
                            sys.exit()
                    
                pass
            elif token in [TinyParser.READ_INT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.match(TinyParser.READ_INT)
                self.state = 92
                self.match(TinyParser.OP_PAR)
                self.state = 93
                self.match(TinyParser.CL_PAR)
                if 1:
                        print('    invokestatic Runtime/readInt()I')
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





