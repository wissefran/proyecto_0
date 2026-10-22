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

    with open(ruta, "r", encoding="cp1252") as f:

        for linea in f:
            campos = linea.strip().split(";")
            ciudad = campos[0].strip()
            datos = campos[1:] 
            viento = separar_viento(campos[8])
            datos[7] = viento
            observaciones[ciudad] = viento 
            
        return observaciones    