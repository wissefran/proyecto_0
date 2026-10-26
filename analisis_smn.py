import sys
from funciones_smn import leer_observaciones, mostrar_resumen

def main():
    if len(sys.argv) < 2:
        print("ERROR, faltan datos")
        print("Comando esperado: python3 analisis_smn.py datos/observaciones_smn.txt")
        sys.exit(1)

    for i, dat in enumerate(sys.argv[1:], start=1):
        print(f"\n>>> Análisis de archivo {i}: {dat} <<<")

        try:
            datos = leer_observaciones(dat)

            if not datos:
                print(f"Aviso: el archivo '{dat}' está vacío")
                continue

            mostrar_resumen(datos)

        except FileNotFoundError:
            print(f"ERROR: no se encontró el archivo '{dat}'")

if __name__ == "__main__":
    main()