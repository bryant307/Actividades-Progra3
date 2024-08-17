class Almacen: #Clase Padre
    def __init__(self, tipo_dispositivo, modelo, almacenamiento, procesador, memoria_ram, precio_compra):
        self.__tipo_dispositivo = tipo_dispositivo
        self.__modelo = modelo
        self.__almacenamiento = almacenamiento
        self.__procesador = procesador
        self.__memoria_ram = memoria_ram
        self.__precio_compra = precio_compra
        self.__marca = "PHR"
        self.__precio_venta = self.calprecio_venta()

    def calprecio_venta(self): #Metodo para calcular precio de venta
        return self.__precio_compra * 1.7
        
    def detalle_producto(self): #Metodo para mostrar los datos
        print("INFORMACION DE DISPOSITIVO")
        print(f"Marca: {self.__marca}")
        print(f'Tipo de Dispositivo: {self.__tipo_dispositivo}')
        print(f'Modelo: {self.__modelo}')
        print(f'Almacenamiento: {self.__almacenamiento} GB')
        print(f'Procesador: {self.__procesador}')
        print(f'Memoria RAM: {self.__memoria_ram} GB')
        print(f'Precio de compra: ${self.__precio_compra}')
        print(f'Precio de venta: ${self.__precio_venta}')
        print()


ejemplo1 = Almacen( #Este es un dato de ejemplo
    tipo_dispositivo= "Computadora",
    modelo= "S23",
    almacenamiento= 256,
    procesador= "i7 Core",
    memoria_ram= 8,
    precio_compra= 500,

)

ejemplo1.detalle_producto()

#Aqui permite introducir valores y datos
datos1 = Almacen(
    tipo_dispositivo= input("Tipo de Dispositivo: "),
    modelo= input('Modelo: '),
    almacenamiento= int(input('Almacenamiento: ')),
    procesador= input('Procesador del dispositivo: '),
    memoria_ram= int(input("Capacidad de Memoria RAM: ")),
    precio_compra= int(input('Precio de Compra: ')),

)

datos1.detalle_producto()
