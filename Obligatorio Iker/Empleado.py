class Empleado:
    def __init__(self, cedula, nombre, nacimiento, nacionalidad, salario):
        self.cedula = cedula
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.nacionalidad = nacionalidad
        self.salario = salario
    
    def get_cedula(self):
        return self.cedula
    
    @staticmethod
    def verificar_nombre(nombre):
        palabras = nombre.split()
        return len(palabras) == 2 and all(palabra.isalpha() for palabra in palabras)

    @staticmethod
    def verificar_cedula(cedula):
        return len(str(cedula)) == 8 and str(cedula).isdigit()

class Piloto(Empleado):
    def __init__(self, cedula, nombre, nacimiento, nacionalidad, salario, score, numero_auto, puntaje_campeonato=0, lesionado=False):
        super().__init__(cedula, nombre, nacimiento, nacionalidad, salario)
        self.score = score
        self.numero_auto = numero_auto
        self.puntaje_campeonato = puntaje_campeonato
        self.lesionado = lesionado

class Mecanico(Empleado):
    def __init__(self, cedula, nombre, nacimiento, nacionalidad, salario, score):
        super().__init__(cedula, nombre, nacimiento, nacionalidad, salario)
        self.score = score

class JefeEquipo(Empleado):
    def __init__(self, cedula, nombre, nacimiento, nacionalidad, salario):
        super().__init__(cedula, nombre, nacimiento, nacionalidad, salario)

def alta_empleado(empleados_registrados):
    nombre = input("Ingrese nombre y apellido del empleado: ")
    while not Empleado.verificar_nombre(nombre):
        nombre = input("ERROR: NOMBRE Y/O APELLIDO INVALIDO. Ingrese nombre y apellido del empleado: ")

    cedula = input("Ingrese cedula de identidad sin puntos ni guiones: ")
    while not Empleado.verificar_cedula(cedula):
        cedula = input("ERROR: CEDULA INVALIDA. Ingrese cedula de identidad valida (sin puntos ni guiones): ")

    if any(empleado.cedula == cedula for empleado in empleados_registrados):
        print("ERROR: EMPLEADO YA EXISTENTE.")
        return

    nacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
    nacionalidad = input("Ingrese la nacionalidad: ")
    salario = input("Ingrese salario del empleado: ")
    while not salario.isdigit():
        salario = input("ERROR: SALARIO INVALIDO. Ingrese salario del empleado: ")
    salario = int(salario)

    print("Seleccione un cargo para el empleado:")
    print("1-Piloto\n2-Piloto de reserva\n3-Mecánico\n4-Jefe de equipo")
    cargo = int(input("Opción: "))
    while cargo < 1 or cargo > 4:
        cargo = int(input("ERROR: CARGO INVALIDO. Opción: "))

    score = None
    numero_auto = None
    if cargo in [1, 2, 3]:  # Piloto, Piloto de reserva, Mecánico
        score = int(input("Ingrese score (1-99): "))
        while not 1 <= score <= 99:
            score = int(input("ERROR: Score invalido. Ingrese score (1-99): "))

    if cargo in [1, 2]:  # Piloto, Piloto de reserva
        numero_auto = input("Ingrese número de auto: ")

    empleado = None
    if cargo == 1 or cargo == 2:  # Piloto o Piloto de reserva
        empleado = Piloto(cedula, nombre, nacimiento, nacionalidad, salario, score, numero_auto)
    elif cargo == 3:  # Mecánico
        empleado = Mecanico(cedula, nombre, nacimiento, nacionalidad, salario, score)
    elif cargo == 4:  # Jefe de equipo
        empleado = JefeEquipo(cedula, nombre, nacimiento, nacionalidad, salario)

    empleados_registrados.append(empleado)
    print(f"\nEmpleado agregado exitosamente: {empleado.nombre}, Cédula: {empleado.cedula}")