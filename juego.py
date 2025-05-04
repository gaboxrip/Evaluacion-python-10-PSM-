import os #importa el sistema operativo para limpiar la pantalla
import time #esta libreria se usa para pausar el juego
import random #importa numero aleatorio para los ataques del jugador y la cpu

#------------------#esta funcion limpia la pantalla del juego#------------------# Nota: esta funcion no tiene nada que ver con el funcionamiento del juego, solo es para limpiar la pantalla y que el juego se vea mejor.
def Limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

#------------------#Diccionario donde muestra a los persojanes#------------------#   
personajes = {
    "1": {"nombre": "Ripper", "Vida": 200, "ataque": 20, "especial": 30, "defensa": 12},
    "2": {"nombre": "Max", "Vida": 200, "ataque": 18, "especial": 35 ,"defensa": 10},
    "3": {"nombre": "Mussulini", "Vida": 200, "ataque": 20, "especial": 32 ,"defensa": 14},
    "4": {"nombre": "Undertaker", "Vida": 200, "ataque": 19, "especial": 34 ,"defensa": 15}
}

#------------------#Menu principal del juego#------------------#
while True:
    Limpiar()
    print("""
|----------------------------------------------------------------|
|                                                                |
|  █████╗  ██████╗   ███████╗ ███╗   ██╗  █████╗        ██╗  ██╗ |
| ██╔══██╗ ██╔══██╗  ██╔════╝ ████╗  ██║ ██╔══██╗       ╚██╗██╔╝ |
| ███████║ ██████╔╝  █████╗   ██╔██╗ ██║ ███████║        ╚███╔╝  |
| ██╔══██║ ██╔══██╗  ██╔══╝   ██║╚██╗██║ ██╔══██║        ██╔██╗  |
| ██║  ██║ ██║  ║██╗ ███████╗ ██║ ╚████║ ██║  ██║       ██╔╝ ██╗ |
| ╚═╝  ╚═╝ ╚═╝  ╚══╝ ╚══════╝ ╚═╝  ╚═══╝ ╚═╝  ╚═╝       ╚═╝  ╚═╝ |
|----------------------------------------------------------------|""")
    print("""""")
    print("|----------------------------------------------------------------|")
    print("|                             1. Historia                        | ")
    print("|                             2. Instrucciones                   | ")
    print("|                             3. Jugar                           | ")
    print("|                             4. Salir                           | ")
    print("|----------------------------------------------------------------|")

    opcion_menu = input("Elige una opcion: ")

    #------------------#Historia del juego#------------------#
    if opcion_menu == "1":
        Limpiar()
        print("""
        |------------------------------------------------------------------------------------|      
        |                                -- Historia del juego --                            |
        |Año 3029. El mundo ha sido reducido a ruinas y las naciones ya no existen.          |
        |La paz es un mito, y la justicia... una reliquia olvidada.                          |
        |                                                                                    |
        |Los sobrevivientes más fuertes, los más despiadados, se enfrentan en un único lugar:|
        |la temida *Arena X*.                                                                |
        |                                                                                    |
        |Aquí no hay reglas. Solo un objetivo:                                               |
        |¡Sobrevivir y convertirse en el Último Guerrero!                                    |
        |                                                                                    |
        |¿Tienes lo que se necesita para dominar la Arena X?                                 |   
        |------------------------------------------------------------------------------------|
          """)

        input("""Presiona Enter para volver al menu.""") #esta funcion permite regresar al menu principal del juego al precionar enter.

    #------------------#Instrucciones del juego#------------------#
    elif opcion_menu == "2":
        Limpiar()
        print("""
        |-------------------------------------------------------------------------------------------|
        |                               -- Instrucciones del juego --                               |
        |      1. Elige uno de los cuatros peleadores seleccionables para comenzar tu combate.      |
        |      2. Cada personaje tiene habilidades unicas.                                          |
        |      3. El jugador tendra que elegir entre atacar o defenderse.                           |
        |      4. El jugador se va a enfrentar a un enemigo aleatorio controlado por la computadora.|
        |      5. El jugador ganara si logra reducir la vida del enemigo a 0.                       |
        |-------------------------------------------------------------------------------------------|
              """)
    
        input("""Presiona Enter para volver al menu.""")
    
    #------------------#Jugar#------------------#
    elif opcion_menu == "3":
        #-----------------# seleccion de personaje#------------------#
        Limpiar()
        print("Elige tu personaje:")
        for key, p in personajes.items(): #Con for se itera sobre el diccionario personajes, donde key es la clave y p es el valor (que es otro diccionario). 
            print(f"{key}. {p['nombre']} - Vida: {p['Vida']} - Ataque: {p['ataque']} - Especial: {p['especial']} - Defensa: {p['defensa']}")
    
        eleccion = input("Selecciona el numero de tu personaje: ") #Se crea una variable eleccion que almacena la entrada del usuario.
        while eleccion not in personajes: #Se crea un bucle while que se ejecuta mientras la eleccion no este en el diccionario personajes.
            eleccion = input("Opcion invalidad. Por favor elige unos de los personajes que se muestran en la pantalla.")

        jugador = personajes[eleccion].copy() #Se crea una variable jugador que almacena el personaje elegido por el usuario, usando el metodo copy() para crear una copia del diccionario. Nota: el metodo copy() se usa para evitar que los cambios en el diccionario original afecten a la copia.

        #--------------#eleccion CPU#------------------#
        lista_valores = list(personajes.values()) #Se crea una lista llamada lista_valores que contiene los valores del diccionario personajes. Esto se hace para poder elegir un enemigo aleatorio de la lista de personajes.
        enemigo = random.choice(lista_valores).copy() #Se crea una variable enemigo que almacena un personaje aleatorio de la lista de valores, usando el metodo copy() para crear una copia del diccionario.
        while enemigo["nombre"] == jugador["nombre"]: #Se crea un bucle while que se ejecuta mientras el nombre del enemigo sea igual al nombre del jugador. Esto se hace para evitar que el jugador se enfrente a si mismo.
            enemigo = random.choice(lista_valores).copy()

        turno = 0 #Se crea una variable turno que almacena el turno actual del juego. Se inicializa en 0 para indicar que es el primer turno.
        #------------------#variables de ataque especial para el jugador y la CPU#------------------#
        puede_usar_ataque_especial = True #Se crea una variable puede_usar_ataque_especial que almacena si el jugador puede usar su ataque especial. Se inicializa en True para indicar que el jugador puede usar su ataque especial en el primer turno.
        puede_cpu_usar_ataque_especial = True #Se crea una variable puede_cpu_usar_ataque_especial que almacena si el enemigo puede usar su ataque especial. Se inicializa en True para indicar que el enemigo puede usar su ataque especial en el primer turno.

        #------------------#COMBATE#------------------#
        while jugador["Vida"] > 0 and enemigo["Vida"] > 0: #Se crea un bucle while que se ejecuta mientras la vida del jugador y la vida del enemigo sean mayores a 0. Esto indica que el combate continua mientras ambos personajes tengan vida.
            Limpiar()
            print(f"Tú: {jugador['nombre']} - Vida: {jugador['Vida']}")
            print(f"CPU: {enemigo['nombre']} - Vida: {enemigo['Vida']}") #Se imprime la vida del jugador y la vida del enemigo en la pantalla.
            print("""
            Elige tu siguiente movimiento: """)
            print("1. Atacar")
            if puede_usar_ataque_especial: #Se verifica si el jugador puede usar su ataque especial. Si es asi, se imprime la opcion de ataque especial en la pantalla.
                print("2. Ataque especial (Disponible)")
            else:
                print("2. Ataque especial (No disponible)")
            print("3. Defenderse")

            accion = input("movimiento: ") #Se crea una variable accion que almacena la entrada del usuario. Esta variable se usa para determinar que accion va a realizar el jugador en su turno.

            #------------------#ataque normal#------------------#
            if accion == "1":
                daño = random.randint(jugador["ataque"] - 5, jugador["ataque"] + 5) #Se crea una variable daño que almacena un numero aleatorio entre el ataque del jugador menos 5 y el ataque del jugador mas 5. Esto se hace para simular la variabilidad en el daño que el jugador puede hacer al enemigo.
                enemigo["Vida"] -= daño #al enemigo se le resta el daño que le ha hecho el jugador.
                print(f"""Has atacado a {enemigo['nombre']} y le has hecho {daño} de daño.""") #Se imprime en la pantalla el daño que el jugador le ha hecho al enemigo.
        
            #------------------#ataque especial#------------------#
            elif accion == "2":
                if puede_usar_ataque_especial: #Se verifica si el jugador puede usar su ataque especial.
                    daño = random.randint(jugador["especial"] - 10, jugador["especial"] + 10) #se crea una variable daño que almacena un numero aleatorio entre el ataque especial del jugador menos 10 y el ataque especial del jugador mas 10. Esto se hace para simular la variabilidad en el daño que el jugador puede hacer al enemigo.
                    enemigo["Vida"] -= daño #al enemigo se le resta el daño que le ha hecho el jugador.
                    puede_usar_ataque_especial = False #Se establece la variable puede_usar_ataque_especial en False para indicar que el jugador no puede usar su ataque especial en el siguiente turno.
                    print(f"""Has usado tu ataque especial contra {enemigo['nombre']} y le has hecho {daño} de daño.""")
                else:
                    print("""No puedes usar tu ataque especial en este turno.""")
                    time.sleep(1) #Se espera 1 segundo antes de continuar con el siguiente turno.
                    continue #se una la instruccion continue para saltar al siguiente turno sin ejecutar el resto del codigo.
            #------------------#defenderse#------------------#
            elif accion == "3":
                print(f"""Te has defendido y has reducido el daño recibido en este turno.""")
                jugador["defensa"] += 5 #Se aumenta la defensa del jugador en 5 puntos. Esto se hace para simular que el jugador se ha defendido y ha reducido el daño recibido en este turno.
            else:
                print("""Opcion no valida. Por favor, elige una opcion del menu.""")
                time.sleep(1)
                continue     
            
            #------------------#turno de la CPU#------------------#
            if enemigo["Vida"] > 0: #Se verifica si la vida del enemigo es mayor a 0. Si es asi, se procede a realizar el turno de la CPU.
                accion_cpu = random.choice(["atacar", "especial", "defender"]) #Se crea una variable accion_cpu que almacena una accion aleatoria entre atacar, especial y defender. Esto se hace para simular el comportamiento aleatorio de la CPU.

                if accion_cpu == "especial": #Se verifica si la accion aleatoria es especial.
                    daño_cpu = random.randint(enemigo["especial"] - 10, enemigo["especial"] + 10) #Se crea una variable daño_cpu que almacena un numero aleatorio entre el ataque especial del enemigo menos 10 y el ataque especial del enemigo mas 10. Esto se hace para simular la variabilidad en el daño que el enemigo puede hacer al jugador.
                    daño_final = max(0, daño_cpu - jugador["defensa"]) #Se crea una variable daño_final que almacena el daño final que le hace el enemigo al jugador. Se usa la funcion max para asegurarse de que el daño final no sea negativo. Esto se hace para simular que el jugador se ha defendido y ha reducido el daño recibido en este turno.
                    jugador["Vida"] -= daño_final #al jugador se le resta el daño final que le ha hecho el enemigo.
                    print(f"""{enemigo['nombre']} ha usado su ataque especial y te ha hecho {daño_final} de daño.""")  #Se imprime en la pantalla el daño que el enemigo le ha hecho al jugador.
 
                else: #Si la accion aleatoria no es especial, se verifica si la accion aleatoria es defender.
                    daño_cpu = random.randint(enemigo["ataque"] - 5, enemigo["ataque"] + 5) #Se crea una variable daño_cpu que almacena un numero aleatorio entre el ataque del enemigo menos 5 y el ataque del enemigo mas 5. Esto se hace para simular la variabilidad en el daño que el enemigo puede hacer al jugador.
                    daño_final = max(0, daño_cpu - jugador["defensa"])# #Se crea una variable daño_final que almacena el daño final que le hace el enemigo al jugador. Se usa la funcion max para asegurarse de que el daño final no sea negativo. Esto se hace para simular que el jugador se ha defendido y ha reducido el daño recibido en este turno. 
                    jugador["Vida"] -= daño_final #al jugador se le resta el daño final que le ha hecho el enemigo.
                    print(f"""{enemigo['nombre']} te ha atacado y te ha hecho {daño_final} de daño.""")
            
            #------------------#control del turno para ataque especial#------------------#
            turno += 1 #Se aumenta el turno en 1 para indicar que ha pasado un turno.
            if turno % 2 == 0: #Se verifica si el turno es par. Si es asi, se permite que el jugador y la CPU puedan usar su ataque especial en el siguiente turno.
                puede_usar_ataque_especial = True #Se establece la variable puede_usar_ataque_especial en True para indicar que el jugador puede usar su ataque especial en el siguiente turno.
                puede_cpu_usar_ataque_especial = True #Se establece la variable puede_cpu_usar_ataque_especial en True para indicar que el enemigo puede usar su ataque especial en el siguiente turno.
                
            time.sleep(5)
    
        #------------------resultado del combate#------------------#
        Limpiar()
        if jugador["Vida"] > 0:
            print(f"""Has ganado el combate contra {enemigo['nombre']}!
            Fin del juego.""")
            input("Presiona Enter para volver al menu.") #Se espera a que el usuario presione Enter para volver al menu principal del juego.
        else:
            print(f"""Has perdido el combate contra {enemigo['nombre']}!""")
            print("""1. Volver a jugar""")
            print("2. Volver al menu principal")
            opcion_post_juego = input("Elige una opcion: ") #Se crea una variable opcion_post_juego que almacena la entrada del usuario. Esta variable se usa para determinar que accion va a realizar el jugador despues de perder el combate.
            if opcion_post_juego == "1": #Se verifica si la opcion elegida es volver a jugar.
                continue
            elif opcion_post_juego == "2": #Se verifica si la opcion elegida es volver al menu principal.
                break
            else:
                print("Opcion no valida. Por favor, elige una opcion del menu.")
                time.sleep(2)
    #------------------Salida del juego#------------------#
    elif opcion_menu == "4":
        Limpiar()
        print("!Gracias por jugar!")
        print("Creado por: Gabriel Rivero - 2025")
        break
        
    else:
        Limpiar()
        print("Opcion no valida. Por favor, elige una opcion del menu.")
        time.sleep(2)
        Limpiar()

    
