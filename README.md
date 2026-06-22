# 🔍 search-name

Outil OSINT léger pour rechercher un pseudo sur **40+ sites** (réseaux sociaux, gaming, dev, musique...)

Inspiré de Sherlock, écrit from scratch pour apprendre.

---

## 📦 Installation

```bash
git clone https://github.com/grrrbam/search-name.git
cd search-name
pip install requests
```

## 🚀 Utilisation

```bash
python main.py pseudo_a_chercher
```

### Exemple

```bash
python main.py torvalds
```

## 🌐 Sites checkés

- Réseaux sociaux : Instagram, TikTok, Snapchat, Pinterest, Mastodon...
- Dev / Tech : GitHub, GitLab, Replit, CodePen, Dev.to...
- Gaming : Steam, Twitch, Roblox, Chess.com...
- Musique : SoundCloud, Spotify, Bandcamp...
- Vidéo : YouTube, Vimeo, Dailymotion...
- Pro : LinkedIn, Behance, Dribbble, Medium...

## ⚠️ Usage légal uniquement

Cet outil recherche uniquement des **profils publics**.
Ne pas utiliser pour harceler ou traquer quelqu'un.

## 📁 Structure

| Fichier | Rôle |
|---|---|
| `main.py` | Lance la recherche en parallèle |
| `checker.py` | Vérifie un site |
| `sites_data.py` | Liste des sites |
