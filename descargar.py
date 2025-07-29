from playwright.sync_api import sync_playwright
import json

def extraer_media_links(url_pagina, cookies_path):
    media_links = {"video": [], "audio": []}

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Cargar cookies
        with open(cookies_path, "r", encoding="utf-8") as f:
            cookies = json.load(f)
        context.add_cookies(cookies)

        page = context.new_page()

        def guardar_media(response):
            tipo = response.headers.get("content-type", "")
            if "video" in tipo:
                media_links["video"].append(response.url)
            elif "audio" in tipo:
                media_links["audio"].append(response.url)

        page.on("response", guardar_media)
        print(f"Visitando: {url_pagina}")
        page.goto(url_pagina, wait_until="networkidle")
        page.wait_for_timeout(10000)  # Espera 10 segundos

        browser.close()

    with open("media_links.json", "w", encoding="utf-8") as f:
        json.dump(media_links, f, indent=2)
    print("🎯 Links detectados guardados en media_links.json")

# Llamada con cookies
extraer_media_links("https://drive.google.com/file/d/1K79jnPCUqon_BhOJAsRQ5eRPMBU5y46Z/view", "cookies.json")