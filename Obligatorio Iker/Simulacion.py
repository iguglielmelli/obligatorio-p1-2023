def simular_carrera(equipos_registrados):
    lesionados = input("Ingrese nro de auto de todos los pilotos lesionados: ").split(',')
    abandonos = input("Ingrese nro auto de todos los pilotos que abandonan separado por coma: ").split(',')
    errores_pits = input("Ingrese nro de auto de todos los pilotos que cometen error en pits: ").split(',')
    penalidades = input("Ingrese nro de auto de todos los pilotos que reciben penalidad: ").split(',')

    resultados = []
    for equipo in equipos_registrados:
        for piloto in equipo.pilotos:
            # Verificar si el piloto está lesionado o abandona
            if piloto.numero_auto in lesionados or piloto.numero_auto in abandonos:
                continue

            # Calcular score final del piloto
            score_final = piloto.score
            score_final += equipo.auto.score if equipo.auto else 0
            score_final -= 5 * errores_pits.count(piloto.numero_auto)
            score_final -= 8 * penalidades.count(piloto.numero_auto)

            resultados.append((piloto, score_final))

    # Ordenar los pilotos por su score final
    resultados.sort(key=lambda x: x[1], reverse=True)

    # Asignar puntos a los pilotos
    puntos = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
    for i, (piloto, score) in enumerate(resultados):
        puntos_asignados = puntos[i] if i < len(puntos) else 0
        piloto.puntaje_campeonato += puntos_asignados
        print(f"Piloto {piloto.nombre}, Auto {piloto.numero_auto}, Score Final: {score}, Puntos Ganados: {puntos_asignados}")
