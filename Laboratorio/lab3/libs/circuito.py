import numpy as np

def resolver_nodos(Y: np.ndarray, I: np.ndarray) -> np.ndarray:
    """
    Resuelve el sistema de ecuaciones nodales Y * V = I.
    Retorna el vector de voltajes V. Retorna None si la matriz es singular.
    """
    try:
        # Resolver sistema sin invertir explícitamente la matriz
        V = np.linalg.solve(Y, I)
        return V
    except np.linalg.LinAlgError:
        print("[Error Matemático] La matriz de admitancia es singular y no tiene solución única.")
        return None

if __name__ == '__main__':
    # Pruebas unitarias aisladas
    Y_test = np.array([[2.0, -1.0], [-1.0, 3.0]])
    I_test = np.array([5.0, 2.0])
    V_test = resolver_nodos(Y_test, I_test)
    print("Prueba de V_test:", V_test)