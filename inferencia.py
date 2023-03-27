from antlr4 import *
from gen.SentenciaLexer import SentenciaLexer
from gen.SentenciaParser import SentenciaParser
from gen.SentenciaVisitor import SentenciaVisitor, neg


# Agregar una sentencia a la lista de axiomas.
def agregar_axioma(axiomas, sentencia):
    axiomas.append(sentencia)


# Visitor con antlr
def visitar(axioma):
    axioma_n = axioma.replace('∀', '/all').replace('∃', '/exists').replace('∧', '/and').replace('∨', '/or')
    return SentenciaVisitor().visit(SentenciaParser(
        CommonTokenStream(
            SentenciaLexer(
                InputStream(
                    axioma_n)))).sentencia())


# Convertir la lista de axiomas a Forma Normal Conjuntiva.
def forma_normal_conjuntiva(axiomas):
    # código para convertir a FNC
    axiomas_n = []
    for i in range(0, len(axiomas)):
        ap = visitar(axiomas[i]).replace("/n", str(i + 1))
        axiomas_n.append(ap)
    return axiomas_n


# Verificar si hay cláusulas por resolver.
def hay_clausulas_por_resolver(clausulas):
    return any(len(c) > 1 for c in clausulas)


# Encontrar dos cláusulas por resolver.
def encontrar_clausulas_por_resolver(clausulas):
    # código para encontrar cláusulas por resolver
    clausula1, clausula2 = 0
    return clausula1, clausula2


# Generar el resultado de la resolución.
def resolver(clausula1, clausula2):
    # código para aplicar resolución
    resultado = 0
    return resultado


# Agregar una nueva cláusula a la lista.
def agregar_clausula(clausulas, nueva_clausula):
    clausulas.append(nueva_clausula)


# Verificar si hay una cláusula nula en la lista.
def es_clausula_nula(clausulas):
    # código para verificar si hay cláusula nula
    hay_nula = 0
    return hay_nula


# Realizar la refutación de la sentencia.
def refutacion(axiomas, sentencia):
    negacion = neg(sentencia)
    agregar_axioma(axiomas, negacion)
    fnc = forma_normal_conjuntiva(axiomas)
    clausulas = fnc
    while hay_clausulas_por_resolver(clausulas):
        clausula1, clausula2 = encontrar_clausulas_por_resolver(clausulas)
        resultado = resolver(clausula1, clausula2)
        if resultado:
            agregar_clausula(clausulas, resultado)
        if es_clausula_nula(clausulas):
            return True
    return False
