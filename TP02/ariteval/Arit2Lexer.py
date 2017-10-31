# Generated from Arit2.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


# header - mettre les variables globales 
import sys
idTab = {};

class UnknownIdentifier(Exception):
    pass


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("L\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\7\n\60\n\n\f\n\16\n\63\13\n\3")
        buf.write("\n\3\n\3\13\6\138\n\13\r\13\16\139\3\f\6\f=\n\f\r\f\16")
        buf.write("\f>\3\f\3\f\3\r\6\rD\n\r\r\r\16\rE\3\16\6\16I\n\16\r\16")
        buf.write("\16\16J\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\3\2\6\4\2\f\f\17\17\4\2C\\c|\5")
        buf.write("\2\13\f\17\17\"\"\3\2\f\f\2P\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2")
        buf.write("\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r\'\3\2\2\2\17)\3")
        buf.write("\2\2\2\21+\3\2\2\2\23-\3\2\2\2\25\67\3\2\2\2\27<\3\2\2")
        buf.write("\2\31C\3\2\2\2\33H\3\2\2\2\35\36\7=\2\2\36\4\3\2\2\2\37")
        buf.write(" \7-\2\2 \6\3\2\2\2!\"\7/\2\2\"\b\3\2\2\2#$\7,\2\2$\n")
        buf.write("\3\2\2\2%&\7\61\2\2&\f\3\2\2\2\'(\7*\2\2(\16\3\2\2\2)")
        buf.write("*\7+\2\2*\20\3\2\2\2+,\7?\2\2,\22\3\2\2\2-\61\7%\2\2.")
        buf.write("\60\n\2\2\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62")
        buf.write("\3\2\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\b\n\2\2\65")
        buf.write("\24\3\2\2\2\668\t\3\2\2\67\66\3\2\2\289\3\2\2\29\67\3")
        buf.write("\2\2\29:\3\2\2\2:\26\3\2\2\2;=\t\4\2\2<;\3\2\2\2=>\3\2")
        buf.write("\2\2><\3\2\2\2>?\3\2\2\2?@\3\2\2\2@A\b\f\2\2A\30\3\2\2")
        buf.write("\2BD\4\62;\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2F")
        buf.write("\32\3\2\2\2GI\t\5\2\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK")
        buf.write("\3\2\2\2K\34\3\2\2\2\b\2\619>EJ\3\b\2\2")
        return buf.getvalue()


class Arit2Lexer(Lexer):

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
    COMMENT = 9
    ID = 10
    WS = 11
    INT = 12
    NEWLINE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT", "ID", "WS", "INT", "NEWLINE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "COMMENT", "ID", "WS", "INT", "NEWLINE" ]

    grammarFileName = "Arit2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


