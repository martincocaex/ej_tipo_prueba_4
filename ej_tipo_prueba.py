lista_usuarios= []

def opciones_validador():
    while True:
        try:
            opcion= (int(input("Ingrese uuna opcion del 1 - 4: ")))
            if opcion <1 or opcion >4:
                print("Eror debe ingresar una opcion entre el 1 y el 4.")
                continue
            return opcion
        except ValueError:
            print("Error la opcion ingreseda no esta en el rango de numeros 1 - 4")
            continue




def ingresar_usuarios():
    while True:

        verificador_usuarios = True
        nombre_usuario = input("Ingrese el nombre del usuario: ")
        if len(nombre_usuario)==0:
            print("Error el nombre de usuario ya existe")
            continue 
        for usuario in lista_usuarios:
            if usuario["nombre"]== nombre_usuario:
                print("Error el nombre de usuario ya existe")
                verificador_usuarios = False
        

            if verificador_usuarios ==False:
                continue
            break
        while True:
            genero=input("Ingrese el sexo (M o F: )")
            if genero !="M" and genero !="F":
                print("Erorr: Ingrese una opcion valida (M/F)")
                continue
            break
        while True:
            numero="0123456789"
            letras="qwertyuiopasdfghjklzxcvbnm"
            verificador_numero= False
            verificador_letras= False
            verificador_espacios = True
            contrasena = input("Ingrese una contrasena: ")

            if len(contrasena)<8:
                print("Error la contrasena no puede exeder los 8 caracteres")
                continue




            for caractar in contrasena:
                for n in numero:
                    if caractar==n:
                        verificador_numero = True
                for j in letras:
                    if caractar==j:
                        verificador_letras = True
                
                if verificador_espacios==False:
                    continue

                if verificador_espacios==False or verificador_letras== False:
                    print("Error la contrasena debe tener almenos un numero y letra.")
                    continue
                break

            return {"nombre":nombre_usuario,"genero":genero,"contrasena":contrasena}


def verificar_usuario():
    usuario=input("Ingrese el nombre del usuario que desea buscar: ")
    for i in lista_usuarios:
        if usuario==i ["nombre"]:
            return i



def verificar_usario_2():
    intentos = 0  # Inicializar la variable
    usuario = input("Ingrese el nombre del usuario que desea buscar: ")
    for i in lista_usuarios:
        if usuario == i["nombre"]:
            return intentos
        intentos += 1
    return None
        









while True:
    
    print("Menu de usuarios")
    print("[1]- ingresar usuario")
    print("[2]- buscar usuario")
    print("[3]- eliminar usuario")
    print("[4]- salir")

    opcion = opciones_validador()




    if opcion ==1:
            nuevo_usurio=ingresar_usuarios()
            lista_usuarios.append(nuevo_usurio)
            print("Usuario agregado corectamente.")









    if opcion ==2:
            usuario = verificar_usuario()
            if usuario== None:
                print("Usuario ingresado no existe")
                continue
            print(f"Usuario encontrado: {usuario["genero"]} y su contrasena es: {usuario["contrasena"]}.")



    if opcion ==3:
            usuario = verificar_usario_2()
            if usuario== None:
                print("El usuario ingresado no existe")
                continue
            del lista_usuarios[usuario]
            print("Usuario encontrado con existo")


        
   



    if opcion == 4:
            print("Saliendo del menu.")
            break

