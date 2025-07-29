# 🎧 DownloadPy

Automatiza la descarga y conversión de medios con Python. Este proyecto permite gestionar videos y audios usando cookies de sesión y enlaces extraídos.

## 🗂️ Estructura

- `descargar.py` / `descargarv2.py`: Scripts para descarga de medios.
- `convertir.py`: Convierte archivos descargados.
- `media_links.json`: Contiene enlaces de medios.
- `cookies.json` / `cookies.txt`: Cookies para autenticación. *No se versionan*.
- `BOTIC-SOFOF...mp4`: Ejemplo de archivo descargado.
- `.gitignore`: Protección contra archivos sensibles.

## ⚙️ Instalación

```bash
git clone https://github.com/LordAlphons/downloadpy.git
cd downloadpy
pip install -r requirements.txt

🚀 Uso
- Asegúrate de tener cookies válidas en cookies.json.
- Ejecuta el script para descargar:
python descargar.py
- (Opcional) Convierte el archivo:
python convertir.py


🛡️ Seguridad
- Archivos como .env, .txt y .json están ignorados vía .gitignore.
- No subas cookies válidas al repositorio público.
📄 Licencia
Este proyecto está bajo la Licencia MIT.
