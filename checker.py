"""
checker.py
==========
Ce fichier contient UNE seule fonction : check_one_site.
Son job : prendre un pseudo + les infos d'un site, et répondre "existe" ou "existe pas".

C'est l'équivalent simplifié de la fonction query_site() dans le vrai Sherlock.
"""

import requests

# On met un user-agent "normal" sinon certains sites bloquent direct les requêtes
# qui ressemblent trop à un script automatisé.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


def check_one_site(username, site_name, site_info):
    """
    username   : le pseudo qu'on cherche, ex "Ilan"
    site_name  : le nom du site, ex "GitHub"
    site_info  : le dict avec "url" et "method" (vient de sites_data.py)

    Retourne un dict avec le résultat.
    """
    url = site_info["url"].format(username)  # remplace {} par le pseudo

    try:
        # timeout=5 : si le site met plus de 5s à répondre, on abandonne
        # ça évite que le script reste bloqué sur un site qui ne répond pas
        response = requests.get(url, headers=HEADERS, timeout=5)
    except requests.RequestException as e:
        # Si la requête plante (site hors ligne, pas internet, etc.)
        return {
            "site": site_name,
            "url": url,
            "exists": None,  # None = on sait pas, erreur technique
            "error": str(e),
        }

    # --- Logique de détection ---
    if site_info["method"] == "status_code":
        # La méthode la plus simple : 200 = la page existe = compte existe
        exists = response.status_code == 200

    elif site_info["method"] == "text_absent":
        # Le site renvoie toujours 200, donc on regarde le contenu HTML
        # Si le message d'erreur N'EST PAS dans la page -> le compte existe
        error_text = site_info.get("error_text", "")
        exists = error_text not in response.text

    else:
        exists = False

    return {
        "site": site_name,
        "url": url,
        "exists": exists,
        "error": None,
    }
