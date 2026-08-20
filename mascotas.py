import os
import json

DIR_DATOS = "datos"
ARCH_MASCOTAS = os.path.join(DIR_DATOS, "mascotas.json")

def _cargar_mascotas():
    """Carga la lista de mascotas desde el archivo JSON."""
    try:
        os.makedirs(DIR_DATOS, exist_ok=True)

        if not os.path.exists(ARCH_MASCOTAS):
            return []

        with open(ARCH_MASCOTAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except json.JSONDecodeError:
        print("Error: El archivo de mascotas está vacío o contiene datos inválidos.")
        return []

    except OSError:
        print("Error: No se pudo abrir el archivo de mascotas.")
        return []

    except Exception as error:
        print(f"Error inesperado al cargar mascotas: {error}")
        return []


def _guardar_mascotas(mascotas):
    """Guarda la lista de mascotas en el archivo JSON."""
    try:
        os.makedirs(DIR_DATOS, exist_ok=True)

        with open(ARCH_MASCOTAS, "w", encoding="utf-8") as archivo:
            json.dump(
                mascotas,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        return True

    except OSError:
        print("Error: No se pudo guardar la información de las mascotas.")
        return False

    except Exception as error:
        print(f"Error inesperado al guardar mascotas: {error}")
        return False


def registrar_mascota():
    """Función para registrar una nueva mascota en el sistema."""
    try:
        print("\n--- Registrar Mascota ---")

        mascotas = _cargar_mascotas()

        codigo = input("Código: ").strip()

        if codigo == "":
            print("Error: El código no puede estar vacío.")
            return

        if any(mascota["codigo"].upper() == codigo.upper() for mascota in mascotas):
            print("Error: Ya existe una mascota con ese código.")
            return

        nombre = input("Nombre: ").strip()
        especie = input("Especie: ").strip()
        raza = input("Raza: ").strip()
        fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
        propietario = input("Nombre del propietario: ").strip()
        telefono = input("Teléfono: ").strip()
        estado = input("Estado (activo/inactivo): ").strip().lower()

        if estado not in ["activo", "inactivo"]:
            print("Error: El estado debe ser 'activo' o 'inactivo'.")
            return

        nueva_mascota = {
            "codigo": codigo,
            "nombre": nombre,
            "especie": especie,
            "raza": raza,
            "fecha_nacimiento": fecha_nacimiento,
            "propietario": propietario,
            "telefono": telefono,
            "estado": estado
        }

        mascotas.append(nueva_mascota)

        if _guardar_mascotas(mascotas):
            print("Mascota registrada correctamente.")

    except KeyboardInterrupt:
        print("\nRegistro cancelado por el usuario.")

    except Exception as error:
        print(f"Error inesperado al registrar la mascota: {error}")


def mostrar_mascotas():
    """Función para mostrar todas las mascotas registradas."""
    try:
        print("\n--- Mostrar Todas las Mascotas ---")

        mascotas = _cargar_mascotas()

        if not mascotas:
            print("No hay mascotas registradas.")
            return

        for mascota in mascotas:
            print("\n------------------------------")
            print(f"Código: {mascota.get('codigo', 'Sin dato')}")
            print(f"Nombre: {mascota.get('nombre', 'Sin dato')}")
            print(f"Especie: {mascota.get('especie', 'Sin dato')}")
            print(f"Raza: {mascota.get('raza', 'Sin dato')}")
            print(f"Fecha de nacimiento: {mascota.get('fecha_nacimiento', 'Sin dato')}")
            print(f"Propietario: {mascota.get('propietario', 'Sin dato')}")
            print(f"Teléfono: {mascota.get('telefono', 'Sin dato')}")
            print(f"Estado: {mascota.get('estado', 'Sin dato')}")

    except Exception as error:
        print(f"Error inesperado al mostrar las mascotas: {error}")


def buscar_mascota():
    """Función para buscar una mascota por su código."""
    try:
        print("\n--- Buscar Mascota por Código ---")

        mascotas = _cargar_mascotas()

        if not mascotas:
            print("No hay mascotas registradas.")
            return

        codigo_buscar = input("Ingrese el código de la mascota: ").strip()

        if codigo_buscar == "":
            print("Error: Debe ingresar un código.")
            return

        for mascota in mascotas:
            if mascota.get("codigo", "").upper() == codigo_buscar.upper():
                print("\nMascota encontrada:")
                print("------------------------------")
                print(f"Código: {mascota.get('codigo', 'Sin dato')}")
                print(f"Nombre: {mascota.get('nombre', 'Sin dato')}")
                print(f"Especie: {mascota.get('especie', 'Sin dato')}")
                print(f"Raza: {mascota.get('raza', 'Sin dato')}")
                print(f"Fecha de nacimiento: {mascota.get('fecha_nacimiento', 'Sin dato')}")
                print(f"Propietario: {mascota.get('propietario', 'Sin dato')}")
                print(f"Teléfono: {mascota.get('telefono', 'Sin dato')}")
                print(f"Estado: {mascota.get('estado', 'Sin dato')}")
                return

        print("No se encontró una mascota con ese código.")

    except KeyboardInterrupt:
        print("\nBúsqueda cancelada por el usuario.")

    except Exception as error:
        print(f"Error inesperado al buscar la mascota: {error}")