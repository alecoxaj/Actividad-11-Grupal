import json
import os

DIR_DATOS = "datos"
ARCH_VACUNAS = os.path.join(DIR_DATOS, "vacunas.json")
ARCH_MASCOTAS = os.path.join(DIR_DATOS, "mascotas.json")

def inicializar_modulo_vacunas():
    os.makedirs(DIR_DATOS, exist_ok=True)
    if not os.path.exists(ARCH_VACUNAS):
        with open(ARCH_VACUNAS, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)

def _cargar_json(ruta):
    if not os.path.exists(ruta):
        return []
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def _guardar_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)

def registrar_vacuna():
    print("\n--- Registrar Vacuna ---")
    codigo_m = input("Código de la mascota: ").strip()

    mascotas = _cargar_json(ARCH_MASCOTAS)
    if mascotas and not any(m["codigo"] == codigo_m for m in mascotas):
        print(" Error: La mascota no se encuentra registrada.")
        return

    vacunas = _cargar_json(ARCH_VACUNAS)

    nueva_vacuna = {
        "codigo_mascota": codigo_m,
        "nombre_vacuna": input("Nombre de la vacuna: ").strip(),
        "fecha_aplicacion": input("Fecha de aplicación (DD/MM/AAAA): ").strip(),
        "proxima_dosis": input("Próxima dosis (DD/MM/AAAA): ").strip(),
        "veterinario": input("Veterinario responsable: ").strip()
    }

    vacunas.append(nueva_vacuna)
    _guardar_json(ARCH_VACUNAS, vacunas)
    print(" Vacuna registrada exitosamente en el archivo.")


def consultar_vacunas():
    print("\n--- Consulta de Vacunas ---")
    codigo_m = input("Código de la mascota a consultar: ").strip()

    vacunas = _cargar_json(ARCH_VACUNAS)
    historial = [v for v in vacunas if v["codigo_mascota"] == codigo_m]

    if not historial:
        print(f"No se encontraron vacunas registradas para la mascota '{codigo_m}'.")
        return

    print(f"\nVacunas registradas para la mascota [{codigo_m}]:")
    for idx, v in enumerate(historial, start=1):
        print(f" {idx}. Vacuna: {v['nombre_vacuna']}")
        print(f"    Fecha Aplicación: {v['fecha_aplicacion']}")
        print(f"    Próxima Dosis:    {v['proxima_dosis']}")
        print(f"    Veterinario:      {v['veterinario']}\n")