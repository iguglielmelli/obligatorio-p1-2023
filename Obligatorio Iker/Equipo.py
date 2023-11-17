from Empleado import *
from Auto import *

Empleado, Piloto, Mecanico, JefeEquipo

class Equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pilotos = []  # Lista para almacenar pilotos
        self.mecanicos = []  # Lista para almacenar mecánicos
        self.jefe = None  # Jefe de equipo
        self.auto = None  # Auto del equipo

    def agregar_piloto(self, piloto):
        if len(self.pilotos) < 3:  # Dos pilotos titulares y uno de reserva
            self.pilotos.append(piloto)

    def agregar_mecanico(self, mecanico):
        if len(self.mecanicos) < 8:  # Al menos 8 mecánicos
            self.mecanicos.append(mecanico)

    def asignar_jefe(self, jefe):
        if self.jefe is None:
            self.jefe = jefe

    def asignar_auto(self, auto):
        if self.auto is None:
            self.auto = auto

def obtener_empleado_por_cedula(cedula_empleado, empleados_registrados):
    for empleado in empleados_registrados:
        if empleado.get_cedula() == cedula_empleado:
            return empleado
    return None

def alta_equipo(equipos_registrados, empleados_registrados, autos_registrados):
    nombre_equipo = input("Ingrese nombre del equipo: ")
    nuevo_equipo = Equipo(nombre_equipo)

    modelo_auto = input("Ingrese modelo de auto: ")
    auto = next((auto for auto in autos_registrados if auto.modelo == modelo_auto), None)
    if auto:
        nuevo_equipo.asignar_auto(auto)
    else:
        print("Auto no encontrado. Por favor, registre el auto primero.")
        return

    while len(nuevo_equipo.pilotos) < 3 or len(nuevo_equipo.mecanicos) < 8 or not nuevo_equipo.jefe:
        cedula_empleado = input("Ingrese cedula del empleado: ")
        empleado = obtener_empleado_por_cedula(cedula_empleado, empleados_registrados)

        if empleado:
            if isinstance(empleado, Piloto) and len(nuevo_equipo.pilotos) < 3:
                nuevo_equipo.agregar_piloto(empleado)
            elif isinstance(empleado, Mecanico) and len(nuevo_equipo.mecanicos) < 8:
                nuevo_equipo.agregar_mecanico(empleado)
            elif isinstance(empleado, JefeEquipo) and not nuevo_equipo.jefe:
                nuevo_equipo.asignar_jefe(empleado)
            else:
                print("Empleado no apto o ya se alcanzó el límite para este rol.")
        else:
            print("Empleado no encontrado.")

    equipos_registrados.append(nuevo_equipo)
    print(f"Equipo '{nombre_equipo}' creado con éxito.")