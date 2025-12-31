# main.py
import sys
import logica
import validaciones


def menu_principal():
    """Función principal que contiene el bucle de control."""
    while True:
        print("\n" + "=" * 40)
        print("   SISTEMA DE MATRÍCULA UNIVERSITARIA   ")
        print("=" * 40)
        print("1. Registrar Estudiante")
        print("2. Listar Estudiantes")
        print("3. Simular Costo Total (Recursivo)")
        print("4. Salir")

        opcion = validaciones.leer_entero("\nSeleccione una opción: ", 1, 4)

        # Estructura condicional IF-ELIF-ELSE
        if opcion == 1:
            logica.registrar_estudiante()
        elif opcion == 2:
            logica.mostrar_estudiantes()
        elif opcion == 3:
            logica.simular_arancel()
        elif opcion == 4:
            print("Saliendo del sistema... ¡Hasta pronto!")
            break  # Rompe el ciclo while
        else:
            print("Opción no válida.")


# Punto de entrada del script
if __name__ == "__main__":
    menu_principal()
