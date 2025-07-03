juegos = {
 "A123": ["FIFA 24", "PS5", "Deportes", 10],
 "B456": ["Mario Kart 8", "Switch", "Carreras", 3],
 "C789": ["The Last of Us II", "PS5", "Acción", 18],
 "D321": ["Zelda BOTW", "Switch", "Aventura", 12],
 "E654": ["Minecraft", "PC", "Creativo", 6]
}
ventas = {
 "A123": [49990, 15],
 "B456": [39990, 10],
 "C789": [59990, 5],
 "D321": [54990, 0],
 "E654": [19990, 25]
}

def buscar_por_consola(consola):
    total = 0
    for codigo,dato in juegos.items():
        if dato[1].lower() == consola.lower() and codigo in ventas :
            total = total + ventas[codigo][1]
    print (f"exiten {total} de unidades de la {consola}")

def jugar_por_rango():
    resultado = []
    for codigo,datos in juegos.items():
        edad = datos[3]
        if min_edad <= edad and edad <= max_edad and ventas[codigo][1] > 0 :
            resultado.append(datos[0])
    if resultado :
        print(resultado)
    else:
        print("no hay juego")
def actualizar_precio(codigo, nuevo_precio):
    if codigo in ventas:
        ventas[codigo][0]

while True:
    try:
        print("*****Menu Game Zone*****")
        print("1. Buscar por consola")
        print("2. Juegos por rango de edad")
        print("3. Actualizar precio")
        print("4. Salir")
        opc = int(input("ingrese opcion: "))
        if opc == 1:
            consola = input("ingrese consola (ps5,switch,pc)")
            buscar_por_consola(consola)
        elif opc == 2:
            while True:
                try:
                    min_edad = input("ingrese edad minima")
                    max_edad = input("ingrese edad maxima")
                    break
                except ValueError:
                    print("debe ingresar un valor numerico")
            jugar_por_rango(min_edad,max_edad)        
        elif opc == 3:
            codigo = input("ingrese codigo del juego")
            try:
                nuevo_precio = int(input("ingrese un nuevo precio"))
                print(ventas)
            except ValueError:
                print("debe ingresar un numero")
            if actualizar_precio(codigo,nuevo_precio):
                print("precio actualizado")
            else:
                print("codigo no encontrado")   
        elif opc == 4:
            print("programa finalizado")
            break
        else:
            print("opcion no valida")         
    except ValueError:
        print("debe ingresar un numero")