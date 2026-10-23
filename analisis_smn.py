import sys
from funciones_smn import leer_observaciones

def main():
    if len(sys.argv) < 2:
        print("ERROR, faltan datos")
        print("Comando esperado: python analisis_smn.py datos/observaciones_smn.txt")
        sys.exit(1) 

    for i, dat in enumerate(sys.argv[1:], start=1):
        print(f"\n >>> analisis de archivo {i} : {dat} <<< ") 

        try: 
            datos = leer_observaciones(dat)
            if not datos: 
                print(f"aviso: el archivo '{dat}' esta vacio") 
                continue 
        
        finally:
            print(datos)
if __name__ == "__main__": 
    main()