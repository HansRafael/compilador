// Generated from /home/hans/Desktop/deskop/Facul/3 ano/1.Semestrais/Compiladores/COMPILADOR/compilador_git/Tiny.g4 by ANTLR 4.8
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
    

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TinyParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PLUS=1, MINUS=2, TIMES=3, OVER=4, REM=5, OP_PAR=6, CL_PAR=7, OP_CUR=8, 
		CL_CUR=9, ATTRIB=10, EQ=11, NE=12, LT=13, LE=14, GT=15, GE=16, PRINTLN=17, 
		FUNC=18, PACKAGE=19, VAR=20, READ_INT=21, READ_STR=22, RETURN=23, FOR=24, 
		IF=25, ELSE=26, MAIN=27, FUNCTION=28, INT=29, NUMBER=30, NAME=31, STRING=32, 
		SPACE=33, COMMENT=34;
	public static final int
		RULE_program = 0, RULE_function = 1, RULE_main = 2, RULE_statement = 3, 
		RULE_st_print = 4, RULE_st_decl = 5, RULE_st_for = 6, RULE_st_return = 7, 
		RULE_st_if = 8, RULE_comparison = 9, RULE_st_attrib = 10, RULE_expression = 11, 
		RULE_term = 12, RULE_factor = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "function", "main", "statement", "st_print", "st_decl", "st_for", 
			"st_return", "st_if", "comparison", "st_attrib", "expression", "term", 
			"factor"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'+'", "'-'", "'*'", "'/'", "'%'", "'('", "')'", "'{'", "'}'", 
			"'='", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'println'", "'func'", 
			"'package'", "'var'", "'read_int'", "'read_str'", "'return'", "'for'", 
			"'if'", "'else'", "'main'", "'function'", "'int'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PLUS", "MINUS", "TIMES", "OVER", "REM", "OP_PAR", "CL_PAR", "OP_CUR", 
			"CL_CUR", "ATTRIB", "EQ", "NE", "LT", "LE", "GT", "GE", "PRINTLN", "FUNC", 
			"PACKAGE", "VAR", "READ_INT", "READ_STR", "RETURN", "FOR", "IF", "ELSE", 
			"MAIN", "FUNCTION", "INT", "NUMBER", "NAME", "STRING", "SPACE", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Tiny.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TinyParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode PACKAGE() { return getToken(TinyParser.PACKAGE, 0); }
		public TerminalNode MAIN() { return getToken(TinyParser.MAIN, 0); }
		public MainContext main() {
			return getRuleContext(MainContext.class,0);
		}
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(PACKAGE);
			setState(29);
			match(MAIN);
			if 1:
			        print('.source Test.src')
			        print('.class  public Test')
			        print('.super  java/lang/Object\n')
			        print('.method public <init>()V')
			        print('    aload_0')
			        print('    invokenonvirtual java/lang/Object/<init>()V')
			        print('    return')
			        print('.end method\n')
			    
			setState(34);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(31);
					function();
					}
					} 
				}
				setState(36);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(37);
			main();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public Token NAME;
		public StatementContext e;
		public TerminalNode FUNC() { return getToken(TinyParser.FUNC, 0); }
		public List<TerminalNode> NAME() { return getTokens(TinyParser.NAME); }
		public TerminalNode NAME(int i) {
			return getToken(TinyParser.NAME, i);
		}
		public TerminalNode OP_PAR() { return getToken(TinyParser.OP_PAR, 0); }
		public List<TerminalNode> INT() { return getTokens(TinyParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(TinyParser.INT, i);
		}
		public TerminalNode CL_PAR() { return getToken(TinyParser.CL_PAR, 0); }
		public TerminalNode OP_CUR() { return getToken(TinyParser.OP_CUR, 0); }
		public TerminalNode CL_CUR() { return getToken(TinyParser.CL_CUR, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(39);
			match(FUNC);
			setState(40);
			((FunctionContext)_localctx).NAME = match(NAME);
			setState(41);
			match(OP_PAR);
			if 1:
			        if (((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null) in func_table:
			            print("error: function " + (((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null) + " already declared",file=sys.stderr)
			        else:
			            print('.method public static ' + (((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null) +'(I)I\n')
			            func_table.append((((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null))
			    
			setState(43);
			((FunctionContext)_localctx).NAME = match(NAME);
			if 1:
			        symbol_table.append((((FunctionContext)_localctx).NAME!=null?((FunctionContext)_localctx).NAME.getText():null))
			        usedVars.append(False)
			        type_table.append('i')
			    
			setState(45);
			match(INT);
			setState(46);
			match(CL_PAR);
			setState(47);
			match(INT);
			setState(48);
			match(OP_CUR);
			setState(52);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINTLN) | (1L << VAR) | (1L << RETURN) | (1L << FOR) | (1L << IF) | (1L << NAME))) != 0)) {
				{
				{
				setState(49);
				((FunctionContext)_localctx).e = statement();
				}
				}
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			if 1:
			        if(((FunctionContext)_localctx).e.type == 'function'):
			            aux = False

			            for i in range (len(usedVars)):
			                if (usedVars[i] == False):
			                    print("Warning: " + symbol_table[i] + " is defined but never used",file=sys.stderr)

			                    aux = True
			            if (((FunctionContext)_localctx).e.type == 'error'):
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
			        
			        
			    
			setState(56);
			match(CL_CUR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MainContext extends ParserRuleContext {
		public StatementContext e;
		public TerminalNode FUNC() { return getToken(TinyParser.FUNC, 0); }
		public TerminalNode MAIN() { return getToken(TinyParser.MAIN, 0); }
		public TerminalNode OP_PAR() { return getToken(TinyParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(TinyParser.CL_PAR, 0); }
		public TerminalNode OP_CUR() { return getToken(TinyParser.OP_CUR, 0); }
		public TerminalNode CL_CUR() { return getToken(TinyParser.CL_CUR, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public MainContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main; }
	}

	public final MainContext main() throws RecognitionException {
		MainContext _localctx = new MainContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_main);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(FUNC);
			setState(59);
			match(MAIN);
			setState(60);
			match(OP_PAR);
			setState(61);
			match(CL_PAR);
			setState(62);
			match(OP_CUR);
			if 1:
			        print('.method public static main([Ljava/lang/String;)V\n')
			    
			setState(67);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINTLN) | (1L << VAR) | (1L << RETURN) | (1L << FOR) | (1L << IF) | (1L << NAME))) != 0)) {
				{
				{
				setState(64);
				((MainContext)_localctx).e = statement();
				}
				}
				setState(69);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			if 1:
			        if(((MainContext)_localctx).e.type != 'function'):
			            aux = False

			            for i in range (len(usedVars)):
			                if (usedVars[i] == False):
			                    print("Warning: " + symbol_table[i] + " is defined but never used",file=sys.stderr)

			                    aux = True
			            if (((MainContext)_localctx).e.type == 'error'):
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
			        elif(((MainContext)_localctx).e.type == 'function'):
			            print('error: return statement cannot be used inside main',file=sys.stderr)
			            sys.exit()
			    
			setState(71);
			match(CL_CUR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public  type;
		public St_returnContext ef;
		public St_printContext st_print() {
			return getRuleContext(St_printContext.class,0);
		}
		public St_declContext st_decl() {
			return getRuleContext(St_declContext.class,0);
		}
		public St_attribContext st_attrib() {
			return getRuleContext(St_attribContext.class,0);
		}
		public St_forContext st_for() {
			return getRuleContext(St_forContext.class,0);
		}
		public St_ifContext st_if() {
			return getRuleContext(St_ifContext.class,0);
		}
		public St_returnContext st_return() {
			return getRuleContext(St_returnContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statement);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRINTLN:
				enterOuterAlt(_localctx, 1);
				{
				setState(73);
				st_print();
				}
				break;
			case VAR:
				enterOuterAlt(_localctx, 2);
				{
				setState(74);
				st_decl();
				}
				break;
			case NAME:
				enterOuterAlt(_localctx, 3);
				{
				setState(75);
				st_attrib();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 4);
				{
				setState(76);
				st_for();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 5);
				{
				setState(77);
				st_if();
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 6);
				{
				setState(78);
				((StatementContext)_localctx).ef = st_return();
				if 1:
				        _localctx.type = ((StatementContext)_localctx).ef.typeFuc
				    
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_printContext extends ParserRuleContext {
		public ExpressionContext e;
		public TerminalNode PRINTLN() { return getToken(TinyParser.PRINTLN, 0); }
		public TerminalNode OP_PAR() { return getToken(TinyParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(TinyParser.CL_PAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public St_printContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_print; }
	}

	public final St_printContext st_print() throws RecognitionException {
		St_printContext _localctx = new St_printContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_st_print);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(PRINTLN);
			setState(84);
			match(OP_PAR);
			if 1:
			        emit('    getstatic java/lang/System/out Ljava/io/PrintStream;', 1)
			        #+1 na pilha
			    
			setState(86);
			((St_printContext)_localctx).e = expression();
			if 1:
			        if (((St_printContext)_localctx).e.type == 'i'):
			            emit('    invokevirtual java/io/PrintStream/println(I)V\n', -2)
			            
			        elif (((St_printContext)_localctx).e.type == 's'):
			            emit('    invokevirtual java/io/PrintStream/println(Ljava/lang/String;)V\n', -2)
			        else:
			            print(((St_printContext)_localctx).e.type)
			    
			setState(88);
			match(CL_PAR);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_declContext extends ParserRuleContext {
		public Token NAME;
		public ExpressionContext e;
		public TerminalNode VAR() { return getToken(TinyParser.VAR, 0); }
		public TerminalNode NAME() { return getToken(TinyParser.NAME, 0); }
		public TerminalNode ATTRIB() { return getToken(TinyParser.ATTRIB, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public St_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_decl; }
	}

	public final St_declContext st_decl() throws RecognitionException {
		St_declContext _localctx = new St_declContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_st_decl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(VAR);
			setState(91);
			((St_declContext)_localctx).NAME = match(NAME);
			if 1:
			        if (len(symbol_table) == 0):
			            symbol_table.append((((St_declContext)_localctx).NAME!=null?((St_declContext)_localctx).NAME.getText():null))
			        else:
			            if (((St_declContext)_localctx).NAME!=null?((St_declContext)_localctx).NAME.getText():null) in symbol_table:
			                print("Variable " + (((St_declContext)_localctx).NAME!=null?((St_declContext)_localctx).NAME.getText():null) + " redeclared in this block.",file=sys.stderr)
			                sys.exit()
			            else:
			                symbol_table.append((((St_declContext)_localctx).NAME!=null?((St_declContext)_localctx).NAME.getText():null))

			        #se existe, gera erro de redeclaracao e para
			    
			setState(93);
			match(ATTRIB);
			setState(94);
			((St_declContext)_localctx).e = expression();
			if 1:
			        if(((St_declContext)_localctx).e.type == 'i'):            #type of int
			            index = symbol_table.index((((St_declContext)_localctx).NAME!=null?((St_declContext)_localctx).NAME.getText():null))
			            usedVars.append(False)
			            type_table.append('i')
			            store = '    istore ' + str(index)  + '\n'
			            emit(store, -1)            #istore ==> -1 na pilha
			                                       
			        if(((St_declContext)_localctx).e.type == 's'):            #type of string
			            index = symbol_table.index((((St_declContext)_localctx).NAME!=null?((St_declContext)_localctx).NAME.getText():null))
			            type_table.append('s')
			            usedVars.append(False)
			            store = '    astore ' + str(index) + '\n'
			            emit(store, -1)
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_forContext extends ParserRuleContext {
		public ComparisonContext op;
		public TerminalNode FOR() { return getToken(TinyParser.FOR, 0); }
		public TerminalNode OP_CUR() { return getToken(TinyParser.OP_CUR, 0); }
		public TerminalNode CL_CUR() { return getToken(TinyParser.CL_CUR, 0); }
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public St_forContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_for; }
	}

	public final St_forContext st_for() throws RecognitionException {
		St_forContext _localctx = new St_forContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_st_for);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			if 1:
			        localCount = countFor
			        plusCount(countFor)
			        localCount += 1
			        print(beginFor + str(localCount) + ':')
			    
			setState(98);
			match(FOR);
			setState(99);
			((St_forContext)_localctx).op = comparison();
			if 1:
			        if ((St_forContext)_localctx).op.bytecode == 'error':
			            print('error: FOR operands must be integers!!!',file=sys.stderr)
			            sys.exit()
			        else:
			            emit('    ' + ((St_forContext)_localctx).op.bytecode + ' ' + endFor + str(localCount),-2)
			    
			setState(101);
			match(OP_CUR);
			setState(105);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINTLN) | (1L << VAR) | (1L << RETURN) | (1L << FOR) | (1L << IF) | (1L << NAME))) != 0)) {
				{
				{
				setState(102);
				statement();
				}
				}
				setState(107);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(108);
			match(CL_CUR);
			if 1:
			        emit('    goto   ' + beginFor + str(localCount), 0)
			        print(endFor + str(localCount) + ':')
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_returnContext extends ParserRuleContext {
		public  typeFuc;
		public ExpressionContext e;
		public TerminalNode RETURN() { return getToken(TinyParser.RETURN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public St_returnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_return; }
	}

	public final St_returnContext st_return() throws RecognitionException {
		St_returnContext _localctx = new St_returnContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_st_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(RETURN);
			setState(112);
			((St_returnContext)_localctx).e = expression();
			if 1:
			        if(((St_returnContext)_localctx).e.type == 'i'):
			            emit('    ireturn',-1)
			            _localctx.typeFuc = 'function'
			        elif(((St_returnContext)_localctx).e.type == 's'):
			            print('error: return value must be of integer type',file=sys.stderr)
			            _localctx.typeFuc = 'function'
			        
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_ifContext extends ParserRuleContext {
		public  type;
		public ComparisonContext op;
		public TerminalNode IF() { return getToken(TinyParser.IF, 0); }
		public List<TerminalNode> OP_CUR() { return getTokens(TinyParser.OP_CUR); }
		public TerminalNode OP_CUR(int i) {
			return getToken(TinyParser.OP_CUR, i);
		}
		public List<TerminalNode> CL_CUR() { return getTokens(TinyParser.CL_CUR); }
		public TerminalNode CL_CUR(int i) {
			return getToken(TinyParser.CL_CUR, i);
		}
		public ComparisonContext comparison() {
			return getRuleContext(ComparisonContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(TinyParser.ELSE, 0); }
		public St_ifContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_if; }
	}

	public final St_ifContext st_if() throws RecognitionException {
		St_ifContext _localctx = new St_ifContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_st_if);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(IF);
			setState(116);
			((St_ifContext)_localctx).op = comparison();
			if 1:
			        if ((St_ifContext)_localctx).op.bytecode == 'error':
			            print('error: IF operands must be integers!!!',file=sys.stderr)
			            _localctx.type = 'error'
			            sys.exit()
			        else:
			            global counterIf
			            counterIf += 1
			            localCount = counterIf
			            hasElse = False
			            emit('    ' + ((St_ifContext)_localctx).op.bytecode + ' NOT_IF_' + str(localCount),-2)

			    
			setState(118);
			match(OP_CUR);
			setState(122);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINTLN) | (1L << VAR) | (1L << RETURN) | (1L << FOR) | (1L << IF) | (1L << NAME))) != 0)) {
				{
				{
				setState(119);
				statement();
				}
				}
				setState(124);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(125);
			match(CL_CUR);
			setState(136);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				if 1:
				        hasElse = True
				        emit('    goto END_ELSE_' + str(localCount),0)
				        print('NOT_IF_' + str(localCount) + ':')
				    
				setState(127);
				match(ELSE);
				setState(128);
				match(OP_CUR);
				setState(132);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << PRINTLN) | (1L << VAR) | (1L << RETURN) | (1L << FOR) | (1L << IF) | (1L << NAME))) != 0)) {
					{
					{
					setState(129);
					statement();
					}
					}
					setState(134);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(135);
				match(CL_CUR);
				}
			}

			if 1:
			        if(hasElse):
			            emit('END_ELSE_' + str(localCount) + ':',0)
			        else:
			            print('NOT_IF_' + str(localCount) + ':')
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ComparisonContext extends ParserRuleContext {
		public  bytecode;
		public ExpressionContext e1;
		public Token op;
		public ExpressionContext e2;
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(TinyParser.EQ, 0); }
		public TerminalNode NE() { return getToken(TinyParser.NE, 0); }
		public TerminalNode LT() { return getToken(TinyParser.LT, 0); }
		public TerminalNode LE() { return getToken(TinyParser.LE, 0); }
		public TerminalNode GT() { return getToken(TinyParser.GT, 0); }
		public TerminalNode GE() { return getToken(TinyParser.GE, 0); }
		public ComparisonContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison; }
	}

	public final ComparisonContext comparison() throws RecognitionException {
		ComparisonContext _localctx = new ComparisonContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_comparison);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			((ComparisonContext)_localctx).e1 = expression();
			setState(141);
			((ComparisonContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQ) | (1L << NE) | (1L << LT) | (1L << LE) | (1L << GT) | (1L << GE))) != 0)) ) {
				((ComparisonContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(142);
			((ComparisonContext)_localctx).e2 = expression();
			if 1:
			        if(((ComparisonContext)_localctx).e1.type == 'i' and ((ComparisonContext)_localctx).e2.type == 'i'):
			            if (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == TinyParser.EQ:
			                _localctx.bytecode = 'if_icmpne'         #faz uma comparacao entre dois valores interios na pilha
			            elif (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == TinyParser.NE:
			                _localctx.bytecode = 'if_icmpeq'
			            elif (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == TinyParser.LT:
			                _localctx.bytecode = 'if_icmpge'
			            elif (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == TinyParser.LE:
			                _localctx.bytecode = 'if_icmpgt'     #fazer o inverso
			            elif (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == TinyParser.GT:
			                _localctx.bytecode = 'if_icmple'
			            elif (((ComparisonContext)_localctx).op!=null?((ComparisonContext)_localctx).op.getType():0) == TinyParser.GE:
			                _localctx.bytecode = 'if_icmplt'
			        else:
			            _localctx.bytecode = 'error'
			            
			    
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class St_attribContext extends ParserRuleContext {
		public  type;
		public Token NAME;
		public ExpressionContext e;
		public TerminalNode NAME() { return getToken(TinyParser.NAME, 0); }
		public TerminalNode ATTRIB() { return getToken(TinyParser.ATTRIB, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public St_attribContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_st_attrib; }
	}

	public final St_attribContext st_attrib() throws RecognitionException {
		St_attribContext _localctx = new St_attribContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_st_attrib);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(145);
			((St_attribContext)_localctx).NAME = match(NAME);
			if 1:
			        if (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) in symbol_table:
			            pass
			        else:
			            print("error: Variable " + (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) + " is not declared.",file=sys.stderr)
			            sys.exit()
			    
			setState(147);
			match(ATTRIB);
			setState(148);
			((St_attribContext)_localctx).e = expression();
			if 1:
			        index = symbol_table.index((((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null))
			        if(((St_attribContext)_localctx).e.type == 'i' and type_table[index] == 'i'):
			            usedVars[index] = True
			            emit('    istore ' + str(index), -1)
			    
			        elif(((St_attribContext)_localctx).e.type == 's' and type_table[index] == 'i'):
			            store = 'error: ' + (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) + ' is a integer\n'
			            print(store ,file=sys.stderr)
			        
			        elif(((St_attribContext)_localctx).e.type == 's' and type_table[index] == 's'):
			            usedVars[index] = True
			            emit('    astore ' + str(index), -1)
			        
			        elif(((St_attribContext)_localctx).e.type == 'i' and type_table[index] == 's'):
			            store = 'error: ' + (((St_attribContext)_localctx).NAME!=null?((St_attribContext)_localctx).NAME.getText():null) + ' is a string\n'
			            print(store ,file=sys.stderr)



			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public  type;
		public TermContext t1;
		public Token op;
		public TermContext t2;
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(TinyParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(TinyParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(TinyParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(TinyParser.MINUS, i);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(151);
			((ExpressionContext)_localctx).t1 = term();
			setState(158);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==PLUS || _la==MINUS) {
				{
				{
				setState(152);
				((ExpressionContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==PLUS || _la==MINUS) ) {
					((ExpressionContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(153);
				((ExpressionContext)_localctx).t2 = term();
				if 1:
				        if(((ExpressionContext)_localctx).t1.type == 'i' and ((ExpressionContext)_localctx).t2.type == 'i'):
				            if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == TinyParser.PLUS:
				                emit('    iadd', -1)
				            if (((ExpressionContext)_localctx).op!=null?((ExpressionContext)_localctx).op.getType():0) == TinyParser.MINUS:
				                emit('    isub', -1)
				        else:
				            _localctx.type = 'error'
				            print('error: (+ and -) operands must be integers',file=sys.stderr)
				    
				}
				}
				setState(160);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			if 1:
			        _localctx.type = ((ExpressionContext)_localctx).t1.type
			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TermContext extends ParserRuleContext {
		public  type;
		public FactorContext f1;
		public Token op;
		public FactorContext f2;
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> TIMES() { return getTokens(TinyParser.TIMES); }
		public TerminalNode TIMES(int i) {
			return getToken(TinyParser.TIMES, i);
		}
		public List<TerminalNode> OVER() { return getTokens(TinyParser.OVER); }
		public TerminalNode OVER(int i) {
			return getToken(TinyParser.OVER, i);
		}
		public List<TerminalNode> REM() { return getTokens(TinyParser.REM); }
		public TerminalNode REM(int i) {
			return getToken(TinyParser.REM, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_term);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			((TermContext)_localctx).f1 = factor();
			setState(170);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) {
				{
				{
				setState(164);
				((TermContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << TIMES) | (1L << OVER) | (1L << REM))) != 0)) ) {
					((TermContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(165);
				((TermContext)_localctx).f2 = factor();
				if 1:
				        if(((TermContext)_localctx).f1.type == 'i' and ((TermContext)_localctx).f2.type == 'i'):    
				            #lcd,imul,idiv,irem ==> -1 na pilha
				            if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == TinyParser.TIMES:
				                emit('    imul', -1)
				            if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == TinyParser.OVER:
				                emit('    idiv', -1)
				            if (((TermContext)_localctx).op!=null?((TermContext)_localctx).op.getType():0) == TinyParser.REM:
				                emit('    irem', -1)
				        else:
				            _localctx.type = 'error'
				            print('error: (* , / and %) operands must be integers!',file=sys.stderr)
				    
				}
				}
				setState(172);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			if 1:
			        _localctx.type = ((TermContext)_localctx).f1.type

			    
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FactorContext extends ParserRuleContext {
		public  type;
		public Token NUMBER;
		public ExpressionContext e;
		public Token NAME;
		public Token STRING;
		public TerminalNode NUMBER() { return getToken(TinyParser.NUMBER, 0); }
		public TerminalNode OP_PAR() { return getToken(TinyParser.OP_PAR, 0); }
		public TerminalNode CL_PAR() { return getToken(TinyParser.CL_PAR, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode NAME() { return getToken(TinyParser.NAME, 0); }
		public TerminalNode READ_INT() { return getToken(TinyParser.READ_INT, 0); }
		public TerminalNode STRING() { return getToken(TinyParser.STRING, 0); }
		public TerminalNode READ_STR() { return getToken(TinyParser.READ_STR, 0); }
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_factor);
		try {
			setState(200);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(175);
				((FactorContext)_localctx).NUMBER = match(NUMBER);
				if 1:
				        store = '    ldc ' + (((FactorContext)_localctx).NUMBER!=null?((FactorContext)_localctx).NUMBER.getText():null)
				        emit(store, 1)

				        _localctx.type = 'i'
				        # essa regra resultou em 'inteiro'
				    
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(177);
				match(OP_PAR);
				setState(178);
				((FactorContext)_localctx).e = expression();
				setState(179);
				match(CL_PAR);
				if 1:
				        _localctx.type = ((FactorContext)_localctx).e.type

				    
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(182);
				((FactorContext)_localctx).NAME = match(NAME);
				setState(183);
				match(OP_PAR);
				setState(184);
				((FactorContext)_localctx).e = expression();
				setState(185);
				match(CL_PAR);
				if 1:
				        if((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) in func_table):
				            emit('    invokestatic Test/'+(((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null)+'(I)I',0)
				            _localctx.type = ((FactorContext)_localctx).e.type
				            if(((FactorContext)_localctx).e.type == 's'):
				                print("error: argument must be integer",file=sys.stderr)
				        else:
				            print("error: function " + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + " not declared",file=sys.stderr)

				        
				    
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(188);
				((FactorContext)_localctx).NAME = match(NAME);
				if 1:
				        #verificar se NAME existe
				        if (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) in symbol_table:
				            index = symbol_table.index((((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null))
				            typeValue = type_table[index]

				            if(typeValue == 'i'):
				                usedVars[index] = True
				                emit('    iload ' + str(index), 1)
				                _localctx.type = 'i'

				            elif(typeValue == 's'):
				                usedVars[index] = True
				                emit('    aload ' + str(index), 1)
				                _localctx.type = 's'

				        #iload +1 ==> na piha aumenta, visto que carrega o valor 
				        #se nao existe, gera erro e para
				        else:
				            print("error: Variable " + (((FactorContext)_localctx).NAME!=null?((FactorContext)_localctx).NAME.getText():null) + " is not declared.",file=sys.stderr)
				            sys.exit()

				        #verificar o tipo na tabela de tipos
				        # _localctx.type = 'i' ou _localctx.type = 's'
				        #_localctx.type = ???
				    
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(190);
				match(READ_INT);
				setState(191);
				match(OP_PAR);
				setState(192);
				match(CL_PAR);
				if 1:
				        emit('    invokestatic Runtime/readInt()I', 1)
				        #+1 na pilha
				        #comando da biblioteca Runtime.java
				        _localctx.type = 'i'
				    
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(194);
				((FactorContext)_localctx).STRING = match(STRING);
				if 1:
				        store = '    ldc  ' + (((FactorContext)_localctx).STRING!=null?((FactorContext)_localctx).STRING.getText():null)
				        emit(store, 1)
				        _localctx.type = 's'
				        

				    
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(196);
				match(READ_STR);
				setState(197);
				match(OP_PAR);
				setState(198);
				match(CL_PAR);
				if 1:
				        emit('    invokestatic Runtime/readString()Ljava/lang/String;', 1)
				        _localctx.type = 's'
				    
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3$\u00cd\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\2\3\2\7\2#\n\2\f\2\16"+
		"\2&\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\65\n"+
		"\3\f\3\16\38\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4D\n\4\f\4"+
		"\16\4G\13\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5T\n\5\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b"+
		"\3\b\7\bj\n\b\f\b\16\bm\13\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3"+
		"\n\3\n\7\n{\n\n\f\n\16\n~\13\n\3\n\3\n\3\n\3\n\3\n\7\n\u0085\n\n\f\n\16"+
		"\n\u0088\13\n\3\n\5\n\u008b\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\7\r\u009f\n\r\f\r\16\r\u00a2\13"+
		"\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\7\16\u00ab\n\16\f\16\16\16\u00ae\13"+
		"\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5"+
		"\17\u00cb\n\17\3\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\5\3\2"+
		"\r\22\3\2\3\4\3\2\5\7\2\u00d2\2\36\3\2\2\2\4)\3\2\2\2\6<\3\2\2\2\bS\3"+
		"\2\2\2\nU\3\2\2\2\f\\\3\2\2\2\16c\3\2\2\2\20q\3\2\2\2\22u\3\2\2\2\24\u008e"+
		"\3\2\2\2\26\u0093\3\2\2\2\30\u0099\3\2\2\2\32\u00a5\3\2\2\2\34\u00ca\3"+
		"\2\2\2\36\37\7\25\2\2\37 \7\35\2\2 $\b\2\1\2!#\5\4\3\2\"!\3\2\2\2#&\3"+
		"\2\2\2$\"\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'(\5\6\4\2(\3\3\2\2\2"+
		")*\7\24\2\2*+\7!\2\2+,\7\b\2\2,-\b\3\1\2-.\7!\2\2./\b\3\1\2/\60\7\37\2"+
		"\2\60\61\7\t\2\2\61\62\7\37\2\2\62\66\7\n\2\2\63\65\5\b\5\2\64\63\3\2"+
		"\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\679\3\2\2\28\66\3\2\2\29"+
		":\b\3\1\2:;\7\13\2\2;\5\3\2\2\2<=\7\24\2\2=>\7\35\2\2>?\7\b\2\2?@\7\t"+
		"\2\2@A\7\n\2\2AE\b\4\1\2BD\5\b\5\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2"+
		"\2\2FH\3\2\2\2GE\3\2\2\2HI\b\4\1\2IJ\7\13\2\2J\7\3\2\2\2KT\5\n\6\2LT\5"+
		"\f\7\2MT\5\26\f\2NT\5\16\b\2OT\5\22\n\2PQ\5\20\t\2QR\b\5\1\2RT\3\2\2\2"+
		"SK\3\2\2\2SL\3\2\2\2SM\3\2\2\2SN\3\2\2\2SO\3\2\2\2SP\3\2\2\2T\t\3\2\2"+
		"\2UV\7\23\2\2VW\7\b\2\2WX\b\6\1\2XY\5\30\r\2YZ\b\6\1\2Z[\7\t\2\2[\13\3"+
		"\2\2\2\\]\7\26\2\2]^\7!\2\2^_\b\7\1\2_`\7\f\2\2`a\5\30\r\2ab\b\7\1\2b"+
		"\r\3\2\2\2cd\b\b\1\2de\7\32\2\2ef\5\24\13\2fg\b\b\1\2gk\7\n\2\2hj\5\b"+
		"\5\2ih\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3\2\2\2ln\3\2\2\2mk\3\2\2\2no\7\13"+
		"\2\2op\b\b\1\2p\17\3\2\2\2qr\7\31\2\2rs\5\30\r\2st\b\t\1\2t\21\3\2\2\2"+
		"uv\7\33\2\2vw\5\24\13\2wx\b\n\1\2x|\7\n\2\2y{\5\b\5\2zy\3\2\2\2{~\3\2"+
		"\2\2|z\3\2\2\2|}\3\2\2\2}\177\3\2\2\2~|\3\2\2\2\177\u008a\7\13\2\2\u0080"+
		"\u0081\b\n\1\2\u0081\u0082\7\34\2\2\u0082\u0086\7\n\2\2\u0083\u0085\5"+
		"\b\5\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3\2\2\2\u0086"+
		"\u0087\3\2\2\2\u0087\u0089\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008b\7\13"+
		"\2\2\u008a\u0080\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\3\2\2\2\u008c"+
		"\u008d\b\n\1\2\u008d\23\3\2\2\2\u008e\u008f\5\30\r\2\u008f\u0090\t\2\2"+
		"\2\u0090\u0091\5\30\r\2\u0091\u0092\b\13\1\2\u0092\25\3\2\2\2\u0093\u0094"+
		"\7!\2\2\u0094\u0095\b\f\1\2\u0095\u0096\7\f\2\2\u0096\u0097\5\30\r\2\u0097"+
		"\u0098\b\f\1\2\u0098\27\3\2\2\2\u0099\u00a0\5\32\16\2\u009a\u009b\t\3"+
		"\2\2\u009b\u009c\5\32\16\2\u009c\u009d\b\r\1\2\u009d\u009f\3\2\2\2\u009e"+
		"\u009a\3\2\2\2\u009f\u00a2\3\2\2\2\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2"+
		"\2\2\u00a1\u00a3\3\2\2\2\u00a2\u00a0\3\2\2\2\u00a3\u00a4\b\r\1\2\u00a4"+
		"\31\3\2\2\2\u00a5\u00ac\5\34\17\2\u00a6\u00a7\t\4\2\2\u00a7\u00a8\5\34"+
		"\17\2\u00a8\u00a9\b\16\1\2\u00a9\u00ab\3\2\2\2\u00aa\u00a6\3\2\2\2\u00ab"+
		"\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad\u00af\3\2"+
		"\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\b\16\1\2\u00b0\33\3\2\2\2\u00b1\u00b2"+
		"\7 \2\2\u00b2\u00cb\b\17\1\2\u00b3\u00b4\7\b\2\2\u00b4\u00b5\5\30\r\2"+
		"\u00b5\u00b6\7\t\2\2\u00b6\u00b7\b\17\1\2\u00b7\u00cb\3\2\2\2\u00b8\u00b9"+
		"\7!\2\2\u00b9\u00ba\7\b\2\2\u00ba\u00bb\5\30\r\2\u00bb\u00bc\7\t\2\2\u00bc"+
		"\u00bd\b\17\1\2\u00bd\u00cb\3\2\2\2\u00be\u00bf\7!\2\2\u00bf\u00cb\b\17"+
		"\1\2\u00c0\u00c1\7\27\2\2\u00c1\u00c2\7\b\2\2\u00c2\u00c3\7\t\2\2\u00c3"+
		"\u00cb\b\17\1\2\u00c4\u00c5\7\"\2\2\u00c5\u00cb\b\17\1\2\u00c6\u00c7\7"+
		"\30\2\2\u00c7\u00c8\7\b\2\2\u00c8\u00c9\7\t\2\2\u00c9\u00cb\b\17\1\2\u00ca"+
		"\u00b1\3\2\2\2\u00ca\u00b3\3\2\2\2\u00ca\u00b8\3\2\2\2\u00ca\u00be\3\2"+
		"\2\2\u00ca\u00c0\3\2\2\2\u00ca\u00c4\3\2\2\2\u00ca\u00c6\3\2\2\2\u00cb"+
		"\35\3\2\2\2\r$\66ESk|\u0086\u008a\u00a0\u00ac\u00ca";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}