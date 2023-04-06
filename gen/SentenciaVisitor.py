# Generated from C:/Users/esteb/Documents/Trabajos U/Intro IA/Motor-de-inferencia/gen\Sentencia.g4 by ANTLR 4.11.1
from antlr4 import *

from .SentenciaLexer import SentenciaLexer

if __name__ is not None and "." in __name__:
    from .SentenciaParser import SentenciaParser
else:
    from SentenciaParser import SentenciaParser


def neg(sentencia):
    a = sentencia.replace(" ", "").split("∧")
    s = ""
    for i in range(0, len(a)):
        if i < len(a) - 1:
            a[i] = a[i] + "*"
        b = a[i].split("∨")
        for j in range(0, len(b)):
            b[j] = "-" + b[j]
            b[j] = b[j].replace("-(", "(-")
            if j < len(b) - 1:
                b[j] = b[j] + "∧"
            s = s + b[j].replace("*", "∨")
    s = s.replace("--", "")
    return s


# This class defines a complete generic visitor for a parse tree produced by SentenciaParser.

class SentenciaVisitor(ParseTreeVisitor):
    predicados = {}
    relaciones = {}

    # Visit a parse tree produced by SentenciaParser#Forall.
    def visitForall(self, ctx: SentenciaParser.ForallContext):
        return self.visit(ctx.sentencia())

    # Visit a parse tree produced by SentenciaParser#Exists.
    def visitExists(self, ctx: SentenciaParser.ExistsContext):
        var: str = str(ctx.ID())
        r: str = self.visit(ctx.sentencia()).replace("(" + var, "(" + var + "#")
        return r

    # Visit a parse tree produced by SentenciaParser#Impl.
    def visitImpl(self, ctx: SentenciaParser.ImplContext):
        a = self.visit(ctx.exp(0))
        b = self.visit(ctx.exp(1))
        return "(" + neg(a) + "∨" + b + ")"

    # Visit a parse tree produced by SentenciaParser#Bicond.
    def visitBicond(self, ctx: SentenciaParser.BicondContext):
        a = self.visit(ctx.exp(0))
        b = self.visit(ctx.exp(1))
        return "(" + neg(a) + "∨" + b + ")/bicond(" + neg(b) + "∨" + a + ")"

    # Visit a parse tree produced by SentenciaParser#Expr.
    def visitExpr(self, ctx: SentenciaParser.ExprContext):
        return self.visit(ctx.exp())

    # Visit a parse tree produced by SentenciaParser#Neg.
    def visitNeg(self, ctx: SentenciaParser.NegContext):
        return neg(self.visit(ctx.exp()))

    # Visit a parse tree produced by SentenciaParser#Or.
    def visitOr(self, ctx: SentenciaParser.OrContext):
        a = self.visit(ctx.exp(0)) + "∨" + self.visit(ctx.exp(1))
        return a

    # Visit a parse tree produced by SentenciaParser#And.
    def visitAnd(self, ctx: SentenciaParser.AndContext):
        a = self.visit(ctx.exp(0)) + "∧" + self.visit(ctx.exp(1))
        return a

    # Visit a parse tree produced by SentenciaParser#Pred.
    def visitPred(self, ctx: SentenciaParser.PredContext):
        return self.visit(ctx.predicado())

    # Visit a parse tree produced by SentenciaParser#Paren.
    def visitParen(self, ctx: SentenciaParser.ParenContext):
        return self.visit(ctx.exp())

    # Visit a parse tree produced by SentenciaParser#Uni.
    def visitUni(self, ctx: SentenciaParser.UniContext):
        clave = ctx.PRED(0).__str__()
        if clave not in self.predicados:
            self.predicados[clave] = []
        if ctx.ID() is None:
            if not any(c == ctx.PRED(1).__str__() for c in self.predicados[clave]):
                self.predicados[clave].append(ctx.PRED(1).__str__())
        return ctx.getText()

    # Visit a parse tree produced by SentenciaParser#IDID.
    def visitIDID(self, ctx: SentenciaParser.IDIDContext):
        clave = ctx.PRED().__str__()
        if clave not in self.predicados:
            self.predicados[clave] = []
        return ctx.getText()

    # Visit a parse tree produced by SentenciaParser#IDP.
    def visitIDP(self, ctx: SentenciaParser.IDPContext):
        clave = ctx.PRED(0).__str__()
        if clave not in self.relaciones:
            self.relaciones[clave] = []
        return ctx.getText()

    # Visit a parse tree produced by SentenciaParser#PID.
    def visitPID(self, ctx: SentenciaParser.PIDContext):
        clave = ctx.PRED(0).__str__()
        if clave not in self.relaciones:
            self.relaciones[clave] = []
        return ctx.getText()

    # Visit a parse tree produced by SentenciaParser#PP.
    def visitPP(self, ctx: SentenciaParser.PPContext):
        clave = ctx.PRED(0).__str__()
        if clave not in self.relaciones:
            self.relaciones[clave] = []
        v1 = ctx.PRED(1).__str__()
        v2 = ctx.PRED(2).__str__()
        v = (v1, v2)
        if v not in self.relaciones[clave]:
            self.relaciones[clave].append(v)
        return ctx.getText()


del SentenciaParser
