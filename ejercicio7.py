#Ejercicio 7, crear un archivo con nombres de estudiantes y sus calificaciones separadas por coma, y escribimos un programa que calcules el promedio de las calificaciones de cada estudiante y lo guarde en un archivo llamado "promedios.txt". El archivo de entrada se llamará "estudiantes.csv" y tendrá el siguiente formato:
# nombre,calificacion1,calificacion2,calificacion3
def calcular_promedios():
    try:
        with open("estudiantes.csv", "r", encoding="utf-8") as archivo_entrada, \
             open("promedios.txt", "w", encoding="utf-8") as archivo_salida:  # Abrimos el archivo de entrada en modo lectura y el de salida en modo escritura
            for linea in archivo_entrada:
                partes = linea.strip().split(",") # Dividimos la línea en partes usando la coma como separador
                nombre = partes[0]
                try:
                    calificaciones = list(map(float, partes[1:]))
                    if calificaciones:  # Verificamos que haya calificaciones
                        # Calculamos el promedio de las calificaciones
                        promedio = sum(calificaciones) / len(calificaciones)
                        archivo_salida.write(f"{nombre},{promedio:.2f}\n")
                except ValueError:  # Si hay un error al convertir las calificaciones a float
                    archivo_salida.write(f"{nombre},Error en calificaciones\n")
    except FileNotFoundError:  # Si el archivo de entrada no existe o no lo encuentra
        print("El archivo 'estudiantes.csv' no existe.")

calcular_promedios()  # Llamamos a la función para calcular los promedios
# Aseguramos que el archivo de salida se cree o se sobrescriba correctamente
#enviamos un mensaje de finalizacion
print("Cálculo de promedios completado. Los resultados se guardaron en 'promedios.txt'.")