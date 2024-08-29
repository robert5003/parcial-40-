'''El diseño del código sigue un enfoque orientado a objetos (POO), 
que permite modelar la situación del consultorio médico mediante clases, 
donde cada clase representa un elemento del sistema (paciente, secretaria, consultorio). '''

print("EJERCICIO 1")

import datetime
import random

class Paciente:
    def __init__(self, nombre, edad, motivo_consulta):
        self.nombre = nombre
        self.edad = edad
        self.motivo_consulta = motivo_consulta
        self.fecha_consulta = None  # Fecha de consulta inicialmente vacía

class Secretaria:
    def __init__(self):
        self.pacientes_registrados = {}  # Diccionario para almacenar pacientes por nombre
        self.sala_espera = []  # Lista para almacenar los nombres de pacientes en la sala de espera

    def registrar_paciente(self, nombre, edad=None, motivo_consulta=None):
        # Verificar si el paciente ya está registrado
        if nombre in self.pacientes_registrados:
            paciente = self.pacientes_registrados[nombre]
            print(f"Paciente {nombre} ya tiene una consulta previa.")
            self.verificar_fecha_consulta(paciente)
        else:
            nuevo_paciente = Paciente(nombre, edad, motivo_consulta)
            self.pacientes_registrados[nombre] = nuevo_paciente
            print(f"Paciente {nombre} registrado exitosamente.")
            self.asignar_fecha_consulta(nombre)

    def asignar_fecha_consulta(self, nombre):
        # Asignar una fecha ficticia de consulta
        fecha_actual = datetime.date.today()
        fecha_consulta = fecha_actual + datetime.timedelta(days=random.randint(1, 10))  # Consulta entre 1 y 10 días después
        self.pacientes_registrados[nombre].fecha_consulta = fecha_consulta
        print(f"Consulta asignada para {nombre} el día {fecha_consulta}.")

    def verificar_fecha_consulta(self, paciente):
        # Verificar si la fecha de consulta ya pasó
        fecha_actual = datetime.date.today()
        if paciente.fecha_consulta < fecha_actual:
            print(f"La fecha de consulta para {paciente.nombre} ya pasó. Enviando a sala de espera.")
            self.sala_espera.append(paciente.nombre)
        else:
            print(f"Datos del paciente {paciente.nombre}:")
            print(f"Nombre: {paciente.nombre}, Edad: {paciente.edad}, Motivo: {paciente.motivo_consulta}, Fecha de consulta: {paciente.fecha_consulta}\n")

    def mandar_paciente_sala_espera(self):
        # Seleccionar un paciente aleatorio cuya consulta ya haya expirado para mandar a la sala de espera
        candidatos = [paciente for paciente in self.pacientes_registrados.values() if paciente.fecha_consulta < datetime.date.today()]
        if candidatos:
            paciente_seleccionado = random.choice(candidatos)
            self.sala_espera.append(paciente_seleccionado.nombre)
            print(f"Paciente {paciente_seleccionado.nombre} ha sido enviado a la sala de espera debido a que su consulta ya expiró.")

    def mostrar_pacientes(self):
        # Mostrar los datos y fechas de consulta de todos los pacientes registrados
        print("\nPacientes registrados:")
        for paciente in self.pacientes_registrados.values():
            print(f"Nombre: {paciente.nombre}, Edad: {paciente.edad}, Motivo: {paciente.motivo_consulta}, Fecha de consulta: {paciente.fecha_consulta}")
        
        # Mostrar los pacientes en la sala de espera
        print("\nPacientes en sala de espera:")
        for nombre in self.sala_espera:
            print(f"{nombre}")

class Consultorio:
    def __init__(self):
        self.secretaria = Secretaria()

    def llegada_paciente(self):
        while True:
            # Pedir datos del paciente
            nombre = input("Ingrese el nombre del paciente: ")
            if nombre in self.secretaria.pacientes_registrados:
                print(f"Paciente {nombre} ya está registrado.")
                self.secretaria.verificar_fecha_consulta(self.secretaria.pacientes_registrados[nombre])
            else:
                edad = input("Ingrese la edad del paciente: ")
                motivo_consulta = input("Ingrese el motivo de consulta: ")
                self.secretaria.registrar_paciente(nombre, edad, motivo_consulta)

            # Preguntar si quiere registrar otro paciente
            continuar = input("¿Desea registrar otro paciente? (s/n): ")
            if continuar.lower() != 's':
                break

        # Enviar un paciente aleatorio a la sala de espera si su consulta ya expiró
        self.secretaria.mandar_paciente_sala_espera()

        # Mostrar todos los pacientes registrados y los que están en la sala de espera al finalizar
        self.secretaria.mostrar_pacientes()

# Ejecución de la simulación del consultorio
consultorio = Consultorio()
consultorio.llegada_paciente()
