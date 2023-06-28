import csv

# Abre el archivo CSV en modo lectura
with open('datos.csv', 'r') as datos:
    # Crea un objeto lector de CSV
    lector_csv = csv.reader(datos)  # método específico para csv
    encabezado = next(lector_csv)
    print(encabezado)
    print(".....")
        

    for fila in lector_csv:
      print(fila)
      for celda in fila:
         print(celda)
         print("hello")