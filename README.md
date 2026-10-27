# Proyecto 0: Analisis de Observaciones Metereologicas del Sistema Meteorologico Nacional

Este proyecto consiste en desarrollar un programa en Python para leer, organizar y analizar observaciones meteorológicas del Servicio Meteorológico Nacional (SMN), en cual crea varias estructuras
de datos (diccionarios/listas) donde desarrolla caracteristicas principales de distintas ciudades de Argentina como por ejemplo: la temperatura total, velocidad de viento (en km), etc .
Tambien permite consultar la cantidad de ciudades registradas, las observaciones completas, los horarios reportados y las ciudades con los valores más altos de distintas variables meteorológicas.

## Cómo obtener los datos

Los archivos de entrada se obtienen desde la página oficial del Servicio Meteorológico Nacional:

**Página de descarga:** https://www.smn.gob.ar/descarga-de-datos

Para obtener los datos, seguir estos pasos:

1. Ingresar a la página de descarga del SMN.
2. Buscar y descargar el archivo `.rar` correspondiente a los datos utilizados en el proyecto.
3. Localizar el archivo descargado en la computadora.
4. Descomprimirlo para obtener los archivos de texto con las observaciones meteorológicas.
5. Colocar los archivos extraídos en la carpeta `/datos` del proyecto.


## Cómo ejecutar el proyecto

El proyecto se ejecuta desde una terminal utilizando Python 3.

1. Abrir una terminal.
2. Ubicarse en la carpeta del proyecto.
```bash
cd proyecto-0
```
3. Comprobar que los archivos de entrada (observaciones_smn.txt) estén dentro de la carpeta `/datos`.
4. Ejecutar el siguiente comando:

```bash
python3 analisis_smn.py datos/observaciones_smn.txt datos/observaciones1_smn.txt
```

El programa procesa los archivos indicados y muestra por consola los resultados del análisis.

## Ejemplo de salida por consola

A continuación, se muestra un ejemplo de la salida obtenida al ejecutar el programa con el archivo `datos/observaciones_smn.txt`.

```text
>>> Análisis de archivo 1: datos/observaciones_smn.txt <<<
===== RESUMEN DE OBSERVACIONES METEOROLÓGICAS =====

Cantidad de ciudades: 121
Cantidad de ciudades completas: 25

Horarios reportados:
['09:00', '10:00', '11:00', '12:00', '13:00', '15:00']

--- 5 ciudades con mayor temperatura ---
Rivadavia - 28.0
Orán - 27.4
Pcia. Roque Saenz Peña - 26.7
Tartagal - 26.4
Resistencia - 26.3

--- 5 ciudades con mayor humedad ---
Bernardo De Irigoyen - 100.0
Ushuaia - 98.0
Paso De Indios - 92.0
Oberá - 92.0
Gobernador Gregores - 92.0

--- 5 ciudades con mayor presión ---
Aeroparque Buenos Aires - 1014.6
Río Gallegos - 1014.4
San Fernando - 1014.0
Dolores - 1013.7
El Palomar - 1013.4

--- 5 ciudades con mayor velocidad del viento ---
Mount Pleasant Airport (Islas Malvinas) - 42.0
Perito Moreno - 38.0
San Julián - 37.0
Río Gallegos - 37.0
Comodoro Rivadavia - 33.0
``` 
 
