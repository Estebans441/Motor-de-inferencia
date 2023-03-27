from inferencia import *

sentencia = "Odia(Marco, Cesar)"
axiomas = [
    "Hombre(Marco)",
    "Pompeyano(Marco)",
    "∀x Pompeyano(x) => Romano(x)",
    "Gobernante(Cesar)",
    "∀x Romano(x) => (Leal(x, Cesar) ∨ Odia(x, Cesar))",
    "∀x ∀y (Hombre(x) ∧ Gobernante(y) ∧ IntentaAsesinar(x, y)) => -Leal(x, y)",
    "IntentaAsesinar(Marco, Cesar)"
]
axiomas = [
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

axiomas_n = forma_normal_conjuntiva(axiomas)
for x in axiomas_n:
    print(x)
