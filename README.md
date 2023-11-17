# obligatorio-p1-2023
Obligatorio Nicolas Iker Guglielmelli

Simulación de Carreras de F1:

Descripción: 

Esta aplicación es una Prueba de Concepto (PoC) para la simulación de carreras del campeonato de Fórmula 1. Permite gestionar equipos y empleados, simular carreras, y realizar varias consultas relacionadas con el rendimiento y estadísticas de los pilotos y equipos.


Cómo Ejecutar la Aplicación:
Para ejecutar la aplicación, sigue estos pasos:

Ejecuta el script principal con el comando: python main.py (asegúrate de que estés en el directorio correcto donde se encuentra main.py).

Al iniciar el programa, se te presentará un menú principal con las siguientes opciones:

Alta de Empleado: Permite ingresar nuevos empleados al sistema, incluyendo pilotos, mecánicos y jefes de equipo. Deberás proporcionar detalles como cédula, nombre, fecha de nacimiento, nacionalidad, salario, y otros atributos específicos del rol.

Alta de Auto: Aquí puedes registrar un nuevo auto para los equipos, especificando el modelo, año y score del auto.

Alta de Equipo: Esta opción te permite crear un nuevo equipo, asignándole pilotos, mecánicos, un jefe de equipo y un auto.

Simular Carrera: Inicia la simulación de una carrera, donde puedes registrar eventos como pilotos lesionados o penalizaciones. La carrera se simula basada en los datos de los pilotos y autos, y el resultado se muestra al final.

Realizar Consultas: Accede a una serie de consultas para obtener información sobre los pilotos y equipos, como el top de pilotos, resumen del campeonato de constructores, entre otros.

Finalizar Programa: Cierra la aplicación.

Navegación e Interacción
Navega a través del menú utilizando los números correspondientes a cada opción.
Sigue las instrucciones en pantalla para ingresar datos cuando se te solicite.
Después de completar una acción, serás redirigido al menú principal para elegir otra acción o salir del programa.

Diagrama UML
El proyecto incluye un diagrama UML que representa la estructura de clases de la aplicación. Las clases principales son:
Empleado: Clase base para diferentes tipos de empleados como Piloto, Mecánico y Jefe de Equipo.
Piloto, Mecanico, JefeEquipo: Subclases de Empleado con atributos específicos.
Auto: Representa los autos con modelo, año y puntuación.
Equipo: Compuesto por pilotos, mecánicos, un jefe de equipo y un auto.
Las relaciones entre estas clases incluyen herencia (subclases de Empleado) y asociaciones (como Equipo conteniendo pilotos y un auto).
