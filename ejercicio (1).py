productos = {'8475HD': ['hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
                      '2175HD': ['acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
                      'JjfFHD': ['asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
                     'fgdxFHD': ['hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
                     'GF75HD': ['acer', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
                     '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
                     '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
                     'UWU131HD': ['dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],}

stock = {'8475HD': ["hp",387990,10], '2175HD': ["acer",327990,4], 'JjfFHD': ["asus",424990,1],
              'fgdxFHD': ["hp",664990,21], '123FHD': ["lenovo",290890,32], '342FHD': ["lenovo",444990,7],
              'GF75HD': ["acer",749990,2], 'UWU131HD': ["dell",349990,1],
                 }

marcas = { "hp": [31], "acer":[6], "asus":[1], "lenovo":[39], "dell":[1]}

def stock_marca():
    modelo = []    
    total = 0
    marca = input('Ingrese marca a consultar: ')

    for clave, valor in productos.items():  
        if marca.lower() == valor[0]:  
            modelo.append(clave)

    for modelo_actual in modelo:
        if modelo_actual in stock:
            precio, cantidad = stock[modelo_actual]
            total += cantidad
    print(f'El stock es: {total}')

def busqueda_precio():
    p_min = int(input("Ingrese precio mínimo: "))
    p_max = int(input("Ingrese precio máximo: "))

    encontrados = False  # bandera para saber si se encontró al menos uno
    print("\nModelos en el rango de precios:")
    for modelo, datos in stock.items():
        marca, precio, cantidad = datos
        if p_min <= precio <= p_max:
            almacenamiento = productos[modelo][4]  
            print(f"- Modelo: {modelo}, Almacenamiento: {almacenamiento}, Precio: ${precio}")
            encontrados = True

        if not encontrados:
            print("No hay notebooks en ese rango de precios.")

        else:
            print("no hay notebooks en ese rango de precios")

def listado_productos():
    print("------ Listado de Notebooks Ordenados -------")
    for clave in productos.items():
        print(f'{[0]}\t{[0]}\t{[2]}\t{[4]}')
        #arreglar!!!

while True:
    print("")
    print('*** MENÚ PRINCIPAL ***')
    print('1. Stock marca.')
    print('2. Busqueda por precio.')
    print('3. Listado de productos.')
    print('4. Salir.')
    print("")
    opc=input('Ingrese Opción: ')
    if opc=='1':
        stock_marca()
    elif opc=='2':
        busqueda_precio()
    elif opc=='3':
        listado_productos()
    elif opc=='4':
        print('Programa finalizdo')
        break
    else:
        print('Debe seleccionar una opción válida!')
