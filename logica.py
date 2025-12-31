# logica.py
import datos
import validaciones


# ... (Mantener la función calcular_costo_recursivo igual) ...
def calcular_costo_recursivo(semestres_restantes, costo_semestre):
    if semestres_restantes <= 0:
        return 0
    else:
        return costo_semestre + calcular_costo_recursivo(semestres_restantes - 1, costo_semestre)


def registrar_estudiante():
    print(f"\n---  Registro de Nuevo Estudiante ---")

    # CAMBIO AQUÍ: Usamos la nueva función de validación de RUT
    rut = validaciones.leer_rut("Ingrese RUT del estudiante (ej: 12.345.678-K): ")

    # Verificamos si ya existe en nuestro SET de datos
    if rut in datos.ruts_registrados:
        print(f" Error: El RUT {rut} ya se encuentra registrado en el sistema.")
        return

    nombre = validaciones.leer_texto("Ingrese Nombre completo: ")
    edad = validaciones.leer_entero("Ingrese Edad: ", minimo=17, maximo=99)

    print("\nCarreras disponibles:")
    for i, carrera in enumerate(datos.CARRERAS_DISPONIBLES, 1):
        print(f"{i}. {carrera}")

    opcion_carrera = validaciones.leer_entero("Seleccione una carrera (número): ", 1, len(datos.CARRERAS_DISPONIBLES))
    carrera_seleccionada = datos.CARRERAS_DISPONIBLES[opcion_carrera - 1]

    nuevo_estudiante = {
        "rut": rut,
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera_seleccionada,
        "matriculado": True
    }

    datos.estudiantes.append(nuevo_estudiante)
    datos.ruts_registrados.add(rut)

    print(f" Estudiante registrado con éxito: {nombre} (RUT: {rut})")


# ... (Mantener el resto de funciones igual) ...
def mostrar_estudiantes():
    print(f"\n---  Listado de Estudiantes ---")
    if not datos.estudiantes:
        print("No hay estudiantes registrados.")
        return

    for est in datos.estudiantes:
        estado = "Activo" if est['matriculado'] else "Inactivo"
        print(f"🎓 {est['nombre']} | RUT: {est['rut']} | Carrera: {est['carrera']} | Estado: {estado}")


def simular_arancel():
    print(f"\n--- 💰 Simulación de Arancel Total ---")

    # 1. MOSTRAR Y SELECCIONAR CARRERA
    print("Para comenzar, seleccione la carrera a proyectar:")
    for i, carrera in enumerate(datos.CARRERAS_DISPONIBLES, 1):
        print(f"{i}. {carrera}")

    opcion_carrera = validaciones.leer_entero("Seleccione una carrera (número): ", 1, len(datos.CARRERAS_DISPONIBLES))
    carrera_seleccionada = datos.CARRERAS_DISPONIBLES[opcion_carrera - 1]

    print(f"\n--- Simulando costos para: {carrera_seleccionada.upper()} ---")

    try:
        # 2. CAPTURA DE DATOS (Personalizado con el nombre de la carrera)
        semestres = validaciones.leer_entero(f"Ingrese duración de {carrera_seleccionada} en semestres: ", 1, 14)
        costo = validaciones.leer_entero("Ingrese valor del arancel semestral (CLP): ", 0)

        # 3. CÁLCULO RECURSIVO
        total = calcular_costo_recursivo(semestres, costo)

        # 4. SALIDA DE DATOS FORMATEADA
        print("\n" + "=" * 50)
        print(f" RESUMEN DE PROYECCIÓN")
        print(f"Carrera Objetiva : {carrera_seleccionada}")
        print(f"Duración         : {semestres} semestres")
        print(f"Arancel Semestral: ${costo:,.0f} CLP")
        print("-" * 50)
        print(f" INVERSIÓN TOTAL: ${total:,.0f} CLP")
        print("=" * 50)

    except Exception as e:
        print(f" Ocurrió un error inesperado durante la simulación: {e}")