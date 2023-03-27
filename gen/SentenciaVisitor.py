# Generated from C:/Users/esteb/Documents/Trabajos U/Intro IA/Motor-de-inferencia/gen\Sentencia.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .SentenciaParser import SentenciaParser
else:
    from SentenciaParser import SentenciaParser


def neg(sentencia):
    a = sentencia.replace(" ", "").split("∧")
    s = ""
    for i in range(0, len(a)):
        if i < len(a) - 1:
            a[i] = a[i] + " * "
        b = a[i].split("∨")
        for j in range(0, len(b)):
            b[j] = "-" + b[j]
            b[j] = b[j].replace("-(", "(-")
            if j < len(b) - 1:
                b[j] = b[j] + " ∧ "
            s = s + b[j].replace("*", "∨")
    s = s.replace("--", "")
    return s


# This class defines a complete generic visitor for a parse tree produced by SentenciaParser.

class SentenciaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SentenciaParser#Forall.
    def visitForall(self, ctx: SentenciaParser.ForallContext):
        return self.visit(ctx.sentencia())

    # Visit a parse tree produced by SentenciaParser#Exists.
    def visitExists(self, ctx: SentenciaParser.ExistsContext):
        var: str = str(ctx.ID())
        r: str = self.visit(ctx.sentencia()).replace("(" + var, "(" + var + "/n")
        return r

    # Visit a parse tree produced by SentenciaParser#Impl.
    def visitImpl(self, ctx: SentenciaParser.ImplContext):
        a = self.visit(ctx.exp(0))
        b = self.visit(ctx.exp(1))
        return "(" + neg(a) + " ∨ " + b + ")"

    # Visit a parse tree produced by SentenciaParser#Bicond.
    def visitBicond(self, ctx: SentenciaParser.BicondContext):
        a = self.visit(ctx.exp(0))
        b = self.visit(ctx.exp(1))
        return "(" + neg(a) + " ∨ " + b + ") ∧ (" + neg(b) + " ∨ " + a + ")"

    # Visit a parse tree produced by SentenciaParser#Expr.
    def visitExpr(self, ctx: SentenciaParser.ExprContext):
        return self.visit(ctx.exp())

    # Visit a parse tree produced by SentenciaParser#Neg.
    def visitNeg(self, ctx: SentenciaParser.NegContext):
        return neg(self.visit(ctx.exp()))

    # Visit a parse tree produced by SentenciaParser#Or.
    def visitOr(self, ctx: SentenciaParser.OrContext):
        a = self.visit(ctx.exp(0)) + " ∨ " + self.visit(ctx.exp(1))
        return a

    # Visit a parse tree produced by SentenciaParser#And.
    def visitAnd(self, ctx: SentenciaParser.AndContext):
        a = self.visit(ctx.exp(0)) + " ∧ " + self.visit(ctx.exp(1))
        return a

    # Visit a parse tree produced by SentenciaParser#Pred.
    def visitPred(self, ctx: SentenciaParser.PredContext):
        return ctx.getText()

    # Visit a parse tree produced by SentenciaParser#Paren.
    def visitParen(self, ctx: SentenciaParser.ParenContext):
        return self.visit(ctx.exp())


del SentenciaParser
