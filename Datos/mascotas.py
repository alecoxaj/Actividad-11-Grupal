import os
import json

DIR_DATOS = "datos"
ARCH_MASCOTAS = os.path.join(DIR_DATOS, "mascotas.json")

def _cargar_mascotas():
    """Carga la lista de mascotas desde el archivo JSON."""
    if not os.path.exists(ARCH_MASCOTAS):
        return []
    try:
        with open(ARCH_MASCOTAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []

def _guardar_mascotas(mascotas):
    """Guarda la lista de mascotas en el archivo JSON."""
    os.makedirs(DIR_DATOS, exist_ok=True)
    with open(ARCH_MASCOTAS, "w", encoding="utf-8") as archivo:
        json.dump(mascotas, archivo, indent=4, ensure_ascii=False)

def registrar_mascota():
    """Función para registrar una nueva mascota en el sistema."""
    print("\n--- Registrar Mascota ---")
    mascotas = _cargar_mascotas()

    codigo = input("Código: ").strip()

    # Validación de código existente
    if any(m["codigo"] == codigo for m in mascotas):
        print(" Error: Ya existe una mascota con ese código.")
        return

    nombre = input("Nombre: ").strip()
    especie = input("Especie: ").strip()
    raza = input("Raza: ").strip()
    fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
    propietario = input("Nombre del propietario: ").strip()
    telefono = input("Teléfono del propietario: ").strip()
    estado = input("Estado (activo/inactivo): ").strip().lower()

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
    _guardar_mascotas(mascotas)

    print(" Mascota registrada correctamente en 'datos/mascotas.json'.")