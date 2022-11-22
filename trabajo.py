L_usuarios = []
ListaContraseñas = []
Cuentabancaria = []
class registro_usuario():
    def registro_usuario(self):
        usuario = input("DIGITE SU USUARIO:  ")
        usuario=input("DIGITE EL APELLIDO: ")
        self.edad=int(input("DIGITE LA EDAD: "))
        if self.edad < 18: 
         print("DEBES SER MAYOR DE EDAD PARA CREAR UNA CUENTA BANCARIA...")
         exit()
        usuario=input("DIGITE LA CEDULA: ")
        
        if usuario in L_usuarios:
            contraseña = int(input("DIGITE LA CONTRASEÑA: "))
            if contraseña in ListaContraseñas:
                print("--------------")
                print("SESION ABIERTA")
                print("--------------")
            else:
                print("---------------------")
                print("CONTRASEÑA INCORRECTA ")
                print("INTRUSOOOOO")
                print("---------------------")
                self.registro_usuario()
        else:
            print("---------------------")
            print("USUARIO NO REGISTRADO ")
            print("---------------------")
            self.registro_usuario()
            
class Registro:
    def registro(self):
        self.usuarios = input("DIGITE EL NOMBRE DE USUARIO POR FAVOR:  ")
        self.usuarios = input("DIGITE EL APELLIDO POR FAVOR: ")
        self.edad=int(input("DIGITE LA EDAD POR FAVOR: "))
        if self.edad < 18: 
            print("Debes tener la edad suficiente para poder tener una cuenta bancaria")
            exit()
        self.usuarios = input("DIGITE LA CEDULA POR FAVOR: ")
        if self.usuarios in (L_usuarios):
            print("---------------------")
            print("USUARIO NO ENCONTRADO ")
            print("---------------------")
            self.registro()
        else:
            self.contraseñas = int(input("DIGITE SU CONTRASEÑA POR FAVOR: "))
            print("--------------")
            print("SU CUENTA BANCARIA HA SIDO CREADA")
            print("--------------")
            L_usuarios.append(self.usuarios)
            ListaContraseñas.append(self.contraseñas)
            self.__init__()
class Inicio(Registro,registro_usuario):
    def __init__(self):
        print("1 = REGISTRO DE NUEVO USUARIO ")
        print("2 =  INICIAR SESION  ")
        print("3 = SALIR ")
        opcion = int(input("DIGITE LA OPCION DESEADA:  "))
        if opcion == 2:
            super(Inicio,self).registro_usuario()
        if opcion == 1:
            super(Inicio,self).registro()
        if opcion == 3:
            exit()
class Movimientos(Inicio):
    def __init__(self):
        super().__init__()
        self.MenuPrincipal()
    def MenuPrincipal(self):
        print("1 = CREAR CUENTA BANCOLOMBIA ")
        print("2 = VER Y HACER MOVIMIENTOS")
        print("3 = SALIR")
        opcion = int(input("DIGITE LA OPCION DESEADA:  "))
        if opcion == 1:
            self.CrearCuenta()
        if opcion == 2:
            self.MenuSecundario()
        if opcion == 3:
            self.__init__()
            Cuentabancaria.clear()
    def CrearCuenta(self):
        print("PARA CREAR SU CUENTA DIGITE 1 , PARA SALIR DIGITE 2 ")
        print("1 = CREAR CUENTA")
        desicion = int(input("DIGITE LA OPCION 1 PARA LA CREACION DE LA CUENTA:  "))
        if desicion == 1:
            print("LA CUENTA BANCARIA HA SIDO CREADA...")
            saldo = float(input("DIGITE EL MONTO DEL PRIMER DEPOSITO:  "))
            Cuentabancaria.append(saldo)
            print("MONTO DEPOSITADO CON EXITO ")
            self.MenuPrincipal()
        else:
            print("ERROR ")
            self.MenuPrincipal()
    def MostrarCuenta(self):
        print("1 = CUENTA BANCARIA ")
        opcion = int(input("DIGITE LA OPCION DESEADA: "))
        if opcion == 1:
            print("EL SALDO TOTAL DE LA CUENTA ES : $ ",sum(Cuentabancaria))
        else:
            print("ERROR ")
            self.MenuPrincipal
    def MenuSecundario (self):
        print("1 = DEPOSITAR DINERO A TU CUENTA ")
        print("2 = VER SALDO ACTUAL ")
        print("3 = RETIRAR SALDO")
        print("4 = REGRESAR AL MENU")
        opcion = int(input("DIGITE LA OPCION DESEADA: "))
        if opcion == 1:
            opcion = int(input("SELECCIONE LA OPCION 1 PARA CONTINUAR, 2 PARA VOLVER AL MENU PRINCIAPAL: "))
            if opcion == 1:
                saldo = float(input("INGRESE EL MONTO A DEPOSITAR:"))
                Cuentabancaria.append(saldo)
                self.MenuPrincipal()
            else:
                print("-----------")
                print("SALIENDO... ")
                print("-----------")
                self.MenuPrincipal()
        if opcion == 2:
            print("1 = CUENTA BANCARIA ")
            opcion = int(input("DIGITE LA OPCION 1 PARA SELECCIONAR SU CUENTA, 2 PARA VOLVER AL MENU DE INICIO: "))
            if opcion == 1:
                print("EL SALDO TOTAL ES DE : $ ",sum(Cuentabancaria))
                self.MenuPrincipal()
            else:
                print("-----------")
                print("SALIENDO... ")
                print("-----------")
                self.MenuPrincipal()
        if opcion == 3:
            TotaldelaCuenta = sum(Cuentabancaria)
            seleccion = int(input("DIGITE LA OPCION 1 PARA SELECCIONAR SU CUENTA, 2 PARA VOVER AL MENU DE INICIO:  "))
            if seleccion == 1:
                print("CUENTA BANCARIA SELECCIONADA ")
                print("SALDO ACTUAL: ",Cuentabancaria)
                dineroretirado = int(input("DIGITE LA CANTIDAD DE DINERO A RETIRAR: "))
                if dineroretirado < TotaldelaCuenta:
                    print("RETIRO REALIZADO ")
                    DineroRestante = dineroretirado - TotaldelaCuenta
                    Cuentabancaria.clear()
                    Cuentabancaria.append(DineroRestante)
                    print("EL NUEVO SALDO ES DE: ", Cuentabancaria)
                    self.MenuPrincipal()
                if dineroretirado > TotaldelaCuenta:
                    print("--------------------------------")
                    print("ERROR ")
                    print("DINERO INSUFICIENTE EN SU CUENTA")
                    print("--------------------------------")
                    self.MenuPrincipal()
        if opcion == 4:
            self.MenuPrincipal()
Movimientos()
registro_usuario()
Inicio()
