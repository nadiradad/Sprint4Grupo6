from typing import Dict, List
from component.condition import mostrarAlgo


def objIterator(argument):
    # Arreglo que guardar la informacion en objeto
    table: List[Dict[str]] = []
    
    for linea in argument:
        rowFlotante: Dict[str] = {}
        for columna in linea:
            rowFlotante[columna] = str(linea[columna])
        table.append(rowFlotante)
        
    mostrarAlgo(table) 