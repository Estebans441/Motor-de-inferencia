from inferencia import *

sentencia_no_uni = "Odia(x, y)"
axiomas_no_uni = [
    "Hombre(x)",
    "Pompeyano(x)",
    "∀x Pompeyano(x) => Romano(x)",
    "Gobernante(y)",
    "∀x Romano(x) => (Leal(x, y) ∨ Odia(x, y))",
    "∀x ∀y (Hombre(x) ∧ Gobernante(y) ∧ IntentaAsesinar(x, y)) => -Leal(x, y)",
    "IntentaAsesinar(x, y)"
]

sentencia_uni = "-Odia(Marco, Cesar)"
axiomas_uni = [
    "Hombre(Marco)",
    "Pompeyano(Marco)",
    "∀x Pompeyano(x) => Romano(x)",
    "Gobernante(Cesar)",
    "∀x Romano(x) => (Leal(x, Cesar) ∨ Odia(x, Cesar))",
    "∀x ∀y (Hombre(x) ∧ Gobernante(y) ∧ IntentaAsesinar(x, y)) => -Leal(x, y)",
    "IntentaAsesinar(Marco, Cesar)"
]

sentencia2 = "Mata(Curiosidad, Tuna)"
axiomas2 = [
    "∀x ∀z ∃y (Animal(z) => Ama(x,z)) => Ama(y,x)",
    "∀x ∃z ∀y (Animal(z) ∧ Mata(x,z)) => -Ama(y,x)",
    "∀x Animal(x) => Ama(Jack,x)",
    "Mata(Jack,Tuna) ∨ Mata(Curiosidad,Tuna)",
    "Gato(Tuna)",
    "∀x Gato(x) => Animal(x)"
]

axiomas = axiomas2
sentencia = "-Ama(Jack, Tuna)"
print(".....................................")
print("Axiomas")
print(".....................................")
for axioma in axiomas:
    print(axioma)
print("________________")
print(sentencia+" ?")
print(".....................................")
print(refutacion(axiomas, sentencia))
