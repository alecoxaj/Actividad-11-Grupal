import os
import json

DIR_DATOS = "datos"
ARCH_CONSULTAS = os.path.join(DIR_DATOS, "consultas.json")
ARCH_MASCOTAS = os.path.join(DIR_DATOS, "mascotas.json")


def _cargar_json(ruta):
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []


def _guardar_consultas(consultas):
    os.makedirs(DIR_DATOS, exist_ok=True)
    with open(ARCH_CONSULTAS, "w", encoding="utf-8") as archivo:
        json.dump(consultas, archivo, indent=4, ensure_ascii=False)


def generar_codigo(consultas):
    if not consultas:
        return "C001"

    ultimo_numero = 0
    for consulta in consultas:
        codigo = consulta.get("codigo_consulta", "C000")
        try:
            numero = int(codigo[1:])
            if numero > ultimo_numero:
                ultimo_numero = numero
        except ValueError:
            continue

    return f"C{ultimo_numero + 1:03d}"

def registrar_consulta():
    print("\n--- Registrar Consulta ---")
    codigo_mascota = input("Código de mascota: ").strip()

    mascotas = _cargar_json(ARCH_MASCOTAS)
    if mascotas and not any(m["codigo"] == codigo_mascota for m in mascotas):
        print(" Error: La mascota no existe en el sistema.")
        return

    fecha = input("Fecha (DD/MM/AAAA): ").strip()
    motivo = input("Motivo: ").strip()
    diagnostico = input("Diagnóstico: ").strip()
    tratamiento = input("Tratamiento: ").strip()

    try:
        costo = float(input("Costo (Q): ").strip())
    except ValueError:
        costo = 0.0

    consultas = _cargar_json(ARCH_CONSULTAS)
    codigo_consulta = generar_codigo(consultas)

    nueva_consulta = {
        "codigo_consulta": codigo_consulta,
        "codigo_mascota": codigo_mascota,
        "fecha": fecha,
        "motivo": motivo,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento,
        "costo": costo
    }

    consultas.append(nueva_consulta)
    _guardar_consultas(consultas)

    print(f" Consulta registrada correctamente con código [{codigo_consulta}].")


def consultar_historial():
    codigo_mascota = input("\nIngrese el código de la mascota a consultar: ").strip()
    consultas = _cargar_json(ARCH_CONSULTAS)

    encontradas = [c for c in consultas if c["codigo_mascota"].upper() == codigo_mascota.upper()]

    print(f"\n--- Historial de Consultas (Mascota: {codigo_mascota}) ---")
    if not encontradas:
        print("No hay consultas registradas para esta mascota.")
        return

    for c in encontradas:
        print(f"\n[Código: {c['codigo_consulta']}] - Fecha: {c['fecha']}")
        print(f"  Motivo:      {c['motivo']}")
        print(f"  Diagnóstico: {c['diagnostico']}")
        print(f"  Tratamiento: {c['tratamiento']}")
        print(f"  Costo:       Q{c['costo']:.2f}")