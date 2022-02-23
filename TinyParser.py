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
    


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$")
        buf.write("\u00cd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\2\7\2#\n\2\f\2\16\2&\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\7\3\65\n\3\f\3\16\38\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\7\4D\n\4\f\4\16\4G\13\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5T\n\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\7\bj\n\b\f\b\16\bm\13\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\7\n{\n\n\f\n\16\n~\13\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\7\n\u0085\n\n\f\n\16\n\u0088\13\n\3\n")
        buf.write("\5\n\u008b\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\7\r\u009f\n\r\f")
        buf.write("\r\16\r\u00a2\13\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\7")
        buf.write("\16\u00ab\n\16\f\16\16\16\u00ae\13\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\5\17\u00cb\n\17\3\17\2\2\20\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\2\5\3\2\r\22\3\2\3\4\3\2\5\7\2\u00d2")
        buf.write("\2\36\3\2\2\2\4)\3\2\2\2\6<\3\2\2\2\bS\3\2\2\2\nU\3\2")
        buf.write("\2\2\f\\\3\2\2\2\16c\3\2\2\2\20q\3\2\2\2\22u\3\2\2\2\24")
        buf.write("\u008e\3\2\2\2\26\u0093\3\2\2\2\30\u0099\3\2\2\2\32\u00a5")
        buf.write("\3\2\2\2\34\u00ca\3\2\2\2\36\37\7\25\2\2\37 \7\35\2\2")
        buf.write(" $\b\2\1\2!#\5\4\3\2\"!\3\2\2\2#&\3\2\2\2$\"\3\2\2\2$")
        buf.write("%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'(\5\6\4\2(\3\3\2\2\2)")
        buf.write("*\7\24\2\2*+\7!\2\2+,\7\b\2\2,-\b\3\1\2-.\7!\2\2./\b\3")
        buf.write("\1\2/\60\7\37\2\2\60\61\7\t\2\2\61\62\7\37\2\2\62\66\7")
        buf.write("\n\2\2\63\65\5\b\5\2\64\63\3\2\2\2\658\3\2\2\2\66\64\3")
        buf.write("\2\2\2\66\67\3\2\2\2\679\3\2\2\28\66\3\2\2\29:\b\3\1\2")
        buf.write(":;\7\13\2\2;\5\3\2\2\2<=\7\24\2\2=>\7\35\2\2>?\7\b\2\2")
        buf.write("?@\7\t\2\2@A\7\n\2\2AE\b\4\1\2BD\5\b\5\2CB\3\2\2\2DG\3")
        buf.write("\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3\2\2\2GE\3\2\2\2HI\b\4\1")
        buf.write("\2IJ\7\13\2\2J\7\3\2\2\2KT\5\n\6\2LT\5\f\7\2MT\5\26\f")
        buf.write("\2NT\5\16\b\2OT\5\22\n\2PQ\5\20\t\2QR\b\5\1\2RT\3\2\2")
        buf.write("\2SK\3\2\2\2SL\3\2\2\2SM\3\2\2\2SN\3\2\2\2SO\3\2\2\2S")
        buf.write("P\3\2\2\2T\t\3\2\2\2UV\7\23\2\2VW\7\b\2\2WX\b\6\1\2XY")
        buf.write("\5\30\r\2YZ\b\6\1\2Z[\7\t\2\2[\13\3\2\2\2\\]\7\26\2\2")
        buf.write("]^\7!\2\2^_\b\7\1\2_`\7\f\2\2`a\5\30\r\2ab\b\7\1\2b\r")
        buf.write("\3\2\2\2cd\b\b\1\2de\7\32\2\2ef\5\24\13\2fg\b\b\1\2gk")
        buf.write("\7\n\2\2hj\5\b\5\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2")
        buf.write("\2\2ln\3\2\2\2mk\3\2\2\2no\7\13\2\2op\b\b\1\2p\17\3\2")
        buf.write("\2\2qr\7\31\2\2rs\5\30\r\2st\b\t\1\2t\21\3\2\2\2uv\7\33")
        buf.write("\2\2vw\5\24\13\2wx\b\n\1\2x|\7\n\2\2y{\5\b\5\2zy\3\2\2")
        buf.write("\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\177\3\2\2\2~|\3\2\2")
        buf.write("\2\177\u008a\7\13\2\2\u0080\u0081\b\n\1\2\u0081\u0082")
        buf.write("\7\34\2\2\u0082\u0086\7\n\2\2\u0083\u0085\5\b\5\2\u0084")
        buf.write("\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u0086\3")
        buf.write("\2\2\2\u0089\u008b\7\13\2\2\u008a\u0080\3\2\2\2\u008a")
        buf.write("\u008b\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\b\n\1\2")
        buf.write("\u008d\23\3\2\2\2\u008e\u008f\5\30\r\2\u008f\u0090\t\2")
        buf.write("\2\2\u0090\u0091\5\30\r\2\u0091\u0092\b\13\1\2\u0092\25")
        buf.write("\3\2\2\2\u0093\u0094\7!\2\2\u0094\u0095\b\f\1\2\u0095")
        buf.write("\u0096\7\f\2\2\u0096\u0097\5\30\r\2\u0097\u0098\b\f\1")
        buf.write("\2\u0098\27\3\2\2\2\u0099\u00a0\5\32\16\2\u009a\u009b")
        buf.write("\t\3\2\2\u009b\u009c\5\32\16\2\u009c\u009d\b\r\1\2\u009d")
        buf.write("\u009f\3\2\2\2\u009e\u009a\3\2\2\2\u009f\u00a2\3\2\2\2")
        buf.write("\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a3\3")
        buf.write("\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\b\r\1\2\u00a4\31")
        buf.write("\3\2\2\2\u00a5\u00ac\5\34\17\2\u00a6\u00a7\t\4\2\2\u00a7")
        buf.write("\u00a8\5\34\17\2\u00a8\u00a9\b\16\1\2\u00a9\u00ab\3\2")
        buf.write("\2\2\u00aa\u00a6\3\2\2\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa")
        buf.write("\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae")
        buf.write("\u00ac\3\2\2\2\u00af\u00b0\b\16\1\2\u00b0\33\3\2\2\2\u00b1")
        buf.write("\u00b2\7 \2\2\u00b2\u00cb\b\17\1\2\u00b3\u00b4\7\b\2\2")
        buf.write("\u00b4\u00b5\5\30\r\2\u00b5\u00b6\7\t\2\2\u00b6\u00b7")
        buf.write("\b\17\1\2\u00b7\u00cb\3\2\2\2\u00b8\u00b9\7!\2\2\u00b9")
        buf.write("\u00ba\7\b\2\2\u00ba\u00bb\5\30\r\2\u00bb\u00bc\7\t\2")
        buf.write("\2\u00bc\u00bd\b\17\1\2\u00bd\u00cb\3\2\2\2\u00be\u00bf")
        buf.write("\7!\2\2\u00bf\u00cb\b\17\1\2\u00c0\u00c1\7\27\2\2\u00c1")
        buf.write("\u00c2\7\b\2\2\u00c2\u00c3\7\t\2\2\u00c3\u00cb\b\17\1")
        buf.write("\2\u00c4\u00c5\7\"\2\2\u00c5\u00cb\b\17\1\2\u00c6\u00c7")
        buf.write("\7\30\2\2\u00c7\u00c8\7\b\2\2\u00c8\u00c9\7\t\2\2\u00c9")
        buf.write("\u00cb\b\17\1\2\u00ca\u00b1\3\2\2\2\u00ca\u00b3\3\2\2")
        buf.write("\2\u00ca\u00b8\3\2\2\2\u00ca\u00be\3\2\2\2\u00ca\u00c0")
        buf.write("\3\2\2\2\u00ca\u00c4\3\2\2\2\u00ca\u00c6\3\2\2\2\u00cb")
        buf.write("\35\3\2\2\2\r$\66ESk|\u0086\u008a\u00a0\u00ac\u00ca")
        return buf.getvalue()


