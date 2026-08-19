import json

try:
    with open("mascotas.json", "r", encoding="utf-8") as archivo:
        mascotas = json.load(archivo)

except FileNotFoundError:
    mascotas = []

except json.JSONDecodeError:
    mascotas = []

while True:
    print("----------------------")
    print("1. Registrar mascota")
    print("2. Salir")
    print("----------------------")

    option = input("Seleccione una opción: ")

    match option:

        case "1":
            print("1. Registrar Mascota")

            codigo = input("Código: ")
            nombre = input("Nombre: ")
            especie = input("Especie: ")
            raza = input("Raza: ")
            fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
            propietario = input("Nombre del propietario: ")
            telefono = input("Teléfono del propietario: ")
            estado = input("Estado (activo/inactivo): ")

            mascota = {
                "codigo": codigo,
                "nombre": nombre,
                "especie": especie,
                "raza": raza,
                "fecha_nacimiento": fecha_nacimiento,
                "propietario": propietario,
                "telefono": telefono,
                "estado": estado
            }

            mascotas.append(mascota)

            with open("mascotas.json", "w", encoding="utf-8") as archivo:
                json.dump(
                    mascotas,
                    archivo,
                    indent=4,
                    ensure_ascii=False
                )

            print("Mascota registrada correctamente.")

        case "2":
            print("Saliendo del programa...")
            break

        case _:
            print("Error, opción inválida, intenta de nuevo.")