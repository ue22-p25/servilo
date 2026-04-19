from pathlib import Path
from http.server import ThreadingHTTPServer


class Réponse:
    def __init__(self, texte="", code=200, headers=None):
        self.texte = texte
        self.code = code
        self.headers = headers or {}


def réponse_pour_route(route, verbe, headers, form):
    réponse = Réponse()

    print(f"{route=} {verbe=}")

    réponse = Réponse()

    nom_fichier = route[1:]
    if not nom_fichier:
        nom_fichier = "index.html"

    chemin = Path(nom_fichier)

    extension = chemin.suffix
    if extension == ".html":
        content_type = "text/html;charset=utf-8"
    else:
        content_type = "text/css"

    réponse.texte = chemin.read_text()
    réponse.headers["Content-Type"] = content_type

    return réponse
