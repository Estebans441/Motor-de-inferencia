from inferencia import *

no_unificacion_sentencia = "Odia(x, y)"
no_unificacion = [
    "Hombre(x)",
    "Pompeyano(x)",
    "∀x Pompeyano(x) => Romano(x)",
    "Gobernante(y)",
    "∀x Romano(x) => (Leal(x, y) ∨ Odia(x, y))",
    "∀x ∀y (Hombre(x) ∧ Gobernante(y) ∧ IntentaAsesinar(x, y)) => -Leal(x, y)",
    "IntentaAsesinar(x, y)"
]

marco_cesar_sentencia = "Odia(Marco, Cesar)"
marco_cesar = [
    "Hombre(Marco) ∧ Pompeyano(Marco) ∧ Hombre(Antonio) ∧ Ateneo(Antonio)",
    "IntentaAsesinar(Antonio,Cesar)",
    "∀x (Pompeyano(x) ∨ Ateneo(x)) => Romano(x)",
    "Gobernante(Cesar)",
    "∀x Romano(x) => (Leal(x, Cesar) ∨ Odia(x, Cesar))",
    "∀x ∀y (Hombre(x) ∧ Gobernante(y) ∧ IntentaAsesinar(x, y)) => -Leal(x, y)",
    "IntentaAsesinar(Marco, Cesar)",
    "∀x ∀y (IntentaAsesinar(x, Cesar) ∧ IntentaAsesinar(y, Cesar)) => Complices(x,y)",
    "∀x ∀y (Odia(x, Cesar) ∧ Odia(y, Cesar)) => Conspiran(x,y)"
]

curiosidad_tuna_sentencia = "Mata(Curiosidad, Tuna)"
curiosidad_tuna = [
    "∀x ∀z ∃y (Animal(z) => Ama(x,z)) => Ama(y,x)",
    "∀x ∃z ∀y (Animal(z) ∧ Mata(x,z)) => -Ama(y,z)",
    "∀x Animal(x) => Ama(Jack,x)",
    "Mata(Jack,Tuna) ∨ Mata(Curiosidad,Tuna)",
    "Gato(Tuna)",
    "∀x Gato(x) => Animal(x)"
]

p1 = [
    "∀x ∃y IntentaAsesinar(x,y) <=> Odia(x,y)",
    "IntentaAsesinar(Marco, Cesar)"
]

axiomas = marco_cesar
sentencia = "Conspiran(Antonio, Marco)"
print(".....................................")
print("Axiomas")
print(".....................................")
for axioma in axiomas:
    print(axioma)
print("________________")
print(sentencia+" ?")
print(".....................................")
print(refutacion(axiomas, sentencia))
