import requests
import json
import sys

from config import API_KEY_PREFIX, API_KEY_SECRET, DOMINIO


def crear_registro_txt_si_no_existe(subdominio, url_larga):
    """
    Comprueba si un registro TXT existe y, si no, lo crea.
    """
    nombre_completo_registro = f"{subdominio}.{DOMINIO}"
    headers = {
        "X-API-Key": f"{API_KEY_PREFIX}.{API_KEY_SECRET}",
        "Content-Type": "application/json"
    }

    try:
        # 1. Obtener registros actuales para comprobar si ya existe
        url_api_get = f"https://api.hosting.ionos.com/dns/v1/zones/{DOMINIO}"
        respuesta = requests.get(url_api_get, headers=headers)
        respuesta.raise_for_status()

        registros_actuales = respuesta.json().get('records', [])
        
        for registro in registros_actuales:
            if registro['type'] == 'TXT' and registro['name'] == nombre_completo_registro:
                return # Si existe, termina la función sin hacer nada

        # 2. Si no existe, lo creamos
        nuevo_registro_data = [
            {
                "name": nombre_completo_registro,
                "type": "TXT",
                "content": f'"{url_larga}"',
                "ttl": 3600
            }
        ]
        
        url_api_patch = f"https://api.hosting.ionos.com/dns/v1/zones/{DOMINIO}"
        requests.patch(url_api_patch, headers=headers, data=json.dumps(nuevo_registro_data)).raise_for_status()

    except requests.exceptions.HTTPError as err:
        sys.stderr.write(f"ERROR de API: {err.response.status_code} - {err.response.text}\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"ERROR INESPERADO: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    crear_registro_txt_si_no_existe("google", "https://www.google.com")
    crear_registro_txt_si_no_existe("you", "https://www.youtube.com/")