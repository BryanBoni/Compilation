# Generated from Arit.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AritParser import AritParser
else:
    from AritParser import AritParser

# This class defines a complete generic visitor for a parse tree produced by AritParser.

class AritVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AritParser#statementList.
    def visitStatementList(self, ctx:AritParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#exprInstr.
    def visitExprInstr(self, ctx:AritParser.ExprInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#assignInstr.
    def visitAssignInstr(self, ctx:AritParser.AssignInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#multiplicationExpr.
    def visitMultiplicationExpr(self, ctx:AritParser.MultiplicationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#atomExpr.
    def visitAtomExpr(self, ctx:AritParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#additiveExpr.
    def visitAdditiveExpr(self, ctx:AritParser.AdditiveExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#numberAtom.
    def visitNumberAtom(self, ctx:AritParser.NumberAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#idAtom.
    def visitIdAtom(self, ctx:AritParser.IdAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#parens.
    def visitParens(self, ctx:AritParser.ParensContext):
        return self.visitChildren(ctx)



del AritParser