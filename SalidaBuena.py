import pandas as pd
from googletrans import Translator
import textwrap

def encontrar_primer_punto(frase):
    indice_punto = frase.find(".")
    if indice_punto != -1:
        return indice_punto
    else:
        return None

def dividir_lineas(texto, max_palabras):
    palabras = texto.split()
    lineas = []
    linea_actual = ""
    contador_palabras = 0

    for palabra in palabras:
        if contador_palabras < max_palabras:
            linea_actual += palabra + " "
            contador_palabras += 1
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "
            contador_palabras = 1

    if linea_actual:
        lineas.append(linea_actual.strip())

    return lineas

# Obtener la hoja a buscar
sheet_name = input("Ingrese el nombre de la hoja que desea buscar: ")

# Cargar la tabla de Excel
df = pd.read_excel('Libro.xlsx', sheet_name=sheet_name)

# Inicializar el traductor de Google
translator = Translator()

# Obtener información del dataset
location = input("Ingrese el location del dataset: ")
dataset_name = input("Ingrese el nombre del dataset: ")
description = input("Ingrese la descripción del dataset: ")
owner = input("Autor")
part_fields = "ds"
# Abrir el archivo para escribir la salida
with open('salida.txt', 'w', encoding='utf-8') as file:
    # Escribir el inicio del dataset
    file.write("dataset {\n")
    file.write(f'  location: "{location}"\n')
    file.write(f'  name: "{dataset_name}"\n')
    file.write(f'  owner: "{owner}"\n')
    file.write(f'  frequency: "quarter"\n')
    file.write(f'  description: "{description}"\n')
    file.write("  attributes {\n")
    file.write(f'    type: "table"\n')
    file.write(f'    name: "fc_cem_{dataset_name}"\n')
    file.write(f'    part_fields: ["{part_fields}"]\n')
    file.write(f'    comments: "Tabla de tipo parquet"\n')
    file.write("  }\n")
    file.write("  schema_fields: [\n")

    # Iterar a través de cada fila en el dataframe
    for i, row in df.iterrows():
        # Obtener los valores de la fila
        campo = row['CAMPO']
        tipo_campo = row['TIPO CAMPO']
        descripcion = row['DESCRIPCIÓN'] if not pd.isnull(row['DESCRIPCIÓN']) else ""

        # Traducir la descripción al inglés
        descripcion_en = translator.translate(descripcion, dest='en').text
        
        # Encontramos el primer punto
        indice = encontrar_primer_punto(descripcion)

        # Escribir los valores en el formato requerido
        field_output = f'{{\n    name: "{campo}", type: "{tipo_campo}"\n'
        if indice is not None:
             primera_parte = descripcion[:indice + 1]
             segunda_parte = descripcion[indice + 1:]

             lineas_segunda_parte = dividir_lineas(segunda_parte,6)
            
             print (f'{primera_parte}'+"hoola hola")
             print (f'{segunda_parte}'+"hoola2 hola2")
             print (f'{lineas_segunda_parte}'+"hoola3 hola3")
             des_formateada=primera_parte +"\n" + "\n".join(lineas_segunda_parte)
             #des_formateada=descripcion[:indice + 1] + "\n" + descripcion[indice + 1:]
             field_output += f'    description: """{des_formateada}"""\n'
        else:
            field_output += f'    description: "{descripcion}"\n\n'
        field_output += "  },"
        # Escribir la salida en el archivo
        file.write(field_output)
    if part_fields is not None:
        field_output = f'{{\n    name: "ds", type: "string"\n'
        field_output += f'    description: "Periodo para el que se han agregado y calculado datos. Formato yyyy-MM-dd"\n'
        field_output += "  }"
        file.write(field_output)
    # Escribir el final del dataset
    file.write("]\n")
    file.write("}")

# Cerrar el archivo
file.close()
