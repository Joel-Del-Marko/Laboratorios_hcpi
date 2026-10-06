import sys
from pathlib import Path
import numpy as np

# Resolución dinámica de la ruta hacia 'libs'
RUTA_LIBS = Path(__file__).resolve().parent.parent / "libs"
sys.path.append(str(RUTA_LIBS))

from circuito import resolver_nodos

def ejecutar():
    print("=" * 45)
    print("   RESOLUCIÓN DE REDES ELÉCTRICAS (LAB 3)")
    print("=" * 45)
    
    # Caso de prueba: Matriz Y (3x3) y Vector I (3x1)
    Y_prueba = np.array([
        [ 4.0, -1.0, -1.0],
        [-1.0,  3.0, -2.0],
        [-1.0, -2.0,  5.0]
    ])
    I_prueba = np.array([1.0, 2.0, 3.0])
    
    print("\n>> Resolviendo sistema de ecuaciones nodales... yeeep")
    V_nodos = resolver_nodos(Y_prueba, I_prueba)
    
    if V_nodos is not None:
        for i, v in enumerate(V_nodos, start=1):
            print(f">> Voltaje Nodo {i}: {v:.2f} V")
            
    print("=" * 45)

if __name__ == '__main__':
    ejecutar()
