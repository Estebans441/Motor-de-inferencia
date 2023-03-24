from inferencia import *

# ∀, ∃, =>, <=>, ∧, ∨
sentencia = "Odia(Marco, Cesar)"
axiomas = [
    "Hombre(Marco)",
    "Pompeyano(Marco)",
    "∀x Pompeyano(x) => Romano(x)",
    "Gobernante(Cesar)",
    "∀x Romano(x) => (Leal(x, Cesar) ∨ Odia(x, Cesar)) ",
    "∀x ∀y (Hombre(x) ∧ Gobernante(y) ∧ IntentaAsesinar(x, y)) => -Leal(x, y)  ",
    "IntentaAsesinar(Marco, Cesar)"
    ]

axiomas_n = forma_normal_conjuntiva(axiomas)
for x in axiomas_n:
    print(x)
