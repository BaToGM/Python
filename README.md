# Python
Los diferentes programas que hay hasta ahora son diferentes versiones de convertir unos archivos de entrada en un formato json, la primera version cogia un fichero txt donde estaban los datos y los saca en un formato json concreto, esta hecho de esta forma porque es lo que necesitaba de forma especifica, en la segunda version en vez de coger los datos de un fichero de texto, se cogen de un excel, y por ultimo termine dando el formato completo al fichero json para que saliera exactamente como yo queria y automatizar una tarea, ahorrandome varias horas de trabajo.

En la version actual, lee cualquier hora del archivo csv de entrada y busca en la primera fila los campos indicados y damos una salida especifica, ¿por que esto es asi? porque se trata de un programa personal para automatizar una tarea, para ahorrarme horas de trabajo que me llevaria crear esos hocoones de forma manual. 
Para ejecutar el script lo llamamos y le pasamos como argumento el archivo, despues nos ira solicitando los diferentes parametros par rellenar el hocoon.

### Futuras versiones     

Para futuras versiones me gustaria añadir:    
1- Buscar de forma correcta en las tablas que se generan en pandas.    
2- Dar diferentes formatos de Json dependiendo del location de entrada.     
3- Introducir mas campos si son necesarios.
