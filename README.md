# Sistema de Gestión Veterinaria

## Información de la tarea

**Tarea:** Persistencia de un sistema

**Estudiantes:**

| Nombre completo | Carné |
| :--- | :---: |
| **BATZ RODRÍGUEZ SANTIAGO JEFTÉ** | **1548725** |
| **COXAJ RAMÍREZ MANUEL ALEJANDRO** | **1506925** |
| **GARCÍA IXCAMPARY ANGELO GUSTAVO** | **1547225** |
| **VÁSQUEZ CHAN MARVIN ANTONIO** | **1558525** |

## Funcionalidades principales

- Registrar, consultar, modificar y eliminar mascotas.
- Registrar consultas asociadas con una mascota.
- Administrar las vacunas aplicadas a cada mascota.
- Asociar documentos o imágenes con una mascota.
- Guardar la información permanentemente en archivos JSON.
- Recuperar automáticamente los datos previamente almacenados.

---

## Estructura y Diseño del proyecto

```text
C:.
│   consultas.py
│   documentos.py
│   main.py
│   mascotas.py
│   README.md
│   vacunas.py
│
├── Datos
│   │   consultas.json
│   │   documentos.json
│   │   mascotas.json
│   │   vacunas.json
│   │
│   └── documentos
│       ├── 0001
│       │       Mascota2.jpg
│       │
│       └── 11
│               Mascota1.jpg
│
├── Documentos
│       Kiss.jpg
│       Mascota1.jpg
│       Mascota2.jpg
│       Oddy.jpg
│       Peluzon.jpg
│
└── __pycache__
        consultas.cpython-313.pyc
        documentos.cpython-313.pyc
        mascotas.cpython-313.pyc
        vacunas.cpython-313.pyc
```

---

## Descripción de los archivos

| Archivo o carpeta | Descripción |
| :--- | :--- |
| `main.py` | Archivo principal desde el cual se inicia y controla el sistema. |
| `mascotas.py` | Contiene las funciones para administrar los datos de las mascotas. |
| `consultas.py` | Contiene las funciones relacionadas con las consultas veterinarias. |
| `vacunas.py` | Administra los registros de vacunación de las mascotas. |
| `documentos.py` | Gestiona los documentos e imágenes asociados con cada mascota. |
| `Datos/` | Carpeta utilizada para almacenar permanentemente los archivos JSON. |
| `Datos/documentos/` | Guarda los documentos organizados según el código de cada mascota. |
| `Documentos/` | Contiene los archivos originales que pueden asociarse con las mascotas. |
| `__pycache__/` | Carpeta creada automáticamente por Python para almacenar archivos compilados. |
| `README.md` | Contiene la descripción, estructura e instrucciones del proyecto. |

---

## Formatos seleccionados para la persistencia

| Información | Formato seleccionado | Justificación |
| :--- | :---: | :--- |
| **Mascotas** | JSON | JSON permite guardar de forma ordenada todos los datos de cada mascota, como código, nombre, especie, propietario y estado. Además, es fácil de leer, modificar y procesar desde el programa, y permite agregar nuevos campos en el futuro. |
| **Consultas** | JSON | Cada consulta contiene varios datos relacionados y debe asociarse con una mascota mediante su código. JSON facilita guardar múltiples consultas, buscarlas y relacionarlas claramente con cada mascota. |
| **Vacunas** | JSON | Una mascota puede tener varias vacunas, por lo que JSON permite manejar fácilmente listas de registros y relacionarlas con el código de la mascota. También facilita agregar nuevas vacunas sin modificar toda la estructura. |
| **Documentos** | JSON y archivos organizados en carpetas | JSON permite guardar la información de cada archivo asociado con una mascota, como su nombre, tipo y ubicación. Los archivos reales, como fotografías o documentos PDF, se almacenan en carpetas, mientras que en JSON se guarda su ruta. |

---


```text
+-------------+----------------------+-----------------------------------------+
| Información | Formato seleccionado | Forma de almacenamiento                 |
+-------------+----------------------+-----------------------------------------+
| Mascotas    | JSON                 | Datos/m mascotas.json                   |
| Consultas   | JSON                 | Datos/consultas.json                    |
| Vacunas     | JSON                 | Datos/vacunas.json                      |
| Documentos  | JSON + archivos      | Datos/documentos.json y subcarpetas     |
+-------------+----------------------+-----------------------------------------+
```

> Corrección de la primera ruta: el archivo correspondiente a mascotas es `Datos/mascotas.json`.

```text
+-------------+----------------------+-----------------------------------------+
| Información | Formato seleccionado | Forma de almacenamiento                 |
+-------------+----------------------+-----------------------------------------+
| Mascotas    | JSON                 | Datos/mascotas.json                     |
| Consultas   | JSON                 | Datos/consultas.json                    |
| Vacunas     | JSON                 | Datos/vacunas.json                      |
| Documentos  | JSON + archivos      | Datos/documentos.json y subcarpetas     |
+-------------+----------------------+-----------------------------------------+
```

---

## Organización de los datos

La información principal se almacena en los siguientes archivos:

```text
Datos/
├── mascotas.json
├── consultas.json
├── vacunas.json
└── documentos.json
```

Los documentos asociados con las mascotas se organizan en subcarpetas identificadas con el código de cada mascota:

```text
Datos/documentos/
├── 0001/
│   └── Mascota2.jpg
└── 11/
    └── Mascota1.jpg
```

Esta organización permite relacionar fácilmente cada documento con la mascota correspondiente.