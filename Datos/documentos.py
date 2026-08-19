import os
import json
import shutil
from datetime import datetime

DIR_DATOS = "datos"
ARCH_MASCOTAS = os.path.join(DIR_DATOS, "mascotas.json")
ARCH_DOCUMENTOS = os.path.join(DIR_DATOS, "documentos.json")
DIR_DOCUMENTOS = os.path.join(DIR_DATOS, "documentos")

def _cargar_mascotas():
    if not os.path.exists(ARCH_MASCOTAS):
        return []
    try:
        with open(ARCH_MASCOTAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []


def _buscar_mascota(codigo):
    mascotas = _cargar_mascotas()
    return next((m for m in mascotas if m["codigo"] == codigo), None)


def _cargar_documentos():
    if not os.path.exists(ARCH_DOCUMENTOS):
        return []
    try:
        with open(ARCH_DOCUMENTOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []


def _guardar_documentos(documentos):
    os.makedirs(DIR_DATOS, exist_ok=True)
    with open(ARCH_DOCUMENTOS, "w", encoding="utf-8") as archivo:
        json.dump(documentos, archivo, indent=4, ensure_ascii=False)


def _detectar_tipo(nombre_archivo):
    ext = os.path.splitext(nombre_archivo)[1].lower()
    if ext in (".jpg", ".jpeg", ".png", ".gif", ".bmp"):
        return "fotografia"
    if ext == ".pdf":
        return "documento_pdf"
    return "otro"

def asociar_documento():
    print("\n--- Asociar Documento a Mascota ---")

    codigo = input("Código de la mascota: ").strip()
    mascota = _buscar_mascota(codigo)

    if mascota is None:
        print(" Error: No existe una mascota con ese código.")
        return

    ruta_origen = input("Ruta del archivo a asociar (ej. Kiss.jpg): ").strip()

    if not os.path.isfile(ruta_origen):
        print(f" Error: No se encontró el archivo '{ruta_origen}'.")
        return

    carpeta_mascota = os.path.join(DIR_DOCUMENTOS, codigo)
    os.makedirs(carpeta_mascota, exist_ok=True)

    nombre_archivo = os.path.basename(ruta_origen)
    ruta_destino = os.path.join(carpeta_mascota, nombre_archivo)

    shutil.copy2(ruta_origen, ruta_destino)

    documentos = _cargar_documentos()
    documentos.append({
        "codigo_mascota": codigo,
        "nombre_archivo": nombre_archivo,
        "tipo": _detectar_tipo(nombre_archivo),
        "fecha_asociacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ruta_almacenada": ruta_destino
    })
    _guardar_documentos(documentos)

    print(f" Documento '{nombre_archivo}' asociado correctamente a {mascota['nombre']} ({codigo}).")


def mostrar_documentos():
    print("\n--- Documentos de una Mascota ---")
    codigo = input("Código de la mascota: ").strip()

    documentos = _cargar_documentos()
    docs_mascota = [d for d in documentos if d["codigo_mascota"] == codigo]

    if not docs_mascota:
        print(f"No hay documentos registrados para la mascota {codigo}.")
        return

    print(f"\nDocumentos de la mascota {codigo}:")
    for i, d in enumerate(docs_mascota, start=1):
        print(f"  {i}. {d['nombre_archivo']} | Tipo: {d['tipo']} | Asociado: {d['fecha_asociacion']}")


def recuperar_documento():
    print("\n--- Recuperar Documento ---")
    codigo = input("Código de la mascota: ").strip()
    nombre_archivo = input("Nombre del archivo a recuperar (ej. Kiss.jpg): ").strip()
    carpeta_destino = input("Carpeta destino (ej. recuperados): ").strip()

    documentos = _cargar_documentos()
    encontrado = next(
        (d for d in documentos
         if d["codigo_mascota"] == codigo and d["nombre_archivo"] == nombre_archivo),
        None
    )

    if not encontrado:
        print(" No se encontró ese documento para esa mascota.")
        return

    os.makedirs(carpeta_destino, exist_ok=True)
    ruta_copia = os.path.join(carpeta_destino, nombre_archivo)
    shutil.copy2(encontrado["ruta_almacenada"], ruta_copia)

    print(f" Documento recuperado y copiado en: {ruta_copia}")