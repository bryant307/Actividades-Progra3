class Vehiculo:
    def __init__(self, marca, modelo, year, color, tipo_combustible, transmision, precio_compra, origen, cilindraje, tipo_carroceria):
        self.__ruedas = 4
        self.__capacidad_pasajeros = 5
        self.__marca = marca
        self.__modelo = modelo
        self.__year = year
        self.__color = color
        self.__tipo_combustible = tipo_combustible
        self.__transmision = transmision  
        self.__precio_compra = precio_compra
        self.__origen = origen  
        self.__cilindraje = cilindraje 
        self.__tipo_carroceria = tipo_carroceria  
        self.__precio_venta = self.calcular_precio_venta() #metodo para calcular precio de venta

    # Métodopara calcular el precio de venta
    def calcular_precio_venta(self):
        return self.__precio_compra * 1.4

    # Método para mostrar la información del auto
    def mostrar_informacion(self):
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")
        print(f"Año: {self.__year}")
        print(f"Color: {self.__color}")
        print(f"Tipo de Combustible: {self.__tipo_combustible}")
        print(f"Transmisión: {self.__transmision}")
        print(f"Precio de Compra: ${self.__precio_compra:.2f}")
        print(f"Precio de Venta: ${self.__precio_venta:.2f}")
        print(f"Origen: {self.__origen}")
        print(f"Cilindraje: {self.__cilindraje}")
        print(f"Tipo de Carrocería: {self.__tipo_carroceria}")
        print(f"Número de Ruedas: {self.__ruedas}")
        print(f"Capacidad de Pasajeros: {self.__capacidad_pasajeros}")
        print()


vehiculo1 = Vehiculo(
    marca="Toyota",
    modelo="Corolla",
    year=2022,
    color="Blanco",
    tipo_combustible="Gasolina",
    transmision="Automática",
    precio_compra=20000,
    origen="Nacional",
    cilindraje="1.8L",
    tipo_carroceria="Sedán"
)

vehiculo2 = Vehiculo(
    marca="Ford",
    modelo="Explorer",
    year=2023,
    color="Negro",
    tipo_combustible="Gasolina",
    transmision="Manual",
    precio_compra=35000,
    origen="Importado",
    cilindraje="3.0L",
    tipo_carroceria="SUV"
)


# Mostrar la información de los autos
print("Información de los autos:")
vehiculo1.mostrar_informacion()
vehiculo2.mostrar_informacion()

vehiculo3 = Vehiculo(
    marca= input("Introduce la marca: "),
    modelo= input("Introduce el modelo: "),
    year= int(input("Introduce el año")),
    color= input("Que color es: "),
    tipo_combustible= input("Que tipo de combustible usa?"),
    transmision= input("Tipo de transmision: "),
    precio_compra= int(input("Precio: ")),
    origen= input("Origen:"),
    cilindraje= input("Cilindraje:"),
    tipo_carroceria= input("Carroceria:"),

)
vehiculo3.mostrar_informacion()