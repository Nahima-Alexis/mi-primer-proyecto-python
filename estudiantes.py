lista_estudiantes = []
def menu():
    print("\n")
    print("="*49)
    print("                  MENU PRINCIPAL                   ")
    print("="*49)
    print("[ 1 ] Agregar estudiantes")
    print("[ 2 ] Ver estudiantes")
    print("[ 3 ] Salir")
    
def agregar_estudiante():
    nombre  = input("\n--> Ingresa tu nombre <--\n>>> ")
    edad    = int(input("\n--> Ingresa tu edad <--\n>>> "))
    nota    = float(input("\n--> Ingresa tu nota <--\n>>> "))
    
    nuevo_estudiante = {
        "* Nombre" : nombre,
        "* Edad"   : edad,
        "* Nota"   : nota
    }
    lista_estudiantes.append(nuevo_estudiante)
    
def ver_estudiantes():
    if lista_estudiantes == []:
        print("Todavia no hay estudiantes registrados.")  
    else:
        for estudiantes in lista_estudiantes:
            print("-"*30)
            print(f"Nombre: {estudiantes['* Nombre']}")
            print(f"Edad:   {estudiantes['* Edad']}")
            print(f"Nota:   {estudiantes['* Nota']}")
        print("-"*30)
while True: 
    menu()
    try:
        opcion = int(input("\nElige una opcion: "))
        if opcion == 1:
            agregar_estudiante()
        elif opcion == 2:
            ver_estudiantes()          
        elif opcion == 3:
            print("\nSaliendo...")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")
    except ValueError:
        print("ERROR! DEBE INGRESAR UN NUMERO ENTERO.")
            