"""
main.py
=======
Le fichier principal, équivalent simplifié de sherlock.py (la fonction main()).

Il fait 3 choses :
1. Récupère le pseudo tapé par l'utilisateur
2. Lance check_one_site() sur TOUS les sites EN PARALLÈLE (sinon ce serait trop lent)
3. Affiche les résultats

Usage :
    python3 main.py pseudo_a_chercher
"""

import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from sites_data import SITES
from checker import check_one_site


def search_username(username):
    print(f"\n[*] Recherche du pseudo : {username}\n")

    results = []

    # ThreadPoolExecutor = lance plusieurs requêtes EN MEME TEMPS (threads)
    # max_workers=10 -> 10 sites checkés simultanément au lieu d'un par un
    # C'est l'équivalent simplifié du FuturesSession(max_workers=20) du vrai Sherlock
    with ThreadPoolExecutor(max_workers=10) as executor:

        # On lance une tâche par site, on garde une référence (future) vers chacune
        futures = {
            executor.submit(check_one_site, username, name, info): name
            for name, info in SITES.items()
        }

        # as_completed() nous donne les résultats AU FUR ET A MESURE
        # qu'ils arrivent, pas forcément dans l'ordre de départ
        for future in as_completed(futures):
            result = future.result()
            results.append(result)

            if result["exists"] is True:
                print(f"[+] TROUVÉ   : {result['site']:<15} -> {result['url']}")
            elif result["exists"] is False:
                print(f"[-] absent   : {result['site']}")
            else:
                print(f"[!] erreur   : {result['site']} ({result['error']})")

    return results


def main():
    if len(sys.argv) != 2:
        print("Usage : python3 main.py <pseudo>")
        sys.exit(1)

    username = sys.argv[1]
    results = search_username(username)

    found_count = sum(1 for r in results if r["exists"] is True)
    print(f"\n[*] Terminé. {found_count} compte(s) trouvé(s) sur {len(results)} sites checkés.\n")


if __name__ == "__main__":
    main()
