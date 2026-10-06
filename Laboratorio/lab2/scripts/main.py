"""
Programa Principal del Sistema de Monitoreo Térmico en Línea de Producción.
Orquesta la interacción con el usuario por consola y consume las librerías de cálculo.
"""
import sys
from pathlib import Path

# =============================================================================
# DETECCIÓN DINÁMICA DE RUTAS (PATH RESOLUTION)
# =============================================================================
# Detecta la ruta absoluta de 'libs' respecto a la posición de este archivo
RUTA_LIBS = Path(__file__).resolve().parent.parent / "libs"
sys.path.append(str(RUTA_LIBS))

# Importación de la biblioteca modular
from telemetria import calcular_promedio_sensores, validar_temperaturas


def ejecutar_consola():
    """Ejecuta el ciclo de interacción interactivo por consola."""
    print("=" * 55)
    print("   SISTEMA DE MONITOREO DE LÍNEA DE PRODUCCIÓN (LAB 2)")
    print("=" * 55)
    
    while True:
        opcion = input("\nPresione ENTER para ingresar lecturas o escriba 'EXIT' para salir: ")
        if opcion.strip().upper() == "EXIT":
            print("\nCerrando el sistema de monitoreo de forma segura. ¡Hasta pronto!")
            break
            
        try:
            s1 = float(input("Ingrese Temperatura Sensor 1 (°C): "))
            s2 = float(input("Ingrese Temperatura Sensor 2 (°C): "))
            s3 = float(input("Ingrese Temperatura Sensor 3 (°C): "))
        except ValueError:
            print("[ERROR] Entrada inválida. Debe ingresar valores numéricos reales.")
            continue

        # Procesamiento mediante las funciones modulares
        promedio = calcular_promedio_sensores(s1, s2, s3)
        alerta, fallas = validar_temperaturas([s1, s2, s3], max_temp=75.0)

        # Visualización de resultados
        print("\n" + "-" * 40)
        print(f">> Promedio de la Línea: {promedio:.2f} °C")
        
        if alerta:
            print(f">> ALERTA: {fallas} sensor(es) superaron el límite crítico (75.0 °C)!")
        else:
            print(">> Estado de la línea: Estable (todos los sensores dentro del rango operativo).")
        print("-" * 40)


if __name__ == '__main__':
    ejecutar_consola()