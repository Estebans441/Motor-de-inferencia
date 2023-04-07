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
    return fnc, visitor.predicados, visitor.relaciones


# Convertir la lista de axiomas a Forma Normal Conjuntiva.
# La variable predicados corresponde a los predicados univariable que se encuentran y una lista de constantes que
# pertenecen a estos. ej: Romano(Marco) -> {'Romano':['Marco']}
def forma_normal_conjuntiva(axiomas):
    # código para convertir a FNC
    axiomas_n = []
    predicados = {}
    relaciones = {}
    for i in range(0, len(axiomas)):
        ap, predicados, relaciones = visitar(axiomas[i])
        ap = ap.replace("#", str(i + 1))
        n_ap = ap.split("/bicond")
        for n in n_ap:
            if n[0] == "(":
                n = n[1:-1]
            axiomas_n.append(n)
    return axiomas_n, predicados, relaciones


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
def unificacion(predicados, relaciones, clausulas: [Clausula]):
    nuevas_clausulas = [c for c in clausulas]
    for c in clausulas:
        # Busqueda de variables dentro de las clausulas y determinacion de su posible reemplazo (unificacion)
        reemplazos = {}
        for c1 in c.clausulas:
            literal = c1.replace(")", "").replace("-", "").split("(")
            predicado = literal[0]
            variable = literal[1]
            # Predicados de una variable
            if predicado in predicados and not variable[0].isupper() and len(variable.split(",")) == 1:
                if variable not in reemplazos:
                    reemplazos[variable] = []
                for cons in predicados[predicado]:
                    if cons not in reemplazos[variable]:
                        reemplazos[variable].append(cons)
            # Predicados multivariable
            elif predicado in relaciones and len(variable.split(",")) == 2:
                x = variable.split(",")[0]
                y = variable.split(",")[1]
                if not x[0].isupper() and y[0].isupper():
                    if x not in reemplazos:
                        reemplazos[x] = []
                    for cons in relaciones[predicado]:
                        if y == cons[1]:
                            reemplazos[x].append(cons[0])
                if not y[0].isupper() and x[0].isupper():
                    if y not in reemplazos:
                        reemplazos[y] = []
                    for cons in relaciones[predicado]:
                        if x == cons[0]:
                            reemplazos[y].append(cons[1])
                if not x[0].isupper() and not y[0].isupper():
                    var = x+","+y
                    if var not in reemplazos:
                        reemplazos[var] = []
                    for cons in relaciones[predicado]:
                        ap = cons[0]+","+cons[1]
                        reemplazos[var].append(ap)

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
def actualizar_pred(predicados, relaciones, clausulas):
    for c in clausulas:
        if len(c.clausulas) == 1:
            c1 = c.clausulas[0]
            literal = c1.replace(")", "").replace("-", "").split("(")
            pred = literal[0]
            var = literal[1]
            splt = var.split(",")
            if var[0].isupper() and len(splt) == 1:
                if not any(c == var for c in predicados[pred]):
                    predicados[pred].append(var)
            """elif len(splt) == 2:
                x = splt[0]
                y = splt[1]
                if x[0].isupper() and y[0].isupper():
                    v =(x, y)
                    if not any(c == v for c in relaciones[pred]):
                        relaciones[pred].append(v)"""



# Elimina clausulas repetidas dentro de la lista de clausulas
def eliminar_repetidas(clausulas):
    for i, c1 in enumerate(clausulas):
        for j, c2 in enumerate(clausulas):
            if i != j and c1.clausulas == c2.clausulas:
                clausulas.pop(j)
    return clausulas


def distributiva(clausulas):
    for i, c in enumerate(clausulas):
        for c1 in c.clausulas:
            c2 = c1
            if c2[0] == "(":
                c2 = c2[1:-1]
            splt = c2.split("∧")
            if len(splt) > 1:
                for s in splt:
                    nueva = [cl for cl in c.clausulas if cl != c1]
                    nueva.append(s)
                    clausulas.append(Clausula(nueva))
                clausulas.pop(i)


# Realizar la refutación de la sentencia.
def refutacion(axiomas, sentencia):
    agregar_axioma(axiomas, neg(sentencia))
    fnc, predicados, relaciones = forma_normal_conjuntiva(axiomas)
    clausulas = [Clausula(a.split("∨")) for a in fnc]
    distributiva(clausulas)
    clausulas = unificacion(predicados, relaciones, clausulas)
    while hay_clausulas_por_resolver(clausulas):
        clausula1, clausula2 = encontrar_clausulas_por_resolver(clausulas)
        resultado = resolver(clausula1, clausula2)
        if len(resultado.clausulas) and not any(c.clausulas == resultado.clausulas for c in clausulas):
            agregar_clausula(clausulas, resultado)
            actualizar_pred(predicados, relaciones, clausulas)
            clausulas = eliminar_repetidas(unificacion(predicados, relaciones, clausulas))
        if es_clausula_nula(clausulas):
            print(relaciones)
            print(predicados)
            for c in clausulas:
                print(c.clausulas)
            return True
    for c in clausulas:
        print(c.clausulas)
    return False
