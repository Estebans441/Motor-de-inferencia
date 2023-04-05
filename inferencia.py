from antlr4 import *
from gen.SentenciaLexer import SentenciaLexer
from gen.SentenciaParser import SentenciaParser
from gen.SentenciaVisitor import SentenciaVisitor, neg


# Clase que define una cláusula donde se tiene la serie de literales que la conforman y con que cláusulas se ha resuelto
# durante el proceso de resolution
class Clausula:
    def __init__(self, clausulas):
        self.clausulas = clausulas
        self.resueltoCon = []


# Agregar una sentencia a la lista de axiomas.
def agregar_axioma(axiomas, sentencia):
    axiomas.append(sentencia)


# Visitor con antlr que realiza una primera transformacion a fnc
def visitar(axioma):
    axioma_n = axioma.replace('∀', '/all').replace('∃', '/exists').replace('∧', '/and').replace('∨', '/or')
    visitor = SentenciaVisitor()
    fnc = visitor.visit(SentenciaParser(
        CommonTokenStream(
            SentenciaLexer(
                InputStream(
                    axioma_n)))).sentencia())
    return fnc, visitor.predicados


# Convertir la lista de axiomas a Forma Normal Conjuntiva.
# La variable predicados corresponde a los predicados univariable que se encuentran y una lista de constantes que
# pertenecen a estos. ej: Romano(Marco) -> {'Romano':['Marco']}
def forma_normal_conjuntiva(axiomas):
    # código para convertir a FNC
    axiomas_n = []
    predicados = {}
    for i in range(0, len(axiomas)):
        ap, predicados = visitar(axiomas[i])
        ap.replace("/n", str(i + 1))
        if ap[0] == "(":
            ap = ap[1:-1]
        axiomas_n.append(ap)
    return axiomas_n, predicados


# Verificar si hay cláusulas por resolver.
def hay_clausulas_por_resolver(clausulas):
    return any(len(c.clausulas) <= 1 and len(c.resueltoCon) < len(clausulas) - 1 for c in clausulas)


# Encontrar dos cláusulas por resolver.
def encontrar_clausulas_por_resolver(clausulas: [Clausula]):
    for i in range(0, len(clausulas)):
        for j in range(0, len(clausulas)):
            # Si las dos cláusulas no se han elegido para resolverse
            if (not clausulas[i].resueltoCon.__contains__(clausulas[j])) and (not i == j):
                clausulas[i].resueltoCon.append(clausulas[j])
                clausulas[j].resueltoCon.append(clausulas[i])
                for c1 in clausulas[i].clausulas:
                    for c2 in clausulas[j].clausulas:
                        # Si c1 tiene un literal que niega un literal de c2
                        if c1 == neg(c2):
                            return clausulas[i], clausulas[j]
    return Clausula([]), Clausula([])


# Generar el resultado de la resolución.
def resolver(clausula1, clausula2):
    # Se busca los dos literales que se niegan para crear el resultado en el que se eliminan
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
def es_clausula_nula(clausulas: [Clausula]):
    # Hay cláusulas nulas si hay dos clausulas de un literal que se niegan entre si
    for c1 in clausulas:
        if len(c1.clausulas) == 1:
            for c2 in clausulas:
                if len(c2.clausulas) == 1:
                    if c1.clausulas[0] == neg(c2.clausulas[0]):
                        return True
    return False


# Realizar la unificacion de variables
def unificacion(predicados, clausulas: [Clausula]):
    nuevas_clausulas = [c for c in clausulas]
    for c in clausulas:
        # Busqueda de variables dentro de las clausulas y determinacion de su posible reemplazo (unificacion)
        reemplazos = {}
        for c1 in c.clausulas:
            literal = c1.replace(")", "").replace("-", "").split("(")
            predicado = literal[0]
            variable = literal[1]
            if predicado in predicados and not variable[0].isupper():
                if variable not in reemplazos:
                    reemplazos[variable] = []
                for cons in predicados[predicado]:
                    reemplazos[variable].append(cons)

        # Reemplazo de la variable dentro de la clausula
        copias = []
        reemplazar(reemplazos, c.clausulas, copias)

        # Se agregan las clausulas con las variables unificadas si no se ha agregado ya
        for copia in copias:
            if copia != c.clausulas:
                nuevas_clausulas.append(Clausula(copia))
    return nuevas_clausulas


# Reemplaza una variable con sus posibles valores almacenados en el diccionario recursivamente
def reemplazar(diccionario: {}, original: [str], copias):
    if len(diccionario) == 0:
        if not any(c == original for c in copias):
            copias.append(original)
    for clave in diccionario:
        for reemplazo in diccionario[clave]:
            c_cpy = []
            for c in original:
                c_cpy.append(c.replace(clave, reemplazo))
            new_dic = diccionario.copy()
            new_dic.pop(clave)
            reemplazar(new_dic, c_cpy, copias)
        return


# Si se encuentra una clausula con solo un literal que define una nueva constante, se actualiza el diccionario con los
# predicados para volver a realizar la unificacion
def actualizar_pred(predicados, clausulas):
    for c in clausulas:
        if len(c.clausulas) == 1:
            c1 = c.clausulas[0]
            literal = c1.replace(")", "").replace("-", "").split("(")
            pred = literal[0]
            var = literal[1]
            if var[0].isupper() and len(var.split(",")) == 1:
                if not any(c == var for c in predicados[pred]):
                    predicados[pred].append(var)


# Elimina clausulas repetidas dentro de la lista de clausulas
def eliminar_repetidas(clausulas):
    for i, c1 in enumerate(clausulas):
        for j, c2 in enumerate(clausulas):
            if i != j and c1.clausulas == c2.clausulas:
                clausulas.pop(j)
    return clausulas


# Realizar la refutación de la sentencia.
def refutacion(axiomas, sentencia):
    agregar_axioma(axiomas, neg(sentencia))
    fnc, predicados = forma_normal_conjuntiva(axiomas)
    clausulas = [Clausula(a.split("∨")) for a in fnc]
    clausulas = unificacion(predicados, clausulas)
    while hay_clausulas_por_resolver(clausulas):
        clausula1, clausula2 = encontrar_clausulas_por_resolver(clausulas)
        resultado = resolver(clausula1, clausula2)
        if len(resultado.clausulas) and not any(c.clausulas == resultado.clausulas for c in clausulas):
            agregar_clausula(clausulas, resultado)
            actualizar_pred(predicados, clausulas)
            clausulas = eliminar_repetidas(unificacion(predicados, clausulas))
        if es_clausula_nula(clausulas):
            return True
    return False
