import os
import json

# Importaciones directas (todos los archivos .py deben estar en la raíz)
from mascotas import (
    registrar_mascota,
    mostrar_mascotas,
    buscar_mascota
)

from consultas import (
    registrar_consulta,
    consultar_historial
)

from vacunas import (
    inicializar_modulo_vacunas,
    registrar_vacuna,
    consultar_vacunas
)

from documentos import (
    asociar_documento,
    mostrar_documentos,
    recuperar_documento
)

# Rutas para el Resumen General
DIR_DATOS = "datos"
ARCH_MASCOTAS = os.path.join(DIR_DATOS, "mascotas.json")
ARCH_CONSULTAS = os.path.join(DIR_DATOS, "consultas.json")
ARCH_VACUNAS = os.path.join(DIR_DATOS, "vacunas.json")
ARCH_DOCUMENTOS = os.path.join(DIR_DATOS, "documentos.json")


def _cargar_json(ruta):
    """Carga los datos de cualquier JSON para el conteo general."""
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []


def mostrar_resumen_general():
    """Punto 9: Resumen general con métricas del sistema."""
    mascotas = _cargar_json(ARCH_MASCOTAS)
    consultas = _cargar_json(ARCH_CONSULTAS)
    vacunas = _cargar_json(ARCH_VACUNAS)
    documentos = _cargar_json(ARCH_DOCUMENTOS)

    print("\n==========================================")
    print("      RESUMEN GENERAL DEL SISTEMA         ")
    print("==========================================")
    print(f"  Total Mascotas Registradas:  {len(mascotas)}")
    print(f"  Total Consultas Realizadas:  {len(consultas)}")
    print(f"  Total Vacunas Aplicadas:     {len(vacunas)}")
    print(f"  Total Documentos Adjuntos:   {len(documentos)}")
    print("==========================================\n")


def menu_mascotas():
    while True:
        print("\n==============================")
        print("        MENÚ MASCOTAS")
        print("==============================")
        print("1. Registrar mascota")
        print("2. Mostrar todas las mascotas")
        print("3. Buscar mascota por código")
        print("4. Regresar al menú principal")
        print("==============================")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                registrar_mascota()
            case "2":
                mostrar_mascotas()
            case "3":
                buscar_mascota()
            case "4":
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


def menu_consultas():
    while True:
        print("\n==============================")
        print("        MENÚ CONSULTAS")
        print("==============================")
        print("1. Registrar consulta")
        print("2. Consultar historial de una mascota")
        print("3. Regresar al menú principal")
        print("==============================")

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
        print("2. Consultar vacunas de una mascota")
        print("3. Regresar al menú principal")
        print("==============================")

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


def menu_documentos():
    while True:
        print("\n==============================")
        print("       MENÚ DOCUMENTOS")
        print("==============================")
        print("1. Asociar archivo/imagen a una mascota")
        print("2. Consultar documentos de una mascota")
        print("3. Recuperar/Copiar documento guardado")
        print("4. Regresar al menú principal")
        print("==============================")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                asociar_documento()
            case "2":
                mostrar_documentos()
            case "3":
                recuperar_documento()
            case "4":
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


def main():
    try:
        inicializar_modulo_vacunas()

        while True:
            print("\n==========================================")
            print("   SISTEMA DE GESTIÓN CLÍNICA VETERINARIA")
            print("==========================================")
            print("1. Mascotas")
            print("2. Consultas")
            print("3. Vacunas")
            print("4. Documentos / Archivos")
            print("5. Mostrar Resumen General")
            print("6. Salir")
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
                    menu_documentos()
                case "5":
                    mostrar_resumen_general()
                case "6":
                    print("\nSaliendo del sistema...")
                    print("Programa finalizado exitosamente.")
                    break
                case _:
                    print("Opción inválida. Intente nuevamente.")

    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario.")

    except Exception as error:
        print(f"\nOcurrió un error inesperado: {error}")


if __name__ == "__main__":
    main()