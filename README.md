# Motor de inferencia basado en resolucion
 
Programa que implementa el **Algoritmo de resolución por refutación**.
Se incluye un algoritmo de Unificación de Variables para que sea capaz de realizar la unificación de variables de tipo simbólico.

## Explicacion del algoritmo
El programa realiza la implementación de un algoritmo de resolución para lógica de primer orden en Python. El algoritmo toma como entrada una lista de axiomas y utiliza el proceso de resolución para determinar si la lista de axiomas es satisfacible o no.

El proceso de resolución utiliza cláusulas, que son disyunciones de literales. Las cláusulas se resuelven mediante la eliminación de literales opuestos. Si dos cláusulas tienen literales que se niegan mutuamente, se pueden unificar para producir una nueva cláusula que no contenga esos literales. Este proceso continúa hasta que no se puedan crear nuevas cláusulas o se encuentre una cláusula vacía (lo que indica que los axiomas son insatisfacibles).
