print("---EJERCICIO 4---")

'''Elegimos este metodo (POO) porque organiza bien la información de los animales y hace que sea fácil 
gestionar el zoológico. La interfaz simple nos permite agregar animales y ver los que están en tratamiento 
de forma rápida y clara'''

# Clase para representar un animal
class Animal:
    def __init__(self, nombre, especie, area, en_tratamiento=False, dosis=None, frecuencia=None):
        self.nombre = nombre
        self.especie = especie
        self.area = area
        self.en_tratamiento = en_tratamiento
        self.dosis = dosis
        self.frecuencia = frecuencia

    def __str__(self):
        tratamiento = f"En tratamiento: Dosis - {self.dosis}, Frecuencia - {self.frecuencia}" if self.en_tratamiento else "Saludable"
        return f"{self.nombre} ({self.especie}), Área: {self.area}, {tratamiento}"

# Clase para la gestión del zoológico
class Zoologico:
    def __init__(self):
        self.animales = []

    def agregar_animal(self, nombre, especie, area, en_tratamiento=False, dosis=None, frecuencia=None):
        # Verificar si el animal ya existe en el zoológico
        for animal in self.animales:
            if animal.nombre == nombre and animal.especie == especie:
                # Actualizar la información del animal existente
                animal.area = area
                animal.en_tratamiento = en_tratamiento
                animal.dosis = dosis
                animal.frecuencia = frecuencia
                return
        
        # Si el animal no existe, agregar uno nuevo
        nuevo_animal = Animal(nombre, especie, area, en_tratamiento, dosis, frecuencia)
        self.animales.append(nuevo_animal)

    def listar_animales(self):
        for animal in self.animales:
            print(animal)

    def listar_animales_en_tratamiento(self):
        for animal in self.animales:
            if animal.en_tratamiento:
                print(animal)

# Función para agregar un animal interactivamente
def agregar_animal_interactivo(zoo):
    print("\n--- Registro de Animal ---")
    nombre = input("Ingrese el nombre del animal: ")
    especie = input("Ingrese la especie del animal: ")
    area = input("Ingrese el área del zoológico donde se encuentra el animal: ")
    
    en_tratamiento = input("¿El animal está en tratamiento? (sí/no): ").strip().lower() == "sí"
    
    dosis = None
    frecuencia = None
    if en_tratamiento:
        dosis = input("Ingrese la dosis del tratamiento: ")
        frecuencia = input("Ingrese la frecuencia del tratamiento: ")
    
    zoo.agregar_animal(nombre, especie, area, en_tratamiento, dosis, frecuencia)

# Uso del sistema de zoológico
zoo = Zoologico()
# Agregar algunos animales iniciales
zoo.agregar_animal("Simba", "León", "Área de felinos")
zoo.agregar_animal("Manny", "Elefante", "Área de grandes herbívoros", True, "50mg", "Cada 12 horas")

# Opciones para el usuario
while True:
    print("\nSeleccione una opción:")
    print("1. Registrar nuevo animal")
    print("2. Listar todos los animales")
    print("3. Listar animales en tratamiento")
    print("4. Salir")
    
    opcion = input("Ingrese el número de la opción deseada: ")
    
    if opcion == "1":
        agregar_animal_interactivo(zoo)
    elif opcion == "2":
        zoo.listar_animales()
    elif opcion == "3":
        zoo.listar_animales_en_tratamiento()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
