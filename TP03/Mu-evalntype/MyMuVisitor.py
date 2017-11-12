from MuVisitor import MuVisitor
from MuParser import MuParser

# Visitor to *interpret* Mu files order MyMuTypingVisitor (validator) -> MyMuVisitor (code execution)


class MuRuntimeError(Exception):
    pass


class MuSyntaxError(Exception):
    pass


class MyMuVisitor(MuVisitor):

    def __init__(self):
        self._memory = dict()  # dict = table, store all variable ids and values.

    # visitors for variable declarations

    def visitVarDecl(self, ctx):
        # Initialise all variables in self._memory (myVariable = None)
        vars_l = self.visit(ctx.id_l())
        for name in vars_l:
            self._memory[name] = None


    def visitIdList(self, ctx):
        t = self.visit(ctx.id_l())
        t.append(ctx.ID().getText())
        return t

    def visitIdListBase(self, ctx):
        return [ctx.ID().getText()]

    # visitors for atoms --> value
    # this code is given to students except for idatoms !

    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitNumberAtom(self, ctx):
        s = ctx.getText()
        try:
            return int(s)
        except ValueError:
            return float(s)

    def visitBooleanAtom(self, ctx):
        return ctx.getText() == "true"

    def visitIdAtom(self, ctx):
        return self._memory[ctx.ID().getText()]

    def visitStringAtom(self, ctx):
        return ctx.getText()[1:-1]

    def visitNilAtom(self, ctx):
        return ctx.getText()

    # visit expressions
    # this code is given to students
    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitOrExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval | rval

    def visitAndExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval & rval

    def visitEqualityExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        # be careful for float equality
        if ctx.myop.type == MuParser.EQ:
            return lval == rval
        else:
            return lval != rval

    def visitRelationalExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MuParser.LT:
            return lval < rval
        elif ctx.myop.type == MuParser.LTEQ:
            return lval <= rval
        elif ctx.myop.type == MuParser.GT:
            return lval > rval
        elif ctx.myop.type == MuParser.GTEQ:
            return lval >= rval
        else:
            raise MuSyntaxError("Unknown comparison operator '%s'" % ctx.myop)

    def visitAdditiveExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MuParser.PLUS:
            if any(isinstance(x, str) for x in (lval, rval)):
                return '{}{}'.format(lval, rval)
            else:
                return lval + rval
        elif ctx.myop.type == MuParser.MINUS:
            return lval - rval
        else:
            raise MuSyntaxError("Unknown additive operator '%s'" % ctx.myop)

    def visitMultiplicativeExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        if ctx.myop.type == MuParser.MULT:
            return lval * rval
        elif ctx.myop.type == MuParser.DIV:
            return lval / rval
        elif ctx.myop.type == MuParser.MOD:
            return lval % rval
        else:
            raise MuSyntaxError("Unknown multiplication operator '%s'"
                                % ctx.myop)

    def visitNotExpr(self, ctx):
        return not self.visit(ctx.expr())

    def visitUnaryMinusExpr(self, ctx):
        return -self.visit(ctx.expr())

    def visitPowExpr(self, ctx):
        lval = self.visit(ctx.expr(0))
        rval = self.visit(ctx.expr(1))
        return lval ** rval

    # visit statements

    def visitLogStat(self, ctx):
        val = self.visit(ctx.expr())
        if val != None:
            if isinstance(val, bool):
                val = '1' if val else '0'
            if isinstance(val, float):
                val = "%.2f" % val
            print(val)
        else:
            print(ctx.expr().getText(), "has no value yet!")
            raise MuSyntaxError()

    def visitAssignStat(self, ctx):
        self._memory[ctx.ID().getText()] = self.visit(ctx.expr())

    def visitCondBlock(self, ctx):
        # expr bool, then stat-block
        # exec the stat-block and return true if the cond evaluates to true
        # else return False.
        val = self.visit(ctx.expr())
        if val == 1: #true
            self.visit(ctx.stat_block())
        return val

    '''
    condition = if, else if, else
    if cond == 1
        return true
    else cond
    '''
    def visitIfStat(self, ctx):
        for condition in ctx.condition_block():
            val = self.visit(condition)
            if val == 1:
                break;
        if val == 0:
            self.visit(ctx.stat_block())


    def visitWhileStat(self, ctx):
        while self.visit(ctx.expr()) == 1:
            self.visit(ctx.stat_block())

        
