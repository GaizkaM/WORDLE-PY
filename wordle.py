import os
import random
import sys
from datetime import datetime
   
# ----------------------------
# Funciones principales
# ----------------------------

def jugar_partida():

    # Configuración inicial
    print("\n" * 3)
    nombre = input("Introduce tu nombre: ").strip()

    # Selección de idioma
    print(f"\nBienvenido {nombre}, elige idioma:\n1. Castellano\n2. Catalán")
    idioma = input("Opción: ")
    
    palabras = cargar_palabras(idioma)
    
    palabra_objetivo = random.choice(palabras)
    intentos = int(input("\nNúmero de intentos: "))
    
    # Game loop
    for intento in range(1, intentos + 1):
        print(f"\n--- Intento {intento} ---")
        while True:
            palabra = input("Palabra: ").upper()
            if len(palabra) == 5 and palabra in palabras:
                break
            print("¡Palabra inválida! Debe tener 5 letras y estar en la lista.")
        
        # Verificar letras
        resultado = []
        for i in range(5):
            if palabra[i] == palabra_objetivo[i]:
                resultado.append('\033[92m' + palabra[i])  # Verde
            elif palabra[i] in palabra_objetivo:
                resultado.append('\033[93m' + palabra[i])  # Amarillo
            else:
                resultado.append('\033[0m' + palabra[i])   # Blanco
        
        print(" ".join(resultado) + '\033[0m')
        
        if palabra == palabra_objetivo:
            print(f"\n¡Correcto {nombre}! Acertaste en {intento} intentos.")
            break
    else:
        print(f"\n¡Agotaste tus intentos! La palabra era: {palabra_objetivo}")
    
    # Guardar historial
    with open("historial.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {nombre} - Palabra: {palabra_objetivo}\n")

def ver_estadisticas():
    try:
        with open("historial.txt", "r", encoding="utf-8") as f:
            print("\n" + "-" * 50)
            print("HISTORIAL DE PARTIDAS")
            print("-" * 50)
            print(f.read())
    except FileNotFoundError:
        print("\nNo hay historial de partidas aún.")

# ----------------------------
# 1. CONFIGURACIÓN INICIAL
# ----------------------------
DIR_WORDLE = os.path.dirname(os.path.abspath(__file__))

# ----------------------------
# 2. FUNCIÓN PARA CARGAR PALABRAS
# ----------------------------
def cargar_palabras(idioma):
    """Carga las palabras desde el archivo correspondiente al idioma"""
    nombre_archivo = "wordle_es.txt" if idioma == "1" else "wordle_ca.txt"
    ruta_completa = os.path.join(DIR_WORDLE, nombre_archivo)
    
    try:
        with open(ruta_completa, "r", encoding="utf-8") as f:
            palabras = [line.strip().upper() for line in f if len(line.strip()) == 5]
        
        if not palabras:
            print(f"⚠️ El archivo {nombre_archivo} está vacío")
            return None
        
        return palabras
    
    except FileNotFoundError:
        print(f"❌ Error: Archivo {nombre_archivo} no encontrado en:")
        print(f"   {ruta_completa}")
        return None


# ----------------------------
# Menú principal
# ----------------------------
def main():
    while True:
        print("\n" * 3)
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        print("%                    WORDLE                     %")
        print("%              1. Jugar una partida             %")
        print("%     2. Ver estadísticas de partidas           %")
        print("%              3. Salir                         %")
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            jugar_partida()
        elif opcion == "2":
            ver_estadisticas()  # Asegúrate de definir esta función
        elif opcion == "3":
            print("\n¡Hasta pronto!")
            break
        else:
            print("\nOpción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
