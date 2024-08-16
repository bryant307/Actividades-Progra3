class Veterinaria:
    def __init__(self, nombre, raza, edad, peso, color, propietario, direccion):
        # Atributos privados
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__color = color
        self.__propietario = propietario
        self.__direccion = direccion
        self.__estado = "NO ATENDIDO"
        self.__clasificacion = None
        
        # Clasificación del perro según su peso
        self.clasificar_perro()
        # Cambio de estado a "ATENDIDO"
        self.cambiar_estado_a_atendido()

   
    def clasificar_perro(self):
        if self.__peso < 10:
            self.__clasificacion = "Perro Pequeño"
        else:
            self.__clasificacion = "Perro Grande"

    def cambiar_estado_a_atendido(self):
        self.__estado = "ATENDIDO"

    # Funcion para obtener la información
    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Raza: {self.__raza}")
        print(f"Edad: {self.__edad} años")
        print(f"Peso: {self.__peso} kg")
        print(f"Color: {self.__color}")
        print(f"Propietario: {self.__propietario}")
        print(f"Dirección: {self.__direccion}")
        print(f"Estado: {self.__estado}")
        print(f"Clasificación: {self.__clasificacion}")

# Ingreso de datos
perro1 = Veterinaria(
    nombre="Rex",
    raza="Labrador",
    edad=5,
    peso=12,
    color="Negro",
    propietario="Juan Pérez",
    direccion="Calle 123, Ciudad"
)

perro1.mostrar_informacion()


#Aqui introduciremos datos
nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
edad = int(input("Ingrese la edad del perro (en años): "))
peso = float(input("Ingrese el peso del perro (en kg): "))
color = input("Ingrese el color del perro: ")
propietario = input("Ingrese el nombre del propietario: ")
direccion = input("Ingrese la dirección del propietario: ")

perro2 = Veterinaria(
    nombre=nombre,
    raza=raza,
    edad=edad,
    peso=peso,
    color=color,
    propietario=propietario,
    direccion=direccion
)

# Mostrar la información del perro
perro2.mostrar_informacion()