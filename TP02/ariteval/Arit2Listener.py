# Generated from Arit2.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Arit2Parser import Arit2Parser
else:
    from Arit2Parser import Arit2Parser

# header - mettre les variables globales 
import sys
idTab = {};

class UnknownIdentifier(Exception):
    pass


# This class defines a complete listener for a parse tree produced by Arit2Parser.
class Arit2Listener(ParseTreeListener):

    # Enter a parse tree produced by Arit2Parser#prog.
    def enterProg(self, ctx:Arit2Parser.ProgContext):
        pass

    # Exit a parse tree produced by Arit2Parser#prog.
    def exitProg(self, ctx:Arit2Parser.ProgContext):
        pass


    # Enter a parse tree produced by Arit2Parser#expr.
    def enterExpr(self, ctx:Arit2Parser.ExprContext):
        pass

    # Exit a parse tree produced by Arit2Parser#expr.
    def exitExpr(self, ctx:Arit2Parser.ExprContext):
        pass


    # Enter a parse tree produced by Arit2Parser#tarte.
    def enterTarte(self, ctx:Arit2Parser.TarteContext):
        pass

    # Exit a parse tree produced by Arit2Parser#tarte.
    def exitTarte(self, ctx:Arit2Parser.TarteContext):
        pass


    # Enter a parse tree produced by Arit2Parser#frite.
    def enterFrite(self, ctx:Arit2Parser.FriteContext):
        pass

    # Exit a parse tree produced by Arit2Parser#frite.
    def exitFrite(self, ctx:Arit2Parser.FriteContext):
        pass


    # Enter a parse tree produced by Arit2Parser#affectation.
    def enterAffectation(self, ctx:Arit2Parser.AffectationContext):
        pass

    # Exit a parse tree produced by Arit2Parser#affectation.
    def exitAffectation(self, ctx:Arit2Parser.AffectationContext):
        pass


