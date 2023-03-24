# Generated from C:/Users/esteb/Documents/Trabajos U/Intro IA/Proyecto2/gen\Sentencia.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SentenciaParser import SentenciaParser
else:
    from SentenciaParser import SentenciaParser

# This class defines a complete generic visitor for a parse tree produced by SentenciaParser.

class SentenciaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SentenciaParser#Forall.
    def visitForall(self, ctx:SentenciaParser.ForallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#Exists.
    def visitExists(self, ctx:SentenciaParser.ExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#Expr.
    def visitExpr(self, ctx:SentenciaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#Neg.
    def visitNeg(self, ctx:SentenciaParser.NegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#Cond.
    def visitCond(self, ctx:SentenciaParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#Or.
    def visitOr(self, ctx:SentenciaParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#Bicondicional.
    def visitBicondicional(self, ctx:SentenciaParser.BicondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#And.
    def visitAnd(self, ctx:SentenciaParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#Pred.
    def visitPred(self, ctx:SentenciaParser.PredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#Paren.
    def visitParen(self, ctx:SentenciaParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#Preduni.
    def visitPreduni(self, ctx:SentenciaParser.PreduniContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SentenciaParser#Predmult.
    def visitPredmult(self, ctx:SentenciaParser.PredmultContext):
        return self.visitChildren(ctx)



del SentenciaParser