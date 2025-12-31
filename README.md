# modulo3-python
Proyecto: Sistema de gestión de datos de mi proyecto es matricula de educación superior

# Sistema Matrícula Estudiantil Modular Python


# Flujo de Información

Cuando registras a alguien, el flujo es el siguiente:

1.- main.py llama a registrar.

2.- logica.py pide los datos.

3.- validaciones.py revisa que el RUT y la edad sean reales.

4.- datos.py guarda el resultado final.


# 1. datos.py (Capa de Persistencia Volátil)
   
Es el "almacén" o base de datos temporal del programa. No contiene lógica, solo contenedores de información.

Tupla (CARRERAS_DISPONIBLES): Define las opciones fijas de estudio. Es inmutable para asegurar que nadie borre una carrera por accidente durante la ejecución.

Lista (estudiantes): Almacena los diccionarios con la ficha de cada alumno.

Conjunto (ruts_registrados): Actúa como un índice de búsqueda rápida para asegurar que no se repitan los RUTs (un set es mucho más eficiente que una list para buscar duplicados).


# 2. validaciones.py (Capa de Seguridad)
   
Es el "escudo" del programa. Su objetivo es filtrar cualquier dato basura que el usuario intente ingresar.

Validación de Tipos: Asegura que si pides un número, no te entreguen letras (manejo de ValueError).

Validación Matemática (RUT): Contiene el algoritmo del Módulo 11. Calcula si el dígito verificador es correcto para evitar datos falsos.

Limpieza: Se encarga de transformar lo que el usuario escribe (como quitar puntos o convertir a mayúsculas) para que el resto del programa trabaje con datos limpios.


# 3. logica.py (Capa de Negocio)
   
Es el "cerebro" donde ocurren los procesos principales. Conecta la entrada del usuario con el almacenamiento.

Gestión de Registro: Orquesta el flujo de pedir datos, validarlos y guardarlos en el diccionario de estudiantes.

Recursividad: Aquí reside la función calcular_costo_recursivo, que demuestra un nivel avanzado de programación al llamarse a sí misma para proyectar el arancel total.

Visualización: Formatea la salida de datos para que el usuario vea la información de manera elegante (tablas y resúmenes).



# 4. main.py (Capa de Interfaz / Orquestador)
   
Es el punto de partida y el "director de orquesta".

Bucle Principal: Mantiene el programa encendido (while True) hasta que el usuario decida salir.

Menú Interactivo: Es la cara visible que conecta las opciones del menú con las funciones específicas de logica.py.

Control de Flujo: Decide qué camino tomar basado en la decisión del usuario.
