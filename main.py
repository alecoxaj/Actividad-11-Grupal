from Datos.mascotas import registrar_mascota
from Datos.consultas import registrar_consulta, consultar_historial
from Datos.vacunas import (
    inicializar_modulo_vacunas,
    registrar_vacuna,
    consultar_vacunas
)


def menu_mascotas():
    while True:
        print("\n==============================")
        print("        MENÚ MASCOTAS")
        print("==============================")
        print("1. Registrar mascota")
        print("2. Regresar al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                registrar_mascota()
            case "2":
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


def menu_consultas():
    while True:
        print("\n==============================")
        print("        MENÚ CONSULTAS")
        print("==============================")
        print("1. Registrar consulta")
        print("2. Consultar historial")
        print("3. Regresar al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                registrar_consulta()
            case "2":
                consultar_historial()
            case "3":
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


def menu_vacunas():
    while True:
        print("\n==============================")
        print("         MENÚ VACUNAS")
        print("==============================")
        print("1. Registrar vacuna")
        print("2. Consultar vacunas")
        print("3. Regresar al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                registrar_vacuna()
            case "2":
                consultar_vacunas()
            case "3":
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


def main():
    # Crea vacunas.json si todavía no existe.
    inicializar_modulo_vacunas()

    while True:
        print("\n==========================================")
        print("   SISTEMA DE GESTIÓN CLÍNICA VETERINARIA")
        print("==========================================")
        print("1. Mascotas")
        print("2. Consultas")
        print("3. Vacunas")
        print("4. Salir")
        print("==========================================")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                menu_mascotas()
            case "2":
                menu_consultas()
            case "3":
                menu_vacunas()
            case "4":
                print("\nSaliendo del sistema...")
                print("Programa finalizado.")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()