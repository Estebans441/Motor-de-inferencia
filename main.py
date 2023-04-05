from inferencia import *

sentencia1 = "Odia(Marco, Cesar)"
axiomas1 = [
    "Hombre(Marco)",
    "Pompeyano(Marco)",
    "∀x Pompeyano(x) => Romano(x)",
    "Gobernante(Cesar)",
    "∀x Romano(x) => (Leal(x, Cesar) ∨ Odia(x, Cesar))",
    "∀x ∀y (Hombre(x) ∧ Gobernante(y) ∧ IntentaAsesinar(x, y)) => -Leal(x, y)",
    "IntentaAsesinar(Marco, Cesar)"
]

sentencia = "Odia(x, y)"
axiomas = [
    "Hombre(x)",
    "Pompeyano(x)",
    "∀x Pompeyano(x) => Romano(x)",
    "Gobernante(y)",
    "∀x Romano(x) => (Leal(x, y) ∨ Odia(x, y))",
    "∀x ∀y (Hombre(x) ∧ Gobernante(y) ∧ IntentaAsesinar(x, y)) => -Leal(x, y)",
    "IntentaAsesinar(x, y)"
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

print(refutacion(axiomas1, sentencia1))



