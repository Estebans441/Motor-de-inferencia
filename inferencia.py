from antlr4 import *
from gen.SentenciaLexer import SentenciaLexer
from gen.SentenciaParser import SentenciaParser
from gen.SentenciaVisitor import SentenciaVisitor, neg

# Clase que define una clausula donde se tiene la serie de literales que la conforman y con que clausulas se ha resuelto
# durante el proceso de resolucion
class Clausula:
    def __init__(self, clausulas):
        self.clausulas = clausulas
        self.resueltoCon = []


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
        if ap[0] == "(":
            ap = ap[1:-1]
        axiomas_n.append(ap)
    return axiomas_n


# Verificar si hay cláusulas por resolver.
def hay_clausulas_por_resolver(clausulas):
    return any(len(c.clausulas) <= 1 and len(c.resueltoCon) < len(clausulas)-1 for c in clausulas)


# Encontrar dos cláusulas por resolver.
def encontrar_clausulas_por_resolver(clausulas:[Clausula]):
    for i in range(0, len(clausulas)):
        for j in range(0, len(clausulas)):
            if (not clausulas[i].resueltoCon.__contains__(clausulas[j])) and (not i == j):
                clausulas[i].resueltoCon.append(clausulas[j])
                clausulas[j].resueltoCon.append(clausulas[i])
                for c1 in clausulas[i].clausulas:
                    for c2 in clausulas[j].clausulas:
                        if c1 == neg(c2):
                            return clausulas[i], clausulas[j]
    return Clausula([]), Clausula([])


# Generar el resultado de la resolución.
def resolver(clausula1, clausula2):
    # código para aplicar resolución
    c1_n, c2_n = [], []
    for c1 in clausula1.clausulas:
        for c2 in clausula2.clausulas:
            if c1 == neg(c2):
                c1_n = [c for c in clausula1.clausulas if c != c1]
                c2_n = [c for c in clausula2.clausulas if c != c2]

    resultado = Clausula(c1_n + c2_n)
    return resultado


# Agregar una nueva cláusula a la lista.
def agregar_clausula(clausulas, nueva_clausula):
    clausulas.append(nueva_clausula)


# Verificar si hay una cláusula nula en la lista.
def es_clausula_nula(clausulas:[Clausula]):
    # código para verificar si hay cláusula nula
    for c1 in clausulas:
        if len(c1.clausulas) == 1:
            for c2 in clausulas:
                if len(c2.clausulas) == 1:
                    if c1.clausulas[0] == neg(c2.clausulas[0]):
                        return True
    return False


# Realizar la refutación de la sentencia.
def refutacion(axiomas, sentencia):
    negacion = neg(sentencia)
    agregar_axioma(axiomas, negacion)
    fnc = forma_normal_conjuntiva(axiomas)
    clausulas = [Clausula(a.split("∨")) for a in fnc]
    while hay_clausulas_por_resolver(clausulas):
        clausula1, clausula2 = encontrar_clausulas_por_resolver(clausulas)
        resultado = resolver(clausula1, clausula2)
        if len(resultado.clausulas) and not any(c.clausulas == resultado.clausulas for c in clausulas):
            agregar_clausula(clausulas, resultado)
        if es_clausula_nula(clausulas):
            return True
    return False
