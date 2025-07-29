# 🎧 DownloadPy

Automatiza la descarga y conversión de medios con Python. Este proyecto permite gestionar videos y audios usando cookies de sesión y enlaces extraídos.

## 🗂️ Estructura

- `descargar.py` / `descargarv2.py`: Scripts para descarga de medios.
- `convertir.py`: Convierte archivos descargados.
- `media_links.json`: Contiene enlaces de medios.
- `cookies.json` / `cookies.txt`: Cookies para autenticación. *No se versionan*.
- `*...mp4`: Ejemplo de archivo descargado.
- `.gitignore`: Protección contra archivos sensibles.

## ⚙️ Instalación

```bash
git clone https://github.com/LordAlphons/downloadpy.git
cd downloadpy
pip install -r requirements.txt

🧩 Flujo de uso
Edita y Ejecuta descargarv2.py incluyendo la URL del video que deseas obtener al final del archivo:
python descargarv2.py "https://ejemplo.com/video"

Una vez obtenidas las cookies en formato .json, usa convertir.py para convertirlas a .txt:
python convertir.py
- Usar yt-dlp
Con el archivo cookies.txt ya generado, descarga el video directamente con yt-dlp:
yt-dlp --cookies cookies.txt "https://ejemplo.com/video"

📂 Nota importante:
Para acceder al video y usar correctamente los scripts, debes haber sido invitado a la carpeta privada que contiene el recurso. Sin acceso autorizado, la descarga no funcionará correctamente.

🛡️ Seguridad
- Archivos como .env, .txt y .json están ignorados vía .gitignore.
- No subas cookies válidas al repositorio público.
📄 Licencia
Este proyecto está bajo la Licencia MIT.
