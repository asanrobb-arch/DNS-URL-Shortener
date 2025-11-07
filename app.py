from flask import Flask, redirect, abort
import dns.resolver

from config import DOMINIO

app = Flask(__name__)

@app.route('/<path:camino_corto>')
def redirigir(camino_corto):
    """
    Busca el registro TXT y redirige al usuario.
    """
    nombre_completo_registro = f"{camino_corto}.{DOMINIO}"

    try:
        respuestas = dns.resolver.resolve(nombre_completo_registro, 'TXT')
        url_larga = respuestas[0].to_text().strip('"')
        return redirect(url_larga, code=302)
    except dns.resolver.NXDOMAIN:
        return abort(404) # Error: No encontrado
    except Exception:
        return abort(500) # Error: Problema en el servidor

@app.route('/')
def inicio():
    return "Acortador de URL activo."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)