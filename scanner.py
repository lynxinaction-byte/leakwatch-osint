import requests

def envoyer_alerte_discord(message):
    
    webhook_url = "https://discord.com/api/webhooks/1458502851990126652/mjIDTCVP43xIUvUQHZz1A2agNSmuptUf-vZIaChv2G9EveJJB9wZv10hDRUzHa0Cl9MT" 
    data = {"content": message}
    try:
        requests.post(webhook_url, json=data)
    except:
        print("Erreur d'envoi Discord")

def scanner_tout():
    try:
        with open("cibles.txt", "r") as f:
            lignes = f.readlines()
            
        for ligne in lignes:
            # On sépare l'URL du mot-clé grâce à la virgule
            url, mot_cle = ligne.strip().split(",")
            print(f"Analyse de {url} pour le mot '{mot_cle}'...")
            
            reponse = requests.get(url, timeout=10)
            if mot_cle.lower() in reponse.text.lower():
                envoyer_alerte_discord(f"🚨 **MATCH !** '{mot_cle}' trouvé sur {url}")
                
    except Exception as e:
        print(f"Erreur lors du scan : {e}")

if __name__ == "__main__":
    scanner_tout()
