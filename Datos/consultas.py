import json

ARCHIVO = "consultas.json"


def cargar_consultas():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            consultas = json.load(archivo)

        return consultas

    except FileNotFoundError:

        return []


def guardar_consultas(consultas):
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(
            consultas,
            archivo,
            ensure_ascii=False,
        )


def generar_codigo(consultas):
    if len(consultas) == 0:
        return "C001"

    ultimo_numero = 0

    for consulta in consultas:

        codigo = consulta["codigo_consulta"]

        numero = int(codigo[1:])

        if numero > ultimo_numero:
            ultimo_numero = numero

    siguiente = ultimo_numero + 1

    return f"C{siguiente:03d}"


def registrar_consulta():
    consultas = cargar_consultas()

    print("\n===== REGISTRAR CONSULTA =====")

    codigo_mascota = input("Código de mascota: ")

    fecha = input("Fecha: ")

    motivo = input("Motivo: ")

    diagnostico = input("Diagnóstico: ")

    tratamiento = input("Tratamiento: ")

    costo = float(input("Costo: Q"))

    codigo_consulta = generar_codigo(consultas)

    consulta = {

        "codigo_consulta": codigo_consulta,

        "codigo_mascota": codigo_mascota,

        "fecha": fecha,

        "motivo": motivo,

        "diagnostico": diagnostico,

        "tratamiento": tratamiento,

        "costo": costo

    }

    consultas.append(consulta)
    guardar_consultas(consultas)

    print("\nConsulta registrada correctamente.")

    print("Código de consulta:", codigo_consulta)


def mostrar_consultas(consulta):
    print("\nCONSULTAS: ")
    print("Código consulta:",
          consulta["codigo_consulta"], )

    print("Código mascota:",
          consulta["codigo_mascota"])

    print("Fecha:",
          consulta["fecha"])

    print("Motivo:",
          consulta["motivo"])

    print("Diagnóstico:",
          consulta["diagnostico"])

    print("Tratamiento:",
          consulta["tratamiento"])

    print("Costo: Q",
          format(consulta["costo"], ".2f"))


def historial_mascota(codigo_mascota):
    consultas = cargar_consultas()

    encontradas = []

    for consulta in consultas:

        if consulta["codigo_mascota"].upper() == codigo_mascota.upper():
            encontradas.append(consulta)

    print("\n===== HISTORIAL DE CONSULTAS =====")

    print("Mascota:", codigo_mascota)

    if len(encontradas) == 0:
        print("No tiene consultas registradas.")

        return

    for consulta in encontradas:
        print("\nHISTORIAL")

        print("Código:",
              consulta["codigo_consulta"])

        print("Fecha:",
              consulta["fecha"])

        print("Motivo:",
              consulta["motivo"])

        print("Diagnóstico:",
              consulta["diagnostico"])

        print("Tratamiento:",
              consulta["tratamiento"])

        print("Costo: Q",
              format(consulta["costo"], ".2f"))


def buscar(codigo_mascota):
    consultas = cargar_consultas()

    for consulta in consultas:

        if consulta["codigo_consulta"].upper() == codigo_mascota.upper():
            return consulta

    return None