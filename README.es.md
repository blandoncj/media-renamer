# 📂 Media Renamer

[🇬🇧 Read in English](./README.md)

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

Una herramienta de **línea de comandos (CLI)** simple e intuitiva para renombrar
fotos y videos masivamente con números secuenciales o prefijos personalizados.
Soporta una variedad de formatos (JPEG, PNG, MP4, MOV, etc), incluye un modo
_dry-run_ para previsualizar los cambios de forma segura y muestra el progreso
con una interfaz colorida en la terminal.

---

## 🎥 Demo

![demo](assets/demo.gif)

---

## ✨ Características

- Renombrado masivo para fotos **y** videos
- Prefijo personalizable (`vacaciones_001.jpg`)
- Modo _dry-run_ (previsualización sin renombrar)
- Progress bar and colorful console output
- Soporte para formatos de imagen y vide más comunes

---

## 🚀 Instalación

1. Clona el repositorio:

   ```bash
     git clone git@github.com:blandoncj/media-renamer.git
     cd media-renamer
   ```

2. Crea un entorno virtual y actívalo:

   ```bash
     python -m venv .venv
     source venv/bin/activate  # On Windows use `.venv\Scripts\activate`
   ```

3. Instala las dependencias:

   ```bash
     pip install -r requirements.txt
   ```

---

## ▶️ Uso

Ejecuta la herramienta directamente desde la terminal:

- **Simulación (previsualización sin renombrar):**

  ```bash
    python main.py /ruta/a/tus/medios --dry-run
  ```

- **Renombrar con un prefijo:**

  ```bash
    python main.py /ruta/a/tus/medios --prefix vacaciones
  ```

- **Renombrar sin prefijo:**

  ```bash
    python main.py /ruta/a/tus/medios
  ```

Ejemplo de resultado:

```console
  📂 Processing 5 files in 'media'
  ✔ IMG_1234.JPG → vacaciones_001.jpg
  ✔ IMG_5678.PNG → vacaciones_002.png
  ✔ video1.MP4   → vacaciones_003.mp4

```

---

## 🛠️ Tecnologías

- Python 3.8+
- [Typer](https://typer.tiangolo.com/) para el manejo de argumentos CLI
- [Rich](https://rich.readthedocs.io/en/stable/) para salida colorida en la terminal
- [Tqdm](https://github.com/tqdm/tqdm) para barras de progreso

---

## 📜 Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE)
para más detalles.

---

## 💡 Contribuciones

¡Las contribuciones, problemas y solicitudes de nuevas funcionalidades son bienvenidas!
No dudes en abrir un **PR** o contactarme.

---

Hecho con ❤️ por [blandoncj](https://github.com/blandoncj)
