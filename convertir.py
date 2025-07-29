import json

def convertir_a_netscape(json_path, txt_path="cookies.txt"):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            cookies = json.load(f)

        with open(txt_path, "w", encoding="utf-8") as f_out:
            f_out.write("# Netscape HTTP Cookie File\n")
            for cookie in cookies:
                # Validar campos mínimos
                nombre = cookie.get("name")
                valor = cookie.get("value")
                dominio = cookie.get("domain")
                path = cookie.get("path", "/")
                secure = "TRUE" if cookie.get("secure", False) else "FALSE"

                # Flag de subdominio: usar TRUE si el dominio empieza con "."
                flag = "TRUE" if dominio.startswith(".") else "FALSE"

                if all([nombre, valor, dominio]):
                    linea = f"{dominio}\t{flag}\t{path}\t{secure}\t{nombre}\t{valor}\n"
                    f_out.write(linea)

        print(f"✅ Conversión completa. Archivo guardado como {txt_path}")
    except Exception as e:
        print(f"❌ Error durante la conversión: {e}")

# Ejecutar conversión
convertir_a_netscape("cookies.json")