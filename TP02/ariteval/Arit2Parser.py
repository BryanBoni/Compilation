# Generated from Arit2.g4 by ANTLR 4.7
# encoding: utf-8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("S\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\7\2\24\n\2\f\2\16\2\27\13\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\'\n")
        buf.write("\3\f\3\16\3*\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\7\4:\n\4\f\4\16\4=\13\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5L\n\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\2\4\4\6\7\2\4\6\b\n\2\2\2V\2\25")
        buf.write("\3\2\2\2\4\30\3\2\2\2\6+\3\2\2\2\bK\3\2\2\2\nM\3\2\2\2")
        buf.write("\f\r\5\4\3\2\r\16\7\3\2\2\16\17\b\2\1\2\17\24\3\2\2\2")
        buf.write("\20\21\5\n\6\2\21\22\7\3\2\2\22\24\3\2\2\2\23\f\3\2\2")
        buf.write("\2\23\20\3\2\2\2\24\27\3\2\2\2\25\23\3\2\2\2\25\26\3\2")
        buf.write("\2\2\26\3\3\2\2\2\27\25\3\2\2\2\30\31\b\3\1\2\31\32\5")
        buf.write("\6\4\2\32\33\b\3\1\2\33(\3\2\2\2\34\35\f\5\2\2\35\36\7")
        buf.write("\4\2\2\36\37\5\6\4\2\37 \b\3\1\2 \'\3\2\2\2!\"\f\4\2\2")
        buf.write("\"#\7\5\2\2#$\5\6\4\2$%\b\3\1\2%\'\3\2\2\2&\34\3\2\2\2")
        buf.write("&!\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\5\3\2\2\2*")
        buf.write("(\3\2\2\2+,\b\4\1\2,-\5\b\5\2-.\b\4\1\2.;\3\2\2\2/\60")
        buf.write("\f\5\2\2\60\61\7\6\2\2\61\62\5\b\5\2\62\63\b\4\1\2\63")
        buf.write(":\3\2\2\2\64\65\f\4\2\2\65\66\7\7\2\2\66\67\5\b\5\2\67")
        buf.write("8\b\4\1\28:\3\2\2\29/\3\2\2\29\64\3\2\2\2:=\3\2\2\2;9")
        buf.write("\3\2\2\2;<\3\2\2\2<\7\3\2\2\2=;\3\2\2\2>?\7\f\2\2?L\b")
        buf.write("\5\1\2@A\7\16\2\2AL\b\5\1\2BC\7\b\2\2CD\5\4\3\2DE\7\t")
        buf.write("\2\2EF\b\5\1\2FL\3\2\2\2GH\7\5\2\2HI\5\b\5\2IJ\b\5\1\2")
        buf.write("JL\3\2\2\2K>\3\2\2\2K@\3\2\2\2KB\3\2\2\2KG\3\2\2\2L\t")
        buf.write("\3\2\2\2MN\7\f\2\2NO\7\n\2\2OP\5\4\3\2PQ\b\6\1\2Q\13\3")
        buf.write("\2\2\2\t\23\25&(9;K")
        return buf.getvalue()


class Arit2Parser ( Parser ):

    grammarFileName = "Arit2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'+'", "'-'", "'*'", "'/'", "'('", 
                     "')'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMMENT", "ID", "WS", "INT", "NEWLINE" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_tarte = 2
    RULE_frite = 3
    RULE_affectation = 4

    ruleNames =  [ "prog", "expr", "tarte", "frite", "affectation" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    COMMENT=9
    ID=10
    WS=11
    INT=12
    NEWLINE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._expr = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Arit2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(Arit2Parser.ExprContext,i)


        def affectation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Arit2Parser.AffectationContext)
            else:
                return self.getTypedRuleContext(Arit2Parser.AffectationContext,i)


        def getRuleIndex(self):
            return Arit2Parser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = Arit2Parser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << Arit2Parser.T__2) | (1 << Arit2Parser.T__5) | (1 << Arit2Parser.ID) | (1 << Arit2Parser.INT))) != 0):
                self.state = 17
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 10
                    localctx._expr = self.expr(0)
                    self.state = 11
                    self.match(Arit2Parser.T__0)
                    print((None if localctx._expr is None else self._input.getText((localctx._expr.start,localctx._expr.stop))) + "=" +str(localctx._expr.output));
                    pass

                elif la_ == 2:
                    self.state = 14
                    self.affectation()
                    self.state = 15
                    self.match(Arit2Parser.T__0)
                    pass


                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.output = None
            self.e1 = None # ExprContext
            self.t1 = None # TarteContext

        def tarte(self):
            return self.getTypedRuleContext(Arit2Parser.TarteContext,0)


        def expr(self):
            return self.getTypedRuleContext(Arit2Parser.ExprContext,0)


        def getRuleIndex(self):
            return Arit2Parser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Arit2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            localctx.t1 = self.tarte(0)
            localctx.output =  localctx.t1.output
            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = Arit2Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 26
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 27
                        self.match(Arit2Parser.T__1)
                        self.state = 28
                        localctx.t1 = self.tarte(0)
                        localctx.output = localctx.e1.output + localctx.t1.output
                        pass

                    elif la_ == 2:
                        localctx = Arit2Parser.ExprContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 32
                        self.match(Arit2Parser.T__2)
                        self.state = 33
                        localctx.t1 = self.tarte(0)
                        localctx.output = localctx.e1.output - localctx.t1.output
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class TarteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.output = None
            self.t1 = None # TarteContext
            self.f1 = None # FriteContext

        def frite(self):
            return self.getTypedRuleContext(Arit2Parser.FriteContext,0)


        def tarte(self):
            return self.getTypedRuleContext(Arit2Parser.TarteContext,0)


        def getRuleIndex(self):
            return Arit2Parser.RULE_tarte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarte" ):
                listener.enterTarte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarte" ):
                listener.exitTarte(self)



    def tarte(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = Arit2Parser.TarteContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_tarte, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            localctx.f1 = self.frite()
            localctx.output =  localctx.f1.output
            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 55
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = Arit2Parser.TarteContext(self, _parentctx, _parentState)
                        localctx.t1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_tarte)
                        self.state = 45
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 46
                        self.match(Arit2Parser.T__3)
                        self.state = 47
                        localctx.f1 = self.frite()
                        localctx.output =  localctx.t1.output * localctx.f1.output
                        pass

                    elif la_ == 2:
                        localctx = Arit2Parser.TarteContext(self, _parentctx, _parentState)
                        localctx.t1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_tarte)
                        self.state = 50
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 51
                        self.match(Arit2Parser.T__4)
                        self.state = 52
                        localctx.f1 = self.frite()
                        localctx.output =  localctx.t1.output / localctx.f1.output
                        pass

             
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class FriteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.output = None
            self.id1 = None # Token
            self._INT = None # Token
            self._expr = None # ExprContext
            self._frite = None # FriteContext

        def ID(self):
            return self.getToken(Arit2Parser.ID, 0)

        def INT(self):
            return self.getToken(Arit2Parser.INT, 0)

        def expr(self):
            return self.getTypedRuleContext(Arit2Parser.ExprContext,0)


        def frite(self):
            return self.getTypedRuleContext(Arit2Parser.FriteContext,0)


        def getRuleIndex(self):
            return Arit2Parser.RULE_frite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrite" ):
                listener.enterFrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrite" ):
                listener.exitFrite(self)




    def frite(self):

        localctx = Arit2Parser.FriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_frite)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [Arit2Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                localctx.id1 = self.match(Arit2Parser.ID)
                if ((None if localctx.id1 is None else localctx.id1.text) not in idTab):
                    raise UnknownIdentifier((None if localctx.id1 is None else localctx.id1.text));
                else:
                    localctx.output =  idTab[(None if localctx.id1 is None else localctx.id1.text)]
                pass
            elif token in [Arit2Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                localctx._INT = self.match(Arit2Parser.INT)
                localctx.output =  (int) (None if localctx._INT is None else localctx._INT.text)
                pass
            elif token in [Arit2Parser.T__5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.match(Arit2Parser.T__5)
                self.state = 65
                localctx._expr = self.expr(0)
                self.state = 66
                self.match(Arit2Parser.T__6)
                localctx.output =  localctx._expr.output
                pass
            elif token in [Arit2Parser.T__2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.match(Arit2Parser.T__2)
                self.state = 70
                localctx._frite = self.frite()
                localctx.output =  localctx._frite.output
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

    class AffectationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.id1 = None # Token
            self.e1 = None # ExprContext

        def ID(self):
            return self.getToken(Arit2Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(Arit2Parser.ExprContext,0)


        def getRuleIndex(self):
            return Arit2Parser.RULE_affectation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAffectation" ):
                listener.enterAffectation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAffectation" ):
                listener.exitAffectation(self)




    def affectation(self):

        localctx = Arit2Parser.AffectationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_affectation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            localctx.id1 = self.match(Arit2Parser.ID)
            self.state = 76
            self.match(Arit2Parser.T__7)
            self.state = 77
            localctx.e1 = self.expr(0)
            idTab[(None if localctx.id1 is None else localctx.id1.text)]= localctx.e1.output; print((None if localctx.id1 is None else localctx.id1.text) + "now equals" + str(localctx.e1.output));
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
        self._predicates[2] = self.tarte_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def tarte_sempred(self, localctx:TarteContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




