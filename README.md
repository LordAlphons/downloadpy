🎧 DownloadPy
Automatiza la descarga y conversión de medios con Python. Este proyecto permite gestionar videos y audios protegidos mediante cookies de sesión y enlaces extraídos manualmente.

🗂️ Estructura del proyecto
- descargarv2.py: Script principal para descargar medios desde una URL específica.
- convertir.py: Convierte cookies en formato .json a .txt para compatibilidad con yt-dlp.
- media_links.json: Contenedor de enlaces de medios recopilados.
- cookies.json / cookies.txt: Cookies para autenticación. No deben versionarse.
- *.mp4: Ejemplos de archivos descargados (no incluidos).
- .gitignore: Protege credenciales y archivos sensibles.

⚙️ Instalación
git clone https://github.com/LordAlphons/downloadpy.git
cd downloadpy
pip install -r requirements.txt



🧩 Flujo de uso
- Ejecuta el script de descarga Edita el archivo descargarv2.py y asegúrate de incluir la URL del video:
python descargarv2.py "https://ejemplo.com/video"
- Convierte las cookies Una vez generadas las cookies en formato .json, transforma a .txt para usar con yt-dlp:
python convertir.py
- Descarga el video con yt-dlp Utiliza el archivo cookies.txt con el comando:
yt-dlp --cookies cookies.txt "https://ejemplo.com/video"



📂 Acceso restringido
Para que la descarga funcione correctamente, debes haber sido invitado a la carpeta privada que contiene el video. Sin acceso autorizado, el contenido no será accesible.

🛡️ Seguridad
- Cookies, credenciales y archivos .env están protegidos por .gitignore.
- Nunca subas cookies reales o archivos sensibles al repositorio público.

📄 Licencia
Este proyecto está bajo la Licencia MIT.

