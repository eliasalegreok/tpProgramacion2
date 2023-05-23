from data.data_helper import DataHelper
import bcrypt as bc

class Verifier:
    def __init__(self,user,password):
        self.user = user
        self.password = password

    def VerificarDatosIngresados(self):
        
        if self.user == '':
            raise Exception( "Es obligatorio ingresar un usuario")
        if self.password == '':
            raise Exception("Es obligatorio ingresar una contraseña")

        self.password =self.password.lower() 


    def Verifymatch(self):

        myDataHelper = DataHelper()
        ruser, rpassword = myDataHelper.matchUserPass(self.user, self.password)
        
        if ruser is None:
            raise Exception("Usuario no encontrado")
        elif rpassword is None:
            raise Exception("Contraseña incorrecta")
        else:
            return 
       

    def VerificarUsuarioExistente(self):
        myDataHelper = DataHelper()
        ruser = myDataHelper.matchUser(self.user)
        
        if ruser is None:
            return
        else:
            raise Exception("El usuario ya esta en uso!")
  

    def guardarUsuarioNuevo(self):
        myDataHelper = DataHelper()
        self.password = bc.hashpw(self.password.encode('utf-8'),bc.gensalt())
        dev = myDataHelper.saveUser(self.user, self.password)
        return


    def modificarContraseña(self):
        
        myDataHelper = DataHelper()
        contraNueva = bc.hashpw(self.password.encode('utf-8'),bc.gensalt())
        modificar = myDataHelper.modifyPassword(self.user, contraNueva)

        if modificar is None:
            raise Exception("Su contraseña fue modificada.")
        else:
            raise Exception("Hubo un error.")


