import time

heure = (0, 0, 0)
alarme = None

def afficher_heure(h):
    global heure
    heure = h

def regler_alarme(h):
    global alarme
    alarme = h

def afficher_heure_actuelle():
    global heure, alarme
    while True:
        heure_actuelle = time.localtime()
        heure = (heure_actuelle.tm_hour, heure_actuelle.tm_min, heure_actuelle.tm_sec)
        if alarme is not None and heure == alarme:
            print("ALARME !!")
        print(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}")
        time.sleep(1)

afficher_heure_actuelle()