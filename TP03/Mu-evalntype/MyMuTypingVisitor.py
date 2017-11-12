from MuVisitor import MuVisitor
from MuParser import MuParser

from enum import Enum


class MuTypeError(Exception):
    pass


class BaseType(Enum):
    Float, Integer, Boolean, String, Nil = range(5)

    def printBaseType(self):
        print(self)


# Basic Type Checking for Mu programs.
class MyMuTypingVisitor(MuVisitor):

    def __init__(self):
        self._memorytypes = dict()  # id-> types

    def _raise(self, ctx, for_what, *types):
        raise MuTypeError(
            'Line {} col {}: invalid type for {}: {}'.format(
                ctx.start.line, ctx.start.column, for_what,
                ' and '.join(t.name.lower() for t in types)))

    # type declaration

    def visitVarDecl(self, ctx):
        vars_l = self.visit(ctx.id_l())
        tt = self.visit(ctx.typee())
        for name in vars_l:
            if name in self._memorytypes:
                raise MuTypeError("Variable {} already declared".format(name))
            self._memorytypes[name] = tt
        return

    def visitBasicType(self, ctx):
        if ctx.mytype.type == MuParser.INTTYPE:
            return BaseType.Integer
        elif ctx.mytype.type == MuParser.FLOATTYPE:
            return BaseType.Float
        elif ctx.mytype.type == MuParser.BOOLTYPE:
            return BaseType.Boolean
        elif ctx.mytype.type == MuParser.STRINGTYPE:
            return BaseType.String
        else:
            return BaseType.Nil

    def visitIdList(self, ctx):
        t = self.visit(ctx.id_l())
        t.append(ctx.ID().getText())
        return t

    def visitIdListBase(self, ctx):
        return [ctx.ID().getText()]

    # typing visitors for expressions, statements !

    # visitors for atoms --> value
    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitNumberAtom(self, ctx):
        s = ctx.getText()
        try:
            int(s)
            return BaseType.Integer
        except ValueError:
            try:
                float(s)
                return BaseType.Float
            except:
                raise MuTypeError("Invalid number atom")

    def visitBooleanAtom(self, ctx):
        return BaseType.Boolean

    def visitIdAtom(self, ctx):
        try:
            valtype = self._memorytypes[ctx.getText()]
            return valtype
        except KeyError:
            raise MuTypeError("Use of undefined id: {}".format(ctx.getText()))

    def visitStringAtom(self, ctx):
        return BaseType.String

    def visitNilAtom(self, ctx):
        return BaseType.Nil

    # now visit expr

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitOrExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))
        if (BaseType.Boolean == lvaltype) and (BaseType.Boolean == lvaltype):
            return BaseType.Boolean
        else:
            self._raise(ctx, 'boolean operands', lvaltype, rvaltype)

    def visitAndExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))
        if (BaseType.Boolean == lvaltype) and (BaseType.Boolean == lvaltype):
            return BaseType.Boolean
        else:
            self._raise(ctx, 'boolean operands', lvaltype, rvaltype)

    def visitEqualityExpr(self, ctx):
        return self.visitRelationalExpr(ctx)

    def visitRelationalExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))
        if {lvaltype, rvaltype} <= {BaseType.Integer, BaseType.Float, BaseType.Boolean}:
            return BaseType.Boolean
        else:
            self._raise(ctx, 'relational operands', lvaltype, rvaltype)

    def visitAdditiveExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))
        if ctx.myop.type == MuParser.MINUS and \
                BaseType.String in {lvaltype, rvaltype}:
            self._raise(ctx, 'minus operands', lvaltype, rvaltype)
        if lvaltype == rvaltype:
            return lvaltype
        elif {lvaltype, rvaltype} == {BaseType.Integer, BaseType.Float}:
            return BaseType.Float
        elif ((ctx.myop.type == MuParser.PLUS) and
              any(vt == BaseType.String
                  for vt in (rvaltype, lvaltype))):
            return BaseType.String
        else:
            self._raise(ctx, 'additive operands', lvaltype, rvaltype)

    def visitMultiplicativeExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))
        if ctx.myop.type in {MuParser.MULT, MuParser.MOD} and \
                lvaltype == BaseType.Integer and rvaltype == BaseType.Integer:
            return BaseType.Integer
        elif {lvaltype, rvaltype} <= {BaseType.Integer, BaseType.Float}:
            return BaseType.Float
        else:
            self._raise(ctx, 'multiplicative operands', lvaltype, rvaltype)

    def visitnotExpr(self, ctx):
        etype = self.visit(ctx.expr())
        if (etype != BaseType.Boolean):
            pass  # do exception handling
        else:
            return BaseType.Boolean

    def visitUnaryMinusExpr(self, ctx):
        etype = self.visit(ctx.expr())
        if (etype != BaseType.Integer and etype != BaseType.Float):
            self._raise(ctx, 'unary minus operand', etype)
        else:
            return etype

    def visitPowExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))
        if lvaltype == BaseType.Integer and rvaltype == BaseType.Integer:
            return BaseType.Integer
        elif lvaltype == BaseType.Float and rvaltype == BaseType.Integer:
            return BaseType.Float
        else:
            self._raise(ctx, 'power operands', lvaltype, rvaltype)

# statements
    def visitAssignStat(self, ctx):
        valtype = self.visit(ctx.expr())
        name = ctx.ID().getText()
        if name not in self._memorytypes:
            raise MuTypeError("Undefined variable "+name)
        if self._memorytypes[name] != valtype:
            raise MuTypeError("Mismatch types for "+name)

    def visitCondBlock(self, ctx):
        condtype = self.visit(ctx.expr())
        if condtype != BaseType.Boolean:
            self._raise(ctx, 'conditional block', condtype)
        self.visit(ctx.stat_block())

    def visitWhileStat(self, ctx):
        condtype = self.visit(ctx.expr())
        if condtype != BaseType.Boolean:
            self._raise(ctx, 'while condition', condtype)
        self.visit(ctx.stat_block())

    def visitIfStat(self, ctx):
        for cond in ctx.condition_block():
            self.visit(cond)
        if ctx.stat_block() is not None:
            self.visit(ctx.stat_block())
