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
    return fnc


# Convertir la lista de axiomas a Forma Normal Conjuntiva.
# La variable predicados corresponde a los predicados univariable que se encuentran y una lista de constantes que
# pertenecen a estos. ej: Romano(Marco) -> {'Romano':['Marco']}
def forma_normal_conjuntiva(axiomas):
    # código para convertir a FNC
    axiomas_n = []
    for i in range(0, len(axiomas)):
        ap = visitar(axiomas[i])
        ap = ap.replace("#", str(i + 1))
        n_ap = ap.split("/bicond")
        for n in n_ap:
            if n[0] == "(":
                n = n[1:-1]
            axiomas_n.append(n)
    return axiomas_n


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
                        if c1.split("(", 1)[0] == neg(c2.split("(", 1)[0]):
                            return clausulas[i], clausulas[j]
    return Clausula([]), Clausula([])


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


# Generar el resultado de la resolución.
def resolver(clausula1, clausula2):
    # Se busca los dos literales que se niegan para crear el resultado en el que se eliminan
    unificados = unificacion(clausula1.clausulas, clausula2.clausulas)
    resultado = []
    for u in unificados:
        resuelto = False
        n_u = []
        for c1 in u:
            esta = False
            for c2 in u:
                if c1 == neg(c2):
                    esta = True
                    resuelto = True
            if not esta:
                n_u.append(c1)
        if resuelto:
            resultado.append(Clausula([n for n in n_u]))
    return resultado


def unificacion(clausula1: [str], clausula2: [str]):
    reemplazos = {}
    copias = []
    for c1 in clausula1:
        for c2 in clausula2:
            splt1 = c1.replace(")", "").replace("-", "").split("(", 1)
            splt2 = c2.replace(")", "").replace("-", "").split("(", 1)
            pred1 = splt1[0]
            pred2 = splt2[0]
            if pred1 == pred2:
                if len(splt1[1].split(",")) == 1:
                    v1 = splt1[1]
                    v2 = splt2[1]
                    if v1[0].isupper() and not v2[0].isupper():
                        if v2 not in reemplazos:
                            reemplazos[v2] = []
                        reemplazos[v2].append(v1)
                    elif v2[0].isupper() and not v1[0].isupper():
                        if v1 not in reemplazos:
                            reemplazos[v1] = []
                        reemplazos[v1].append(v2)
                else:
                    v11 = splt1[1].split(",")[0]
                    v12 = splt1[1].split(",")[1]
                    v21 = splt2[1].split(",")[0]
                    v22 = splt2[1].split(",")[1]
                    if v11[0].isupper() and v12[0].isupper() and (not v21[0].isupper()) and (not v22[0].isupper()):
                        copias.append([c.replace(v21, v11).replace(v22, v12) for c in clausula1] +
                                      [c.replace(v21, v11).replace(v22, v12) for c in clausula2])
                    elif (not v11[0].isupper()) and (not v12[0].isupper()) and v21[0].isupper() and v22[0].isupper():
                        copias.append([c.replace(v11, v21).replace(v12, v22) for c in clausula1] +
                                      [c.replace(v11, v21).replace(v22, v22) for c in clausula2])
                    elif v11[0].isupper() and (not v21[0].isupper()) and (not v22[0].isupper()):
                        if v21 not in reemplazos:
                            reemplazos[v21] = []
                        reemplazos[v21].append(v11)
                    elif (not v11[0].isupper()) and (not v12[0].isupper()) and v21[0].isupper():
                        if v11 not in reemplazos:
                            reemplazos[v11] = []
                        reemplazos[v11].append(v21)
                    elif v12[0].isupper() and (not v21[0].isupper()) and (not v22[0].isupper):
                        if v22 not in reemplazos:
                            reemplazos[v22] = []
                        reemplazos[v22].append(v12)
                    elif (not v11[0].isupper()) and (not v12[0].isupper()) and v22[0].isupper():
                        if v12 not in reemplazos:
                            reemplazos[v12] = []
                        reemplazos[v12].append(v22)

    # Reemplazo de la variable dentro de la clausula
    # print("Para " + str(clausula1) + " " + str(clausula2))
    # print(reemplazos)
    reemplazar(reemplazos, clausula1 + clausula2, copias)
    return copias


def refutacion(axiomas, sentencia):
    agregar_axioma(axiomas, neg(sentencia))
    fnc = forma_normal_conjuntiva(axiomas)
    clausulas = [Clausula(a.split("∨")) for a in fnc]
    distributiva(clausulas)
    while hay_clausulas_por_resolver(clausulas):
        clausula1, clausula2 = encontrar_clausulas_por_resolver(clausulas)
        resultados = resolver(clausula1, clausula2)
        for resultado in resultados:
            if len(resultado.clausulas) > 0 and not any(c.clausulas == resultado.clausulas for c in clausulas):
                agregar_clausula(clausulas, resultado)
                clausulas = sorted(clausulas, key=lambda c: len(c.clausulas))
        if es_clausula_nula(clausulas):
            return True
    return False
