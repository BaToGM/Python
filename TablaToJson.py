import pandas as pd
from googletrans import Translator

# Cargar la tabla de Excel
df = pd.read_excel('Libro.xlsx')

# Inicializar el traductor de Google
translator = Translator()

# Abrir el archivo para escribir la salida
with open('salida.txt', 'w', encoding='utf-8') as file:
    # Escribir el inicio de la lista de campos
    file.write("[\n")

    # Iterar a través de cada fila en el dataframe
    for index, row in df.iterrows():
        # Obtener los valores de la fila
        campo = row['CAMPO']
        descripcion = row['DESCRIPCIÓN']
        tipo_campo = row['TIPO CAMPO']

        # Traducir la descripción al inglés
        descripcion_en = translator.translate(descripcion, dest='en').text

        # Escribir los valores en el formato requerido
        output = {
            'name': campo,
            'type': tipo_campo,
            'description': descripcion,
            'description_en': descripcion_en
        }

        # Escribir la salida en el archivo
        if index > 0:
            file.write(",\n")
        file.write("{")
        file.write(f'"name": "{campo}", ')
        file.write(f"type: {tipo_campo}\n")
        file.write(f"description: {descripcion}\n")
        file.write(f"description_en: {descripcion_en}\n")
        file.write("}")

    # Escribir el final de la lista de campos
    file.write("\n]")
    
# Cerrar el archivo
file.close()

