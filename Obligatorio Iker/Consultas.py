def top_10_pilotos(pilotos_registrados):
    pilotos_ordenados = sorted(pilotos_registrados, key=lambda x: x.puntaje_campeonato, reverse=True)
    return pilotos_ordenados[:10]

def resumen_campeonato_constructores(equipos_registrados):
    resumen = {}
    for equipo in equipos_registrados:
        resumen[equipo.nombre] = sum(piloto.puntaje_campeonato for piloto in equipo.pilotos)
    return sorted(resumen.items(), key=lambda x: x[1], reverse=True)

def top_5_pilotos_mejor_pagados(pilotos_registrados):
    pilotos_ordenados = sorted(pilotos_registrados, key=lambda x: x.salario, reverse=True)
    return pilotos_ordenados[:5]

def top_3_pilotos_mas_habiles(pilotos_registrados):
    pilotos_ordenados = sorted(pilotos_registrados, key=lambda x: x.score, reverse=True)
    return pilotos_ordenados[:3]

def obtener_jefes_de_equipo(equipos_registrados):
    jefes = [(equipo.jefe, equipo.nombre) for equipo in equipos_registrados if equipo.jefe is not None]
    return sorted(jefes, key=lambda x: x[0].nombre)

def mostrar_submenu_consultas():
    print("Submenú de Consultas:")
    print("1. Top 10 pilotos con más puntos")
    print("2. Resumen campeonato de constructores")
    print("3. Top 5 pilotos mejores pagos")
    print("4. Top 3 pilotos más habilidosos")
    print("5. Jefes de equipo")
    print("")

def submenu_consultas(pilotos_registrados, equipos_registrados):
    while True:
        mostrar_submenu_consultas()
        opcion = input("Seleccione una opción del submenú o presione 'X' para salir: ")

        if opcion == "1":
            resultado = top_10_pilotos(pilotos_registrados)
            for piloto in resultado:
                print(f"{piloto.nombre} - Puntos: {piloto.puntaje_campeonato}")
        elif opcion == "2":
            resultado = resumen_campeonato_constructores(equipos_registrados)
            for equipo, puntos in resultado:
                print(f"Equipo: {equipo} - Puntos: {puntos}")
        elif opcion == "3":
            resultado = top_5_pilotos_mejor_pagados(pilotos_registrados)
            for piloto in resultado:
                print(f"{piloto.nombre} - Salario: {piloto.salario}")
        elif opcion == "4":
            resultado = top_3_pilotos_mas_habiles(pilotos_registrados)
            for piloto in resultado:
                print(f"{piloto.nombre} - Score: {piloto.score}")
        elif opcion == "5":
            resultado = obtener_jefes_de_equipo(equipos_registrados)
            for jefe, equipo in resultado:
                print(f"Jefe de equipo: {jefe.nombre} - Equipo: {equipo}")
        elif opcion.lower() == 'x':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")