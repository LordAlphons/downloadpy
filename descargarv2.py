from playwright.sync_api import sync_playwright
import json
import os

def validar_cookies(cookies_raw):
    cookies_validadas = []
    for c in cookies_raw:
        required_keys = ["name", "value", "domain", "path"]
        if all(k in c for k in required_keys):
            c.setdefault("secure", True)
            c.setdefault("httpOnly", False)
            cookies_validadas.append(c)
    return cookies_validadas

def extraer_media_links(url_pagina, cookies_path):
    media_links = {"video": [], "audio": [], "headers": []}

    if not os.path.exists(cookies_path):
        print("🚫 Archivo de cookies no encontrado")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Cargar y validar cookies
        with open(cookies_path, "r", encoding="utf-8") as f:
            cookies_raw = json.load(f)
        cookies_validas = validar_cookies(cookies_raw)
        context.add_cookies(cookies_validas)

        page = context.new_page()

        def guardar_media(response):
            tipo = response.headers.get("content-type", "")
            if "video" in tipo or "audio" in tipo:
                info = {
                    "url": response.url,
                    "content-type": tipo,
                    "length": response.headers.get("content-length", "?"),
                    "filename": response.headers.get("content-disposition", "?")
                }
                media_links["headers"].append(info)
                if "video" in tipo:
                    media_links["video"].append(response.url)
                elif "audio" in tipo:
                    media_links["audio"].append(response.url)

        page.on("response", guardar_media)
        print(f"🧠 Visitando: {url_pagina}")
        page.goto(url_pagina, wait_until="networkidle")
        page.wait_for_timeout(10000)  # Espera 10 segundos

        browser.close()

    with open("media_links.json", "w", encoding="utf-8") as f:
        json.dump(media_links, f, indent=2)
    print("✅ Links multimedia guardados en media_links.json")

# Ejemplo de uso
extraer_media_links(
    "URL-AQUI",
    "cookies.json"
)