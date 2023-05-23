import bcrypt as bc


class DataHelper:
    def __init__(self):
        self.filepath='users.txt'

    def matchUserPass(self, user, password):
        with open (self.filepath, "r") as f: 
            for line in f.readlines():

                usuario = line.split(',')[0]
                contra = line.split(',')[1].rstrip()
                
                if user  == line.split(',')[0]: 
                    if bc.checkpw(password.encode('utf-8'), contra.encode('utf-8')): 
                        return usuario, contra
                    else:
                        return usuario, None
            return None, None     


    def matchUser(self, user):
        with open (self.filepath, "r") as f: 
            for line in f.readlines():
                if user  == line.split(',')[0]: 
                        return line.split(',')[0]
            return None    
    

    def saveUser(self, usuarioNuevo, contraseñaNueva):
        entrada = usuarioNuevo + ',' + contraseñaNueva.decode('utf-8')
        with open (self.filepath, "a") as f:
            f.write(entrada + '\n')
        return



    def modifyPassword(self, user, contraNueva):
        with open (self.filepath, "r+") as f: 
            for line in f.readlines():

                userGuardado = line.split(',')[0]
                contraGuardada = line.split(',')[1].rstrip()

                if user  == userGuardado: 
                    f.seek(0)
                    contenidoArchivo = f.read()
                    contenidoActualizado = contenidoArchivo.replace(contraGuardada, contraNueva.decode('utf-8'))
                    f.seek(0)
                    f.write(contenidoActualizado)
                    return None
            return 1


























































# import bcrypt as bc


# class DataHelper:
#     def __init__(self):
#         self.filepath='users.txt'

#     def matchUserPass(self, user, password):
#         with open (self.filepath, "r") as f: # es el modo de apertura del archivo ("r" para lectura, "w" para escritura, "a" para agregar, entre otros)
#             for line in f.readlines():

#                 contra = line.split(',')[1].rstrip()

#                 if user  == line.split(',')[0]: #.split separa las lineas de texto, en este caso el separados seria la coma
#                     if bc.checkpw(password.encode('utf-8'), contra.encode('utf-8')): #rstrip elimina los espacios
#                         return line.split(',')[0], line.split(',')[1].rstrip()
#                     else:
#                         return line.split(',')[0], None
#             return None, None     


#     def matchUser(self, user):
#         with open (self.filepath, "r") as f: # es el modo de apertura del archivo ("r" para lectura, "w" para escritura, "a" para agregar, entre otros)
#             for line in f.readlines():
#                 if user  == line.split(',')[0]: #.split separa las lineas de texto, en este caso el separados seria la coma
#                         return line.split(',')[0]
#             return None    
    

#     def saveUser(self, usuarioNuevo, contraseñaNueva):
#         entrada = usuarioNuevo + ',' + contraseñaNueva.decode('utf-8')
#         with open (self.filepath, "a") as f:
#             f.write(entrada + '\n')
#         print('Los datos han sido guardados en el archivo')


#     def modifyPassword(self, user, contraNueva):
#         with open (self.filepath, "r") as f: # es el modo de apertura del archivo ("r" para lectura, "w" para escritura, "a" para agregar, entre otros)
#             for line in f.readlines():

#                 userGuardado = line.split(',')[0]
#                 contraGuardada = line.split(',')[1].rstrip()

#                 if user  == userGuardado: #.split separa las lineas de texto, en este caso el separados seria la coma
#                     contenidoArchivo = f.read()
#                     contenidoArchivo.replace(contraGuardada, contraNueva)
#                     return None
#                 else: 
#                     return 1