class TinyParser ( Parser ):

    grammarFileName = "Tiny.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'('", 
                     "')'", "'{'", "'}'", "'='", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'println'", "'func'", "'package'", 
                     "'var'", "'read_int'", "'read_str'", "'return'", "'for'", 
                     "'if'", "'else'", "'main'", "'function'", "'int'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "TIMES", "OVER", "REM", 
                      "OP_PAR", "CL_PAR", "OP_CUR", "CL_CUR", "ATTRIB", 
                      "EQ", "NE", "LT", "LE", "GT", "GE", "PRINTLN", "FUNC", 
                      "PACKAGE", "VAR", "READ_INT", "READ_STR", "RETURN", 
                      "FOR", "IF", "ELSE", "MAIN", "FUNCTION", "INT", "NUMBER", 
                      "NAME", "STRING", "SPACE", "COMMENT" ]

    RULE_program = 0
    RULE_function = 1
    RULE_main = 2
    RULE_statement = 3
    RULE_st_print = 4
    RULE_st_decl = 5
    RULE_st_for = 6
    RULE_st_return = 7
    RULE_st_if = 8
    RULE_comparison = 9
    RULE_st_attrib = 10
    RULE_expression = 11
    RULE_term = 12
    RULE_factor = 13

    ruleNames =  [ "program", "function", "main", "statement", "st_print", 
                   "st_decl", "st_for", "st_return", "st_if", "comparison", 
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
    READ_STR=22
    RETURN=23
    FOR=24
    IF=25
    ELSE=26
    MAIN=27
    FUNCTION=28
    INT=29
    NUMBER=30
    NAME=31
    STRING=32
    SPACE=33
    COMMENT=34

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


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TinyParser.FunctionContext)
            else:
                return self.getTypedRuleContext(TinyParser.FunctionContext,i)


        def getRuleIndex(self):
            return TinyParser.RULE_program




    def program(self):

        localctx = TinyParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(TinyParser.PACKAGE)
            self.state = 29
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
                
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 31
                    self.function() 
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 37
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._NAME = None # Token
            self.e = None # StatementContext

        def FUNC(self):
            return self.getToken(TinyParser.FUNC, 0)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(TinyParser.NAME)
            else:
                return self.getToken(TinyParser.NAME, i)

        def OP_PAR(self):
            return self.getToken(TinyParser.OP_PAR, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(TinyParser.INT)
            else:
                return self.getToken(TinyParser.INT, i)

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
            return TinyParser.RULE_function




    def function(self):

        localctx = TinyParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(TinyParser.FUNC)
            self.state = 40
            localctx._NAME = self.match(TinyParser.NAME)
            self.state = 41
            self.match(TinyParser.OP_PAR)
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) in func_table:
                        print("error: function " + (None if localctx._NAME is None else localctx._NAME.text) + " already declared",file=sys.stderr)
                    else:
                        print('.method public static ' + (None if localctx._NAME is None else localctx._NAME.text) +'(I)I\n')
                        func_table.append((None if localctx._NAME is None else localctx._NAME.text))
                
            self.state = 43
            localctx._NAME = self.match(TinyParser.NAME)
            if 1:
                    symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                    usedVars.append(False)
                    type_table.append('i')
                
            self.state = 45
            self.match(TinyParser.INT)
            self.state = 46
            self.match(TinyParser.CL_PAR)
            self.state = 47
            self.match(TinyParser.INT)
            self.state = 48
            self.match(TinyParser.OP_CUR)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.PRINTLN) | (1 << TinyParser.VAR) | (1 << TinyParser.RETURN) | (1 << TinyParser.FOR) | (1 << TinyParser.IF) | (1 << TinyParser.NAME))) != 0):
                self.state = 49
                localctx.e = self.statement()
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
                    if(localctx.e.type == 'function'):
                        aux = False

                        for i in range (len(usedVars)):
                            if (usedVars[i] == False):
                                print("Warning: " + symbol_table[i] + " is defined but never used",file=sys.stderr)

                                aux = True
                        if (localctx.e.type == 'error'):
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
                    
                    
                
            self.state = 56
            self.match(TinyParser.CL_CUR)
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
            self.e = None # StatementContext

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
        self.enterRule(localctx, 4, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(TinyParser.FUNC)
            self.state = 59
            self.match(TinyParser.MAIN)
            self.state = 60
            self.match(TinyParser.OP_PAR)
            self.state = 61
            self.match(TinyParser.CL_PAR)
            self.state = 62
            self.match(TinyParser.OP_CUR)
            if 1:
                    print('.method public static main([Ljava/lang/String;)V\n')
                
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.PRINTLN) | (1 << TinyParser.VAR) | (1 << TinyParser.RETURN) | (1 << TinyParser.FOR) | (1 << TinyParser.IF) | (1 << TinyParser.NAME))) != 0):
                self.state = 64
                localctx.e = self.statement()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
                    if(localctx.e.type != 'function'):
                        aux = False

                        for i in range (len(usedVars)):
                            if (usedVars[i] == False):
                                print("Warning: " + symbol_table[i] + " is defined but never used",file=sys.stderr)

                                aux = True
                        if (localctx.e.type == 'error'):
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
                    elif(localctx.e.type == 'function'):
                        print('error: return statement cannot be used inside main',file=sys.stderr)
                        sys.exit()
                
            self.state = 71
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
            self.type = None
            self.ef = None # St_returnContext

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


        def st_return(self):
            return self.getTypedRuleContext(TinyParser.St_returnContext,0)


        def getRuleIndex(self):
            return TinyParser.RULE_statement




    def statement(self):

        localctx = TinyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TinyParser.PRINTLN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.st_print()
                pass
            elif token in [TinyParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.st_decl()
                pass
            elif token in [TinyParser.NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.st_attrib()
                pass
            elif token in [TinyParser.FOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.st_for()
                pass
            elif token in [TinyParser.IF]:
                self.enterOuterAlt(localctx, 5)
                self.state = 77
                self.st_if()
                pass
            elif token in [TinyParser.RETURN]:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                localctx.ef = self.st_return()
                if 1:
                        localctx.type = localctx.ef.typeFuc
                    
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
            self.e = None # ExpressionContext

        def PRINTLN(self):
            return self.getToken(TinyParser.PRINTLN, 0)

        def OP_PAR(self):
            return self.getToken(TinyParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(TinyParser.CL_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(TinyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TinyParser.RULE_st_print




    def st_print(self):

        localctx = TinyParser.St_printContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_st_print)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(TinyParser.PRINTLN)
            self.state = 84
            self.match(TinyParser.OP_PAR)
            if 1:
                    emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', 1)
                    #+1 na pilha
                
            self.state = 86
            localctx.e = self.expression()
            if 1:
                    if (localctx.e.type == 'i'):
                        emit('    invokevirtual java/io/PrintStream/println(I)V\n', -2)
                        
                    elif (localctx.e.type == 's'):
                        emit('    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V\n', -2)
                    else:
                        print(localctx.e.type)
                
            self.state = 88
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
            self.e = None # ExpressionContext

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
        self.enterRule(localctx, 10, self.RULE_st_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(TinyParser.VAR)
            self.state = 91
            localctx._NAME = self.match(TinyParser.NAME)
            if 1:
                    if (len(symbol_table) == 0):
                        symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))
                    else:
                        if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                            print("Variable " + (None if localctx._NAME is None else localctx._NAME.text) + " redeclared in this block.",file=sys.stderr)
                            sys.exit()
                        else:
                            symbol_table.append((None if localctx._NAME is None else localctx._NAME.text))

                    #se existe, gera erro de redeclaracao e para
                
            self.state = 93
            self.match(TinyParser.ATTRIB)
            self.state = 94
            localctx.e = self.expression()
            if 1:
                    if(localctx.e.type == 'i'):            #type of int
                        index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                        usedVars.append(False)
                        type_table.append('i')
                        store = '    istore ' + str(index)  + '\n'
                        emit(store, -1)            #istore ==> -1 na pilha
                                                   
                    if(localctx.e.type == 's'):            #type of string
                        index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                        type_table.append('s')
                        usedVars.append(False)
                        store = '    astore ' + str(index) + '\n'
                        emit(store, -1)
                
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
        self.enterRule(localctx, 12, self.RULE_st_for)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            if 1:
                    localCount = countFor
                    plusCount(countFor)
                    localCount += 1
                    print(beginFor + str(localCount) + ':')
                
            self.state = 98
            self.match(TinyParser.FOR)
            self.state = 99
            localctx.op = self.comparison()
            if 1:
                    if localctx.op.bytecode == 'error':
                        print('error: FOR operands must be integers!!!',file=sys.stderr)
                        sys.exit()
                    else:
                        emit('    ' + localctx.op.bytecode + ' ' + endFor + str(localCount),-2)
                
            self.state = 101
            self.match(TinyParser.OP_CUR)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.PRINTLN) | (1 << TinyParser.VAR) | (1 << TinyParser.RETURN) | (1 << TinyParser.FOR) | (1 << TinyParser.IF) | (1 << TinyParser.NAME))) != 0):
                self.state = 102
                self.statement()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
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


    class St_returnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.typeFuc = None
            self.e = None # ExpressionContext

        def RETURN(self):
            return self.getToken(TinyParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(TinyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TinyParser.RULE_st_return




    def st_return(self):

        localctx = TinyParser.St_returnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_st_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(TinyParser.RETURN)
            self.state = 112
            localctx.e = self.expression()
            if 1:
                    if(localctx.e.type == 'i'):
                        emit('    ireturn',-1)
                        localctx.typeFuc = 'function'
                    elif(localctx.e.type == 's'):
                        print('error: return value must be of integer type',file=sys.stderr)
                        localctx.typeFuc = 'function'
                    
                
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
            self.type = None
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
        self.enterRule(localctx, 16, self.RULE_st_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(TinyParser.IF)
            self.state = 116
            localctx.op = self.comparison()
            if 1:
                    if localctx.op.bytecode == 'error':
                        print('error: IF operands must be integers!!!',file=sys.stderr)
                        localctx.type = 'error'
                        sys.exit()
                    else:
                        global counterIf
                        counterIf += 1
                        localCount = counterIf
                        hasElse = False
                        emit('    ' + localctx.op.bytecode + ' NOT_IF_' + str(localCount),-2)

                
            self.state = 118
            self.match(TinyParser.OP_CUR)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.PRINTLN) | (1 << TinyParser.VAR) | (1 << TinyParser.RETURN) | (1 << TinyParser.FOR) | (1 << TinyParser.IF) | (1 << TinyParser.NAME))) != 0):
                self.state = 119
                self.statement()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
            self.match(TinyParser.CL_CUR)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TinyParser.ELSE:
                if 1:
                        hasElse = True
                        emit('    goto END_ELSE_' + str(localCount),0)
                        print('NOT_IF_' + str(localCount) + ':')
                    
                self.state = 127
                self.match(TinyParser.ELSE)
                self.state = 128
                self.match(TinyParser.OP_CUR)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.PRINTLN) | (1 << TinyParser.VAR) | (1 << TinyParser.RETURN) | (1 << TinyParser.FOR) | (1 << TinyParser.IF) | (1 << TinyParser.NAME))) != 0):
                    self.state = 129
                    self.statement()
                    self.state = 134
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 135
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
            self.e1 = None # ExpressionContext
            self.op = None # Token
            self.e2 = None # ExpressionContext

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
        self.enterRule(localctx, 18, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            localctx.e1 = self.expression()
            self.state = 141
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.EQ) | (1 << TinyParser.NE) | (1 << TinyParser.LT) | (1 << TinyParser.LE) | (1 << TinyParser.GT) | (1 << TinyParser.GE))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 142
            localctx.e2 = self.expression()
            if 1:
                    if(localctx.e1.type == 'i' and localctx.e2.type == 'i'):
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
                    else:
                        localctx.bytecode = 'error'
                        
                
                
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
            self.type = None
            self._NAME = None # Token
            self.e = None # ExpressionContext

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
        self.enterRule(localctx, 20, self.RULE_st_attrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            localctx._NAME = self.match(TinyParser.NAME)
            if 1:
                    if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                        pass
                    else:
                        print("error: Variable " + (None if localctx._NAME is None else localctx._NAME.text) + " is not declared.",file=sys.stderr)
                        sys.exit()
                
            self.state = 147
            self.match(TinyParser.ATTRIB)
            self.state = 148
            localctx.e = self.expression()
            if 1:
                    index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                    if(localctx.e.type == 'i' and type_table[index] == 'i'):
                        usedVars[index] = True
                        emit('    istore ' + str(index), -1)
                
                    elif(localctx.e.type == 's' and type_table[index] == 'i'):
                        store = 'error: ' + (None if localctx._NAME is None else localctx._NAME.text) + ' is a integer\n'
                        print(store ,file=sys.stderr)
                    
                    elif(localctx.e.type == 's' and type_table[index] == 's'):
                        usedVars[index] = True
                        emit('    astore ' + str(index), -1)
                    
                    elif(localctx.e.type == 'i' and type_table[index] == 's'):
                        store = 'error: ' + (None if localctx._NAME is None else localctx._NAME.text) + ' is a string\n'
                        print(store ,file=sys.stderr)



                
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
            self.type = None
            self.t1 = None # TermContext
            self.op = None # Token
            self.t2 = None # TermContext

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
        self.enterRule(localctx, 22, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            localctx.t1 = self.term()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TinyParser.PLUS or _la==TinyParser.MINUS:
                self.state = 152
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==TinyParser.PLUS or _la==TinyParser.MINUS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 153
                localctx.t2 = self.term()
                if 1:
                        if(localctx.t1.type == 'i' and localctx.t2.type == 'i'):
                            if (0 if localctx.op is None else localctx.op.type) == TinyParser.PLUS:
                                emit('    iadd', -1)
                            if (0 if localctx.op is None else localctx.op.type) == TinyParser.MINUS:
                                emit('    isub', -1)
                        else:
                            localctx.type = 'error'
                            print('error: (+ and -) operands must be integers',file=sys.stderr)
                    
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
                    localctx.type = localctx.t1.type
                
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
            self.type = None
            self.f1 = None # FactorContext
            self.op = None # Token
            self.f2 = None # FactorContext

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
        self.enterRule(localctx, 24, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            localctx.f1 = self.factor()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.TIMES) | (1 << TinyParser.OVER) | (1 << TinyParser.REM))) != 0):
                self.state = 164
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TinyParser.TIMES) | (1 << TinyParser.OVER) | (1 << TinyParser.REM))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 165
                localctx.f2 = self.factor()
                if 1:
                        if(localctx.f1.type == 'i' and localctx.f2.type == 'i'):    
                            #lcd,imul,idiv,irem ==> -1 na pilha
                            if (0 if localctx.op is None else localctx.op.type) == TinyParser.TIMES:
                                emit('    imul', -1)
                            if (0 if localctx.op is None else localctx.op.type) == TinyParser.OVER:
                                emit('    idiv', -1)
                            if (0 if localctx.op is None else localctx.op.type) == TinyParser.REM:
                                emit('    irem', -1)
                        else:
                            localctx.type = 'error'
                            print('error: (* , / and %) operands must be integers!',file=sys.stderr)
                    
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            if 1:
                    localctx.type = localctx.f1.type

                
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
            self.type = None
            self._NUMBER = None # Token
            self.e = None # ExpressionContext
            self._NAME = None # Token
            self._STRING = None # Token

        def NUMBER(self):
            return self.getToken(TinyParser.NUMBER, 0)

        def OP_PAR(self):
            return self.getToken(TinyParser.OP_PAR, 0)

        def CL_PAR(self):
            return self.getToken(TinyParser.CL_PAR, 0)

        def expression(self):
            return self.getTypedRuleContext(TinyParser.ExpressionContext,0)


        def NAME(self):
            return self.getToken(TinyParser.NAME, 0)

        def READ_INT(self):
            return self.getToken(TinyParser.READ_INT, 0)

        def STRING(self):
            return self.getToken(TinyParser.STRING, 0)

        def READ_STR(self):
            return self.getToken(TinyParser.READ_STR, 0)

        def getRuleIndex(self):
            return TinyParser.RULE_factor




    def factor(self):

        localctx = TinyParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                localctx._NUMBER = self.match(TinyParser.NUMBER)
                if 1:
                        store = '    ldc ' + (None if localctx._NUMBER is None else localctx._NUMBER.text)
                        emit(store, 1)

                        localctx.type = 'i'
                        # essa regra resultou em 'inteiro'
                    
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(TinyParser.OP_PAR)
                self.state = 178
                localctx.e = self.expression()
                self.state = 179
                self.match(TinyParser.CL_PAR)
                if 1:
                        localctx.type = localctx.e.type

                    
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                localctx._NAME = self.match(TinyParser.NAME)
                self.state = 183
                self.match(TinyParser.OP_PAR)
                self.state = 184
                localctx.e = self.expression()
                self.state = 185
                self.match(TinyParser.CL_PAR)
                if 1:
                        if((None if localctx._NAME is None else localctx._NAME.text) in func_table):
                            emit('    invokestatic Test/'+(None if localctx._NAME is None else localctx._NAME.text)+'(I)I',0)
                            localctx.type = localctx.e.type
                            if(localctx.e.type == 's'):
                                print("error: argument must be integer",file=sys.stderr)
                        else:
                            print("error: function " + (None if localctx._NAME is None else localctx._NAME.text) + " not declared",file=sys.stderr)

                        
                    
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 188
                localctx._NAME = self.match(TinyParser.NAME)
                if 1:
                        #verificar se NAME existe
                        if (None if localctx._NAME is None else localctx._NAME.text) in symbol_table:
                            index = symbol_table.index((None if localctx._NAME is None else localctx._NAME.text))
                            typeValue = type_table[index]

                            if(typeValue == 'i'):
                                usedVars[index] = True
                                emit('    iload ' + str(index), 1)
                                localctx.type = 'i'

                            elif(typeValue == 's'):
                                usedVars[index] = True
                                emit('    aload ' + str(index), 1)
                                localctx.type = 's'

                        #iload +1 ==> na piha aumenta, visto que carrega o valor 
                        #se nao existe, gera erro e para
                        else:
                            print("error: Variable " + (None if localctx._NAME is None else localctx._NAME.text) + " is not declared.",file=sys.stderr)
                            sys.exit()

                        #verificar o tipo na tabela de tipos
                        # localctx.type = 'i' ou localctx.type = 's'
                        #localctx.type = ???
                    
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 190
                self.match(TinyParser.READ_INT)
                self.state = 191
                self.match(TinyParser.OP_PAR)
                self.state = 192
                self.match(TinyParser.CL_PAR)
                if 1:
                        emit('    invokestatic Runtime/readInt()I', 1)
                        #+1 na pilha
                        #comando da biblioteca Runtime.java
                        localctx.type = 'i'
                    
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 194
                localctx._STRING = self.match(TinyParser.STRING)
                if 1:
                        store = '    ldc  ' + (None if localctx._STRING is None else localctx._STRING.text)
                        emit(store, 1)
                        localctx.type = 's'
                        

                    
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 196
                self.match(TinyParser.READ_STR)
                self.state = 197
                self.match(TinyParser.OP_PAR)
                self.state = 198
                self.match(TinyParser.CL_PAR)
                if 1:
                        emit('    invokestatic Runtime/readString()Ljava/lang/String;', 1)
                        localctx.type = 's'
                    
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





