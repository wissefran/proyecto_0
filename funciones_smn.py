from datetime import datetime 

def separar_viento(campo_viento: str) -> tuple:
    partes = campo_viento.strip().split()

    if partes[0] == "Calma": 
        return ("Calma", None) 

    direccion = " ".join(partes[:-1]) 
    velocidad = int(partes[-1]) 

    return (direccion, velocidad)



def parsear_fecha_hora(fecha: str, hora: str) -> datetime:
    meses = {                 
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12
    }

    dia, mes, anio = fecha.split("-")  

    fecha_hora = datetime(
        int(anio),
        meses[mes.lower()],  
        int(dia),
        int(hora[:2]),   
        int(hora[3:])
    )

    return fecha_hora


def leer_observaciones(ruta: str) -> dict:
    
    observaciones = dict()
    
    if "observaciones1_smn.txt" in ruta:
         codificacion = "utf-8"
    else:
         codificacion = "iso-8859-1"


    with open(ruta, "r", encoding=codificacion) as f:

        for linea in f:
            campos = linea.strip().split(";")

            if len(campos) == 10:
               ciudad = campos[0].strip()
               datos = campos[1:] 
               viento = separar_viento(campos[8])
               datos[7] = viento
               observaciones[ciudad] = datos
            
    return observaciones    


def cantidad_ciudades(observaciones: dict) -> int:
    return len(observaciones)

def cantidad_ciudades_completas(observaciones: dict) -> int:
    cantidad = 0

    for datos in observaciones.values():
        completa = True

        for dato in datos:
            if dato == "No se calcula":
                completa = False
                break

        if completa:
            cantidad += 1

    return cantidad

def top_n_ciudades(observaciones: dict, campo: str, n: int, descendente: bool = True) -> list:
    posiciones = {
        "temperatura": 4,
        "humedad": 6,
        "presion": 8
    }

    lista_ordenada = []

    for ciudad, datos in observaciones.items():
        if campo == "velocidad_viento":
            valor = datos[7][1]
        elif campo in posiciones:
            valor = datos[posiciones[campo]]
        else:
            continue

        if valor is not None and valor != "No se calcula" :
          if campo == "presion":
             valor = valor.replace("/", "").strip()

          valor = float(valor)
          lista_ordenada.append((valor, ciudad))
    
    lista_ordenada.sort(reverse=descendente)

    resultado = []

    for valor, ciudad in lista_ordenada[:n]:
        resultado.append((ciudad, valor))

    return resultado

def horarios_reportados(observaciones: dict) -> list:
    horarios = []
    for datos in observaciones.values():
        hora = datos[1]

        if hora not in horarios:
            horarios.append(hora)

    horarios.sort()
    return horarios

def mostrar_resumen(observaciones: dict) -> None:
    print("===== RESUMEN DE OBSERVACIONES METEOROLÓGICAS =====")

    print("\nCantidad de ciudades:", cantidad_ciudades(observaciones))

    print("Cantidad de ciudades completas:", cantidad_ciudades_completas(observaciones))

    print("\nHorarios reportados:")
    print(horarios_reportados(observaciones))

    print("\n--- 5 ciudades con mayor temperatura ---")
    resultado = top_n_ciudades(observaciones, "temperatura", 5)
    for ciudad, valor in resultado:
        print(ciudad, "-", valor)

    print("\n--- 5 ciudades con mayor humedad ---")
    resultado = top_n_ciudades(observaciones, "humedad", 5)
    for ciudad, valor in resultado:
        print(ciudad, "-", valor)

    print("\n--- 5 ciudades con mayor presión ---")
    resultado = top_n_ciudades(observaciones, "presion", 5)
    for ciudad, valor in resultado:
        print(ciudad, "-", valor)

    print("\n--- 5 ciudades con mayor velocidad del viento ---")
    resultado = top_n_ciudades(observaciones, "velocidad_viento", 5)
    for ciudad, valor in resultado:
        print(ciudad, "-", valor)