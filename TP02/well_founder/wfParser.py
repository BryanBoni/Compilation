# Generated from wf.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\23\n\3\3\3\3\3\3\3\3\3\7\3\31\n\3\f\3")
        buf.write("\16\3\34\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4&\n\4")
        buf.write("\3\5\3\5\3\5\2\3\4\6\2\4\6\b\2\3\3\2\b\13\2)\2\n\3\2\2")
        buf.write("\2\4\22\3\2\2\2\6%\3\2\2\2\b\'\3\2\2\2\n\13\5\4\3\2\13")
        buf.write("\f\7\3\2\2\f\3\3\2\2\2\r\16\b\3\1\2\16\17\7\r\2\2\17\23")
        buf.write("\b\3\1\2\20\23\5\6\4\2\21\23\7\f\2\2\22\r\3\2\2\2\22\20")
        buf.write("\3\2\2\2\22\21\3\2\2\2\23\32\3\2\2\2\24\25\f\6\2\2\25")
        buf.write("\26\5\b\5\2\26\27\5\4\3\7\27\31\3\2\2\2\30\24\3\2\2\2")
        buf.write("\31\34\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\5\3\2\2")
        buf.write("\2\34\32\3\2\2\2\35\36\7\4\2\2\36\37\5\4\3\2\37 \7\5\2")
        buf.write("\2 &\3\2\2\2!\"\7\6\2\2\"#\5\4\3\2#$\7\7\2\2$&\3\2\2\2")
        buf.write("%\35\3\2\2\2%!\3\2\2\2&\7\3\2\2\2\'(\t\2\2\2(\t\3\2\2")
        buf.write("\2\5\22\32%")
        return buf.getvalue()


class wfParser ( Parser ):

    grammarFileName = "wf.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'['", "']'", "'('", "')'", "'+'", 
                     "'*'", "'-'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "ID", "WS" ]

    RULE_r = 0
    RULE_expr = 1
    RULE_paranthese = 2
    RULE_op = 3

    ruleNames =  [ "r", "expr", "paranthese", "op" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    INT=10
    ID=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(wfParser.ExprContext,0)


        def getRuleIndex(self):
            return wfParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)




    def r(self):

        localctx = wfParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.expr(0)
            self.state = 9
            self.match(wfParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(wfParser.ID, 0)

        def paranthese(self):
            return self.getTypedRuleContext(wfParser.ParantheseContext,0)


        def INT(self):
            return self.getToken(wfParser.INT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(wfParser.ExprContext)
            else:
                return self.getTypedRuleContext(wfParser.ExprContext,i)


        def op(self):
            return self.getTypedRuleContext(wfParser.OpContext,0)


        def getRuleIndex(self):
            return wfParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = wfParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [wfParser.ID]:
                self.state = 12
                localctx._ID = self.match(wfParser.ID)
                print('oh an id : '+(None if localctx._ID is None else localctx._ID.text));
                pass
            elif token in [wfParser.T__1, wfParser.T__3]:
                self.state = 14
                self.paranthese()
                pass
            elif token in [wfParser.INT]:
                self.state = 15
                self.match(wfParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = wfParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 18
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 19
                    self.op()
                    self.state = 20
                    self.expr(5) 
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ParantheseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(wfParser.ExprContext,0)


        def getRuleIndex(self):
            return wfParser.RULE_paranthese

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParanthese" ):
                listener.enterParanthese(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParanthese" ):
                listener.exitParanthese(self)




    def paranthese(self):

        localctx = wfParser.ParantheseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_paranthese)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [wfParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(wfParser.T__1)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(wfParser.T__2)
                pass
            elif token in [wfParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(wfParser.T__3)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(wfParser.T__4)
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

    class OpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return wfParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = wfParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << wfParser.T__5) | (1 << wfParser.T__6) | (1 << wfParser.T__7) | (1 << wfParser.T__8))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




