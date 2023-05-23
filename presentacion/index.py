from business.admin import Verifier
import getpass
import sys


class App:
    def __init__(self):
        self.user = ''
        self.password = ''



    def Run (self):
        print('Bienvenido')

        App.iniciarSesion(self)

        print('Elija una opcion:')
        print('[1] Crear un usuario nuevo')
        print('[2] Modificar contraseña')
        self.opcion = input('')

        if self.opcion == '1':
             App.crearUsuario()
        if self.opcion == '2':
             App.Modificar(self)
             


    def crearUsuario():
        usuarioNuevo = input('Por favor ingrese un nombre de usuario: ')
        contraseñaNueva = getpass.getpass('Ahora ingrese una contraseña: ')

        myVerifier = Verifier(usuarioNuevo , contraseñaNueva)

        try:
            dev = myVerifier.VerificarDatosIngresados()
            try:
                verificarUsuarioExistente = myVerifier.VerificarUsuarioExistente()
                print('Usuario disponible!')
                myVerifier.guardarUsuarioNuevo()
                print('Los datos han sido guardados en el archivo')
            except Exception as e:
                print(e.args[0])    
        except Exception as e:
                print(e.args[0])



    def iniciarSesion(self):
            self.user = input('Ingrese su nombre de usuario: ')
            self.password = getpass.getpass('Ingrese contraseña: ')

            myVerifier = Verifier(self.user , self.password)

            try:
                print ("\n")
                dev = myVerifier.VerificarDatosIngresados()   
            except Exception as e:
                 print(e.args[0])
                 sys.exit(1)

            try:
                dev = myVerifier.Verifymatch()
                print("Datos Correctos, Bienvenido!")
            except Exception as e:
                print(e.args[0])
                sys.exit(1)

                

    def Modificar(self):
        contraseñaNueva = getpass.getpass('Ingrese una contraseña nueva: ')

        if contraseñaNueva == "":
            print("Es obligatorio ingresar una contraseña")
            sys.exit(1)

        myVerifier = Verifier(self.user , contraseñaNueva)  

        try:
            myVerifier.modificarContraseña()
        except Exception as e:
            print(e.args[0])
