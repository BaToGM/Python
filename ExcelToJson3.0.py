import pandas as pd
from googletrans import Translator

# Obtener la hoja a buscar
sheet_name = input("Ingrese el nombre de la hoja que desea buscar: ")

# Cargar la tabla de Excel
df = pd.read_excel('Libro.xlsx', sheet_name=sheet_name)

# Inicializar el traductor de Google
translator = Translator()

# Obtener información del dataset
location =  input("Ingrese el location del dataset: ")
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
        
        # Escribir los valores en el formato requerido
        field_output = f'{{\n    name: "{campo}", type: "{tipo_campo}"\n'
        field_output += f'    description: "{descripcion}"\n'
        field_output += f'    description_en: "{descripcion_en}"\n'
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
