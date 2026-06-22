"""
sites_data.py
==============
Liste étendue de sites à checker.
Remplace ton fichier sites_data.py actuel par celui-ci.
 
method "status_code" : le site renvoie 404 si le compte n'existe pas
method "text_absent" : le site renvoie toujours 200, mais affiche un message
                       d'erreur dans le HTML -> on vérifie que ce message est ABSENT
"""
 
SITES = {
 
    # --- RÉSEAUX SOCIAUX ---
    "Instagram": {
        "url": "https://www.instagram.com/{}/",
        "method": "status_code",
    },
    "Twitter / X": {
        "url": "https://x.com/{}",
        "method": "status_code",
    },
    "TikTok": {
        "url": "https://www.tiktok.com/@{}",
        "method": "status_code",
    },
    "Snapchat": {
        "url": "https://www.snapchat.com/add/{}",
        "method": "status_code",
    },
    "Pinterest": {
        "url": "https://www.pinterest.com/{}/",
        "method": "status_code",
    },
    "Tumblr": {
        "url": "https://{}.tumblr.com/",
        "method": "text_absent",
        "error_text": "There's nothing here.",
    },
    "Flickr": {
        "url": "https://www.flickr.com/people/{}",
        "method": "status_code",
    },
    "Mastodon": {
        "url": "https://mastodon.social/@{}",
        "method": "status_code",
    },
 
    # --- DEV / TECH ---
    "GitHub": {
        "url": "https://github.com/{}",
        "method": "status_code",
    },
    "GitLab": {
        "url": "https://gitlab.com/{}",
        "method": "status_code",
    },
    "HackerNews": {
        "url": "https://news.ycombinator.com/user?id={}",
        "method": "text_absent",
        "error_text": "No such user.",
    },
    "Replit": {
        "url": "https://replit.com/@{}",
        "method": "status_code",
    },
    "CodePen": {
        "url": "https://codepen.io/{}",
        "method": "status_code",
    },
    "Dev.to": {
        "url": "https://dev.to/{}",
        "method": "status_code",
    },
    "Pastebin": {
        "url": "https://pastebin.com/u/{}",
        "method": "status_code",
    },
    "Bitbucket": {
        "url": "https://bitbucket.org/{}",
        "method": "status_code",
    },
 
    # --- FORUMS / COMMUNAUTÉS ---
    "Reddit": {
        "url": "https://www.reddit.com/user/{}",
        "method": "status_code",
    },
    "Discord (lookup)": {
        "url": "https://discord.com/users/{}",
        "method": "status_code",
    },
    "Steam": {
        "url": "https://steamcommunity.com/id/{}",
        "method": "text_absent",
        "error_text": "The specified profile could not be found.",
    },
    "Twitch": {
        "url": "https://www.twitch.tv/{}",
        "method": "status_code",
    },
    "Kick": {
        "url": "https://kick.com/{}",
        "method": "status_code",
    },
 
    # --- MUSIQUE / CRÉATIFS ---
    "SoundCloud": {
        "url": "https://soundcloud.com/{}",
        "method": "status_code",
    },
    "Spotify (profil)": {
        "url": "https://open.spotify.com/user/{}",
        "method": "status_code",
    },
    "Bandcamp": {
        "url": "https://{}.bandcamp.com/",
        "method": "text_absent",
        "error_text": "Sorry, that something isn't here.",
    },
    "Mixcloud": {
        "url": "https://www.mixcloud.com/{}/",
        "method": "status_code",
    },
 
    # --- VIDÉO ---
    "YouTube": {
        "url": "https://www.youtube.com/@{}",
        "method": "status_code",
    },
    "Dailymotion": {
        "url": "https://www.dailymotion.com/{}",
        "method": "status_code",
    },
    "Vimeo": {
        "url": "https://vimeo.com/{}",
        "method": "status_code",
    },
 
    # --- PRO / PORTFOLIO ---
    "LinkedIn": {
        "url": "https://www.linkedin.com/in/{}",
        "method": "status_code",
    },
    "Behance": {
        "url": "https://www.behance.net/{}",
        "method": "status_code",
    },
    "Dribbble": {
        "url": "https://dribbble.com/{}",
        "method": "status_code",
    },
    "Medium": {
        "url": "https://medium.com/@{}",
        "method": "status_code",
    },
    "Substack": {
        "url": "https://{}.substack.com/",
        "method": "text_absent",
        "error_text": "page not found",
    },
 
    # --- GAMING ---
    "Roblox": {
        "url": "https://www.roblox.com/user.aspx?username={}",
        "method": "text_absent",
        "error_text": "Page cannot be found",
    },
    "Minecraft (NameMC)": {
        "url": "https://namemc.com/profile/{}",
        "method": "status_code",
    },
    "Chess.com": {
        "url": "https://www.chess.com/member/{}",
        "method": "status_code",
    },
    "Lichess": {
        "url": "https://lichess.org/@/{}",
        "method": "status_code",
    },
 
    # --- DIVERS ---
    "Gravatar": {
        "url": "https://en.gravatar.com/{}",
        "method": "status_code",
    },
    "Keybase": {
        "url": "https://keybase.io/{}",
        "method": "status_code",
    },
    "ProductHunt": {
        "url": "https://www.producthunt.com/@{}",
        "method": "status_code",
    },
    "HuggingFace": {
        "url": "https://huggingface.co/{}",
        "method": "status_code",
    },
    "Linktree": {
        "url": "https://linktr.ee/{}",
        "method": "status_code",
    },
    "About.me": {
        "url": "https://about.me/{}",
        "method": "status_code",
    },
}