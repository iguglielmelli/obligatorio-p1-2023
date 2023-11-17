from Empleado import alta_empleado, Empleado, Piloto, Mecanico, JefeEquipo
from Auto import alta_auto, Auto
from Equipo import alta_equipo, Equipo
from Simulacion import simular_carrera
from Consultas import submenu_consultas

empleados_registrados = []
autos_registrados = []
equipos_registrados = []

def mostrar_menu():
    print("")
    print("Menu:")
    print("1. Alta de empleado")
    print("2. Alta de auto")
    print("3. Alta de equipo")
    print("4. Simular carrera")
    print("5. Realizar consultas")
    print("6. Finalizar programa")
    print("")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\nALTA DE EMPLEADO\n")
            alta_empleado(empleados_registrados)

        elif opcion == "2":
            print("\nALTA DE AUTO\n")
            alta_auto(autos_registrados)
            
        elif opcion == "3":
            print("\nALTA DE EQUIPO\n")
            alta_equipo(equipos_registrados, empleados_registrados, autos_registrados)
            
        elif opcion == "4":
            print("\nSIMULACION DE CARRERA\n")
            simular_carrera(equipos_registrados)
            
        elif opcion == "5":
            print("\nREALIZAR CONSULTAS\n")
            submenu_consultas(empleados_registrados, equipos_registrados)
            
        elif opcion == "6":
            print("Finalizando el programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()