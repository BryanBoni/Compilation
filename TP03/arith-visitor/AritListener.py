# Generated from Arit.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AritParser import AritParser
else:
    from AritParser import AritParser

# This class defines a complete listener for a parse tree produced by AritParser.
class AritListener(ParseTreeListener):

    # Enter a parse tree produced by AritParser#statementList.
    def enterStatementList(self, ctx:AritParser.StatementListContext):
        pass

    # Exit a parse tree produced by AritParser#statementList.
    def exitStatementList(self, ctx:AritParser.StatementListContext):
        pass


    # Enter a parse tree produced by AritParser#exprInstr.
    def enterExprInstr(self, ctx:AritParser.ExprInstrContext):
        pass

    # Exit a parse tree produced by AritParser#exprInstr.
    def exitExprInstr(self, ctx:AritParser.ExprInstrContext):
        pass


    # Enter a parse tree produced by AritParser#assignInstr.
    def enterAssignInstr(self, ctx:AritParser.AssignInstrContext):
        pass

    # Exit a parse tree produced by AritParser#assignInstr.
    def exitAssignInstr(self, ctx:AritParser.AssignInstrContext):
        pass


    # Enter a parse tree produced by AritParser#multiplicationExpr.
    def enterMultiplicationExpr(self, ctx:AritParser.MultiplicationExprContext):
        pass

    # Exit a parse tree produced by AritParser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx:AritParser.MultiplicationExprContext):
        pass


    # Enter a parse tree produced by AritParser#atomExpr.
    def enterAtomExpr(self, ctx:AritParser.AtomExprContext):
        pass

    # Exit a parse tree produced by AritParser#atomExpr.
    def exitAtomExpr(self, ctx:AritParser.AtomExprContext):
        pass


    # Enter a parse tree produced by AritParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:AritParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by AritParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:AritParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by AritParser#numberAtom.
    def enterNumberAtom(self, ctx:AritParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by AritParser#numberAtom.
    def exitNumberAtom(self, ctx:AritParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by AritParser#idAtom.
    def enterIdAtom(self, ctx:AritParser.IdAtomContext):
        pass

    # Exit a parse tree produced by AritParser#idAtom.
    def exitIdAtom(self, ctx:AritParser.IdAtomContext):
        pass


    # Enter a parse tree produced by AritParser#parens.
    def enterParens(self, ctx:AritParser.ParensContext):
        pass

    # Exit a parse tree produced by AritParser#parens.
    def exitParens(self, ctx:AritParser.ParensContext):
        pass


