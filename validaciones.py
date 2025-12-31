# validaciones.py

def validar_rut_chileno(rut):
    """
    Aplica el algoritmo de Módulo 11 para validar un RUT chileno.
    Retorna (True, rut_limpio) si es válido, o (False, mensaje_error) si no.
    """
    # 1. Limpieza de datos (eliminar puntos y guión, pasar a mayúsculas)
    rut_limpio = rut.replace(".", "").replace("-", "").upper().strip()

    # Validar largo mínimo (ej: 1.111.111-1 tiene 8 caracteres mínimos sin puntos ni guión)
    if len(rut_limpio) < 8 or len(rut_limpio) > 9:
        return False, "El largo del RUT es incorrecto."

    # Separar cuerpo y dígito verificador
    cuerpo = rut_limpio[:-1]
    dv_ingresado = rut_limpio[-1]

    # 2. Validar que el cuerpo sean solo números
    if not cuerpo.isdigit():
        return False, "El cuerpo del RUT debe contener solo números."

    # 3. Calcular Dígito Verificador (Algoritmo Módulo 11)
    suma = 0
    multiplo = 2

    # Recorremos el cuerpo del rut de atrás hacia adelante (reversed)
    for c in reversed(cuerpo):
        suma += int(c) * multiplo
        multiplo += 1
        if multiplo == 8:
            multiplo = 2

    # Fórmula del algoritmo
    resto = suma % 11
    dv_calculado = 11 - resto

    # Convertir resultado numérico a formato RUT (11=0, 10=K)
    if dv_calculado == 11:
        dv_final = '0'
    elif dv_calculado == 10:
        dv_final = 'K'
    else:
        dv_final = str(dv_calculado)

    # 4. Comparar
    if dv_final == dv_ingresado:
        # Devolvemos el RUT formateado con guión para guardarlo ordenado
        return True, f"{cuerpo}-{dv_final}"
    else:
        return False, "El dígito verificador es incorrecto."


def leer_rut(mensaje):
    """
    Solicita un RUT al usuario y no avanza hasta que sea matemáticamente válido.
    """
    while True:
        rut_entrada = input(mensaje)
        es_valido, resultado = validar_rut_chileno(rut_entrada)

        if es_valido:
            return resultado  # Retorna el RUT limpio y formateado (ej: 12345678-K)
        else:
            print(f" Error: {resultado} Intente nuevamente.")


# ... (Mantener aquí tus funciones leer_entero y leer_texto anteriores) ...
def leer_texto(mensaje):
    """Valida que el texto no esté vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print(" Error: El campo no puede estar vacío.")


def leer_entero(mensaje, minimo=None, maximo=None):
    """Captura un entero validando rango y tipo."""
    while True:
        try:
            valor = input(mensaje)
            numero = int(valor)
            if minimo is not None and numero < minimo:
                print(f" Error: El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and numero > maximo:
                print(f" Error: El valor debe ser menor o igual a {maximo}.")
                continue
            return numero
        except ValueError:
            print(" Error: Debes ingresar un número entero válido.")