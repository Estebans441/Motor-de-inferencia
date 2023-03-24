# Generated from C:/Users/esteb/Documents/Trabajos U/Intro IA/Proyecto2/gen\Sentencia.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,55,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,
        0,14,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,24,8,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,38,8,1,10,1,12,1,41,9,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,53,8,2,1,2,0,1,2,3,0,
        2,4,0,1,1,0,11,12,60,0,13,1,0,0,0,2,23,1,0,0,0,4,52,1,0,0,0,6,7,
        5,4,0,0,7,8,5,11,0,0,8,14,3,0,0,0,9,10,5,5,0,0,10,11,5,11,0,0,11,
        14,3,0,0,0,12,14,3,2,1,0,13,6,1,0,0,0,13,9,1,0,0,0,13,12,1,0,0,0,
        14,1,1,0,0,0,15,16,6,1,-1,0,16,17,5,1,0,0,17,18,3,2,1,0,18,19,5,
        2,0,0,19,24,1,0,0,0,20,21,5,10,0,0,21,24,3,2,1,2,22,24,3,4,2,0,23,
        15,1,0,0,0,23,20,1,0,0,0,23,22,1,0,0,0,24,39,1,0,0,0,25,26,10,6,
        0,0,26,27,5,7,0,0,27,38,3,2,1,7,28,29,10,5,0,0,29,30,5,6,0,0,30,
        38,3,2,1,6,31,32,10,4,0,0,32,33,5,9,0,0,33,38,3,2,1,5,34,35,10,3,
        0,0,35,36,5,8,0,0,36,38,3,2,1,4,37,25,1,0,0,0,37,28,1,0,0,0,37,31,
        1,0,0,0,37,34,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,
        40,3,1,0,0,0,41,39,1,0,0,0,42,43,5,12,0,0,43,44,5,1,0,0,44,45,7,
        0,0,0,45,53,5,2,0,0,46,47,5,12,0,0,47,48,5,1,0,0,48,49,7,0,0,0,49,
        50,5,3,0,0,50,51,7,0,0,0,51,53,5,2,0,0,52,42,1,0,0,0,52,46,1,0,0,
        0,53,5,1,0,0,0,5,13,23,37,39,52
    ]

class SentenciaParser ( Parser ):

    grammarFileName = "Sentencia.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "<INVALID>", "<INVALID>", 
                     "'=>'", "'<=>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ALL", "EXISTS", "IMPLY", "BICOND", "OR", "AND", "NOT", 
                      "ID", "PRED", "WS" ]

    RULE_sentencia = 0
    RULE_exp = 1
    RULE_predicado = 2

    ruleNames =  [ "sentencia", "exp", "predicado" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ALL=4
    EXISTS=5
    IMPLY=6
    BICOND=7
    OR=8
    AND=9
    NOT=10
    ID=11
    PRED=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentenciaParser.RULE_sentencia

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprContext(SentenciaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.SentenciaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(SentenciaParser.ExpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExistsContext(SentenciaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.SentenciaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def EXISTS(self):
            return self.getToken(SentenciaParser.EXISTS, 0)
        def ID(self):
            return self.getToken(SentenciaParser.ID, 0)
        def sentencia(self):
            return self.getTypedRuleContext(SentenciaParser.SentenciaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExists" ):
                return visitor.visitExists(self)
            else:
                return visitor.visitChildren(self)


    class ForallContext(SentenciaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.SentenciaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ALL(self):
            return self.getToken(SentenciaParser.ALL, 0)
        def ID(self):
            return self.getToken(SentenciaParser.ID, 0)
        def sentencia(self):
            return self.getTypedRuleContext(SentenciaParser.SentenciaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForall" ):
                return visitor.visitForall(self)
            else:
                return visitor.visitChildren(self)



    def sentencia(self):

        localctx = SentenciaParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sentencia)
        try:
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = SentenciaParser.ForallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 6
                self.match(SentenciaParser.ALL)
                self.state = 7
                self.match(SentenciaParser.ID)
                self.state = 8
                self.sentencia()
                pass
            elif token in [5]:
                localctx = SentenciaParser.ExistsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 9
                self.match(SentenciaParser.EXISTS)
                self.state = 10
                self.match(SentenciaParser.ID)
                self.state = 11
                self.sentencia()
                pass
            elif token in [1, 10, 12]:
                localctx = SentenciaParser.ExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 12
                self.exp(0)
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


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentenciaParser.RULE_exp

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NegContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(SentenciaParser.NOT, 0)
        def exp(self):
            return self.getTypedRuleContext(SentenciaParser.ExpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNeg" ):
                return visitor.visitNeg(self)
            else:
                return visitor.visitChildren(self)


    class CondContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SentenciaParser.ExpContext)
            else:
                return self.getTypedRuleContext(SentenciaParser.ExpContext,i)

        def IMPLY(self):
            return self.getToken(SentenciaParser.IMPLY, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCond" ):
                return visitor.visitCond(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SentenciaParser.ExpContext)
            else:
                return self.getTypedRuleContext(SentenciaParser.ExpContext,i)

        def OR(self):
            return self.getToken(SentenciaParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class BicondicionalContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SentenciaParser.ExpContext)
            else:
                return self.getTypedRuleContext(SentenciaParser.ExpContext,i)

        def BICOND(self):
            return self.getToken(SentenciaParser.BICOND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBicondicional" ):
                return visitor.visitBicondicional(self)
            else:
                return visitor.visitChildren(self)


    class AndContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SentenciaParser.ExpContext)
            else:
                return self.getTypedRuleContext(SentenciaParser.ExpContext,i)

        def AND(self):
            return self.getToken(SentenciaParser.AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnd" ):
                return visitor.visitAnd(self)
            else:
                return visitor.visitChildren(self)


    class PredContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def predicado(self):
            return self.getTypedRuleContext(SentenciaParser.PredicadoContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPred" ):
                return visitor.visitPred(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExpContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.ExpContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(SentenciaParser.ExpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)



    def exp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SentenciaParser.ExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_exp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = SentenciaParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 16
                self.match(SentenciaParser.T__0)
                self.state = 17
                self.exp(0)
                self.state = 18
                self.match(SentenciaParser.T__1)
                pass
            elif token in [10]:
                localctx = SentenciaParser.NegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(SentenciaParser.NOT)
                self.state = 21
                self.exp(2)
                pass
            elif token in [12]:
                localctx = SentenciaParser.PredContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.predicado()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SentenciaParser.BicondicionalContext(self, SentenciaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 25
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 26
                        self.match(SentenciaParser.BICOND)
                        self.state = 27
                        self.exp(7)
                        pass

                    elif la_ == 2:
                        localctx = SentenciaParser.CondContext(self, SentenciaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 28
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 29
                        self.match(SentenciaParser.IMPLY)
                        self.state = 30
                        self.exp(6)
                        pass

                    elif la_ == 3:
                        localctx = SentenciaParser.AndContext(self, SentenciaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 31
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 32
                        self.match(SentenciaParser.AND)
                        self.state = 33
                        self.exp(5)
                        pass

                    elif la_ == 4:
                        localctx = SentenciaParser.OrContext(self, SentenciaParser.ExpContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp)
                        self.state = 34
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 35
                        self.match(SentenciaParser.OR)
                        self.state = 36
                        self.exp(4)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PredicadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SentenciaParser.RULE_predicado

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PredmultContext(PredicadoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.PredicadoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRED(self, i:int=None):
            if i is None:
                return self.getTokens(SentenciaParser.PRED)
            else:
                return self.getToken(SentenciaParser.PRED, i)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SentenciaParser.ID)
            else:
                return self.getToken(SentenciaParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredmult" ):
                return visitor.visitPredmult(self)
            else:
                return visitor.visitChildren(self)


    class PreduniContext(PredicadoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SentenciaParser.PredicadoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRED(self, i:int=None):
            if i is None:
                return self.getTokens(SentenciaParser.PRED)
            else:
                return self.getToken(SentenciaParser.PRED, i)
        def ID(self):
            return self.getToken(SentenciaParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPreduni" ):
                return visitor.visitPreduni(self)
            else:
                return visitor.visitChildren(self)



    def predicado(self):

        localctx = SentenciaParser.PredicadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_predicado)
        self._la = 0 # Token type
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = SentenciaParser.PreduniContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(SentenciaParser.PRED)
                self.state = 43
                self.match(SentenciaParser.T__0)
                self.state = 44
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 45
                self.match(SentenciaParser.T__1)
                pass

            elif la_ == 2:
                localctx = SentenciaParser.PredmultContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(SentenciaParser.PRED)
                self.state = 47
                self.match(SentenciaParser.T__0)
                self.state = 48
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 49
                self.match(SentenciaParser.T__2)
                self.state = 50
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 51
                self.match(SentenciaParser.T__1)
                pass


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
        self._predicates[1] = self.exp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_sempred(self, localctx:ExpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




