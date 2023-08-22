class Asiento:
    def __init__(self,color:str,precio:int,registro:int):
        self.color = color
        self.precio = precio
        self.registro = registro
    def cambiarColor(self, color:str):
        if color =="rojo" or color =="blanco" or color =="amarillo" or color =="verde" or color =="negro":
            self.color = color

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo:str,precio:int,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    def cantidadAsientos(self):
        cantidad = 0
        for j in range( len(self.asientos)):
            if self.asientos[j] is not None:
                cantidad +=1
        return cantidad

    def verificarIntegridad(self):
        asientos = self.cantidadAsientos()
        for i in range(asientos-1):
            if self.asientos[i] is not None:
                if (self.asientos[i].registro!=self.registro):
                    return "Las piezas no son originales"
            if self.motor.registro != self.registro:
                return "Las piezas no son originales"
            else:
                return "Auto original"



class Motor:
    def  __init__(self,numeroCilindros:int,tipo:str,registro:int):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro= registro
    def cambiarRegistro(self, registro:int):
        self.registro = registro

    def asignarTipo(self,tipo:str):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo = tipo

