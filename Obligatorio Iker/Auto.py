class Auto:
    def __init__(self, modelo, año, score):
        self.modelo = modelo
        self.año = año
        self.score = score

    def validar_score(score):
        try:
            score = int(score)
            return 1 <= score <= 99
        except ValueError:
            return False

autos_registrados = []

def auto_existe(modelo, autos_registrados):
    return any(auto.modelo == modelo for auto in autos_registrados)

def alta_auto(autos_registrados):
    modelo = input("Ingrese el modelo del auto: ")
    if auto_existe(modelo, autos_registrados):
        print("ERROR: Un auto con ese modelo ya existe.")
        return None

    año = input("Ingrese el año del auto: ")
    while not año.isdigit() or int(año) < 1900 or int(año) > 2023:
        print("ERROR: Año inválido. Ingrese un año razonable.")
        año = input("Ingrese el año del auto: ")

    score = input("Ingrese el score del auto (1-99): ")
    while not Auto.validar_score(score):
        print("ERROR: Score inválido. Debe ser un número entre 1 y 99.")
        score = input("Ingrese el score del auto (1-99): ")

    nuevo_auto = Auto(modelo, año, score)
    autos_registrados.append(nuevo_auto)

    print('\nAuto registrado con éxito:')
    print(f'Modelo: {nuevo_auto.modelo}')
    print(f'Año: {nuevo_auto.año}')
    print(f'Score: {nuevo_auto.score}')

    return nuevo_auto