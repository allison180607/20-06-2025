import os
#Importamos para usar la funcion: os.path.exists(ruta)
ARCHIVO = "Estudiantes.txt"


def cargar_estudiantes():
    estudiantes = []
    #La funcion os.path.exists(ruta) nos permite saber si existe el archivo en una ruta predeterminada
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera = linea.strip().split(",")
                #linea.strip() elimina los espacios en blanco al inicio y al final de la linea
                #split(",") divide la linea en una lista de elementos separados por comas
                estudiantes.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "apellido": apellido,
                    "carrera": carrera
                })
    return estudiantes


def guardar_estudiantes(estudiantes):
    with open(ARCHIVO, "w") as archivo:
        for est in estudiantes:
            linea = f"{est['codigo']},{est['nombre']},{est['apellido']},{est['carrera']}\n"
            archivo.write(linea)


def crear_estudiante(estudiantes):
    codigo = input("Codigo del estudiante: ")
    #verificar si el codigo ya esxite
    #La funcion any() devuelve True si al menos un elemento del iterable es verdadero
    if any(est['codigo'] == codigo for est in estudiantes):
        print("El codigo ya existe")
        return 
    
    nombre = input("Nombre del estudiante: ")
    apellido = input("Apellido del estudiante: ")
    carrera = input("Carrera del estudiante: ")

    estudiantes.append({
        "codigo": codigo,
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera
    })
    guardar_estudiantes(estudiantes)
    print("Estudiante creado exitosamente.")


def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
        
    print("\nLista de estudiantes:")
    for est in estudiantes:
         print(f"Código: {est['codigo']}, Nombre: {est['nombre']}, Apellido: {est['apellido']}, Carrera: {est['carrera']}")
    print()


def actualizar_estudiante(estudiantes):
    codigo = input("Ingresa al codigo del estudiante a actualizar:")
    for est in estudiantes:
        if est['codigo'] == codigo:
            est['nombre'] = input(f"Nuevo nombre a (actual: {est['nombre']}): ") or est['nombre']
            est['apellido'] = input(f"Nuevo apellido (actual: {est['apellido']}): ") or est['apellido']
            est['carrera'] = input(f"Nueva carrera (actual: {est['carrera']}): ") or est['carrera']
            guardar_estudiantes(estudiantes)
            print("Estudiante actualizado.\n")
            return
    print("Estudiante no encontrado.\n")


def eliminar_estudiante(estudiantes):
    codigo = input("Ingresa el codigo del estudiante a eliminar: ")
    for est in estudiantes:
        if est['codigo'] == codigo:
            estudiantes.remove(est)
            guardar_estudiantes(estudiantes)
            print("Estudiante eliminado.\n")
            return
        print("Estudiante no encontrado.\n")


#Funcion menu principal
def menu():
    estudiantes = cargar_estudiantes()
    while True:
        print("\n--- Menu de Estudiantes ---")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        opcion = input("Selecciona una opcion (1-5): ")

        if opcion == "1":
            crear_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            actualizar_estudiante(estudiantes)
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion invalida, intenta de nuevo.")

#Instruccion 
menu()