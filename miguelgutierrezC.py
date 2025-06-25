data = {"entradas":
    [
        {
            "nombre":"tiare",
            "tipo_entrada":"G o V",
            "codigo":"entrada1"
        },
        {
            "nombre":"miguel",
            "tipo_entrada":"G o V",
            "codigo":"entrada2"
        },
        {
            "nombre":"vicente",
            "tipo_entrada":"G o V",
            "codigo":"entrada1"
        },
     
     ]

}
def validar_texto(mensaje_input:str):
    while True:
        texto = input(mensaje_input)
        if len(texto) == 0:
            print("La opcion debe contener algun caracter! ")
            continue
        else:
            return texto
        
def validar_numero_entero_positvo(mensaje_input:str):
    while True:
        try:
            numero = mensaje_input
            if numero <= 0:
                print("Solo puede ingresar numeros de caracter entero positivo! ")
                continue    
        except ValueError:
            print("Ingrese un numero entero positivo! ")
            break

def compra_entrada(entradas):
    entrada_comprada = {

                    "nombre":"nombre",
                    "tipo_entrada":"G o V",
                    "codigo":int
                    
                    }
    data["entradas"].append(entrada_comprada)


print(" ***Totem autoservicio*** ") 
print(" *Compra tu entrada aqui* ")
print("1.- Compra de entradas para Los fortificados ")
print("2.- Compra de entradas para Los iluminados ") 
print("3.- Stock de entrada para este concierto ")
print("4.- Salir ")      




stock = 500
stock1 = 500
while True:
    opciones = int(input("ingrese una opcion : "))

    if opciones == 1:
        print("Ingrese sus datos  ")
        nombre = validar_texto("Nombre : ")
        tipo_entrada = validar_texto("Entrada general o vip : ")
        codigo = input("Ingrese el codigo : ")
        

        codigo == "entrada1"
        print("Compra exitosa ")
        compra_entrada
        break

    elif opciones == 2:
        print("Ingrese sus datos")
        nombre = validar_texto("Nombre : ")
        tipo_entrada = validar_texto("Entrada general o vip : ")
        codigo = input("Ingrese el codigo : ")
        
        

        codigo == "entrada2"
        print("Compra exitosa ")
        compra_entrada
        break

    elif opciones == 3:
        print(f"Entradas disponibles para Los fortificados:  ",stock)
        print(f"Entradas disponibles para Los iluminados:  ",stock1)

    elif opciones == 4:
        print("Saliendo de totem autoservicio... ")    
