# 🎧 DownloadPy

Automatiza la descarga y conversión de medios con Python. Este proyecto permite gestionar videos y audios protegidos mediante cookies de sesión y enlaces extraídos manualmente.

---

## 🗂️ Estructura del proyecto

- `descargarv2.py`: Script principal para descargar medios desde una URL específica.
- `convertir.py`: Convierte cookies en formato `.json` a `.txt`.
- `media_links.json`: Contiene enlaces recopilados.
- `cookies.json` / `cookies.txt`: Cookies para autenticación. **No deben versionarse.**
- `*.mp4`: Ejemplo de archivo descargado.
- `.gitignore`: Protege archivos sensibles como `.env` o cookies.

---

## ⚙️ Instalación

```bash
git clone https://github.com/LordAlphons/downloadpy.git
cd downloadpy
pip install -r requirements.txt
```
---

## 🧩 Flujo de uso
- Ejecutar el script de descarga
Incluye la URL del video:
python descargarv2.py "https://ejemplo.com/video"
- Convertir las cookies
python convertir.py
- Descargar el video con yt-dlp
yt-dlp --cookies cookies.txt "https://ejemplo.com/video"



## 📂 Acceso restringido
Debes haber sido invitado a la carpeta privada que contiene el video. Sin autorización, el recurso no será accesible.

## 🛡️ Seguridad
- Archivos .env, .json, .txt sensibles están ignorados vía .gitignore.
- No subas cookies válidas al repositorio público.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT.

