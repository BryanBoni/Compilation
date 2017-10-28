# Generated from wf.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write(">\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\6\13/\n\13\r\13\16\13\60\3\f\6\f\64")
        buf.write("\n\f\r\f\16\f\65\3\r\6\r9\n\r\r\r\16\r:\3\r\3\r\2\2\16")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\3\2\4\4\2C\\c|\5\2\13\f\17\17\"\"\2@\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2")
        buf.write("\2\7\37\3\2\2\2\t!\3\2\2\2\13#\3\2\2\2\r%\3\2\2\2\17\'")
        buf.write("\3\2\2\2\21)\3\2\2\2\23+\3\2\2\2\25.\3\2\2\2\27\63\3\2")
        buf.write("\2\2\318\3\2\2\2\33\34\7=\2\2\34\4\3\2\2\2\35\36\7]\2")
        buf.write("\2\36\6\3\2\2\2\37 \7_\2\2 \b\3\2\2\2!\"\7*\2\2\"\n\3")
        buf.write("\2\2\2#$\7+\2\2$\f\3\2\2\2%&\7-\2\2&\16\3\2\2\2\'(\7,")
        buf.write("\2\2(\20\3\2\2\2)*\7/\2\2*\22\3\2\2\2+,\7\61\2\2,\24\3")
        buf.write("\2\2\2-/\4\62;\2.-\3\2\2\2/\60\3\2\2\2\60.\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\26\3\2\2\2\62\64\t\2\2\2\63\62\3\2\2\2")
        buf.write("\64\65\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\30\3\2\2")
        buf.write("\2\679\t\3\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:;\3\2\2")
        buf.write("\2;<\3\2\2\2<=\b\r\2\2=\32\3\2\2\2\6\2\60\65:\3\b\2\2")
        return buf.getvalue()


class wfLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    INT = 10
    ID = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'['", "']'", "'('", "')'", "'+'", "'*'", "'-'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "INT", "ID", "WS" ]

    grammarFileName = "wf.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


