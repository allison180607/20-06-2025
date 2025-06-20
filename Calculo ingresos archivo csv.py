#Programa para calcular los ingresos de venta atravez de un archivo csv

import csv

#Paso 1: Ingresar datos de producto
print("=== Ingreso de datos de ventas ===")
ventas = []

while True:
    fecha = input("Fecha (YYYY-MM-DD): ").strip()
    producto = input("Producto: ").strip()
    cantidad = input("Cantidad: ").strip()
    precio = input("Precio unitario: ").strip()

    ventas.append([fecha, producto, cantidad, precio])

    continuar = input("¿Deseas ingresar otra venta? (s/n): ").strip().lower()
    if continuar != 's':
        break

#Paso 2: Crear el archivo CSV con los datos ingresados
with open('ventas.csv', mode='w', newline='', encoding='utf-8') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['fecha', 'producto', 'cantidad', 'precio']) # encabezado
    escritor.writerows(ventas)

print("\nArchivo 'ventas.csv' creado con éxito.\n")

#Paso 3: Consultar producto específico
producto_buscado = input("¿Qué producto deseas consultar?: ").strip().lower()

total_ingresos = 0.0
total_unidades = 0
encontrado = False

with open('ventas.csv', mode='r', newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        producto = fila['producto'].strip().lower()
        if producto == producto_buscado:
            try:
                cantidad = int(fila['cantidad'])
                precio = float(fila['precio'])
                total_unidades += cantidad
                total_ingresos += cantidad * precio
                encontrado = True
            except ValueError:
                print("Error: cantidad o precio inválido en una fila.")

if encontrado:
    print(f"\nProducto: {producto_buscado.capitalize()}")
    print(f"Total de unidades vendidas: {total_unidades}")
    print(f"Total de ingresos generados: ${total_ingresos:.2f}")
else:
    print(f"\nNo se encontraron ventas para el producto: {producto_buscado}")