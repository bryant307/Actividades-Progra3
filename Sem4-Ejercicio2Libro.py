class Cuaderno:
    def __init__(self, tipo_hojas, precio_compra):
        self.__marca = "HOJITA"  # Todos los cuadernos son de la marca HOJITA
        self.__tipo_hojas = tipo_hojas  # Puede ser de 50 o 100 hojas
        self.__precio_compra = precio_compra
        self.__precio_venta = self.calcular_precio_venta()
    
    def calcular_precio_venta(self):
        # El precio de venta es igual al precio de compra multiplicado por 1.30
        return self.__precio_compra * 1.30
    
    def mostrar_informacion(self):
        print(f"Cuaderno marca: {self.__marca}")
        print(f"Tipo de hojas: {self.__tipo_hojas} hojas")
        print(f"Precio de compra: ${self.__precio_compra:.2f}")
        print(f"Precio de venta: ${self.__precio_venta:.2f}")
        print()

class Lapiz:
    def __init__(self, tipo, precio_compra):
        self.__marca = "RAYAS"  # Todos los lápices son de la marca RAYAS
        self.__tipo = tipo  # Puede ser de grafito o de colores
        self.__precio_compra = precio_compra
        self.__precio_venta = self.__calcular_precio_venta()
    
    def __calcular_precio_venta(self):
        # El precio de venta es igual al precio de compra multiplicado por 1.30
        return self.__precio_compra * 1.30
    
    def mostrar_informacion(self):
        print(f"Lápiz marca: {self.__marca}")
        print(f"Tipo: {self.__tipo}")
        print(f"Precio de compra: ${self.__precio_compra:.2f}")
        print(f"Precio de venta: ${self.__precio_venta:.2f}")
        print()

# Ejemplo de uso
# Registro de dos cuadernos
cuaderno1 = Cuaderno(tipo_hojas=50, precio_compra=1.50)
cuaderno2 = Cuaderno(tipo_hojas=100, precio_compra=2.00)

# Registro de dos lápices
lapiz1 = Lapiz(tipo="Grafito", precio_compra=0.50)
lapiz2 = Lapiz(tipo="Colores", precio_compra=0.75)

# Mostrar la información de los cuadernos
print("Información de los cuadernos:")
cuaderno1.mostrar_informacion()
cuaderno2.mostrar_informacion()

# Mostrar la información de los lápices
print("Información de los lápices:")
lapiz1.mostrar_informacion()
lapiz2.mostrar_informacion()
