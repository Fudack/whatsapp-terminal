import os
import time


def iniciar_conexion():
    opciones = {1: iniciar_conexion, 2: leer_ultimo_mensaje, 3: mensaje_por_contacto, 4: responder_mensaje}
    while True:
        os.system("node ../api/whatsapp_api.js")
        menu()
        seleccion = int(input("Ingrese su elección: "))

        if seleccion == 0:
            print("Adiós")
            time.sleep(2)
            os.system("clear")
            break

        opcion = opciones.get(seleccion)
        if opcion:
            os.system("clear")
            opcion()
        else:
            os.system("clear")
            print("Opción inválida")


def leer_ultimo_mensaje():
    print("Leer último mensaje")


def mensaje_por_contacto():
    print("Mensajes por contacto")


def responder_mensaje():
    print("Responder mensaje")


def menu():
    print("****************************")
    print("* Selecciona una opción    *")
    print("* 1. Iniciar conexión      *")
    print("* 2. Leer último mensaje   *")
    print("* 3. Mensajes por contacto *")
    print("* 4. Responder mensaje     *")
    print("* 0. Salir                 *")
    print("****************************")


opciones = {1: iniciar_conexion, 2: leer_ultimo_mensaje, 3: mensaje_por_contacto, 4: responder_mensaje}

while True:
    menu()
    seleccion = int(input("Ingrese su elección: "))

    if seleccion == 0:
        print("Adiós")
        time.sleep(2)
        os.system("clear")
        break

    opcion = opciones.get(seleccion)
    if opcion:
        os.system("clear")
        opcion()
    else:
        os.system("clear")
        print("Opción inválida")
