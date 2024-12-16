from datetime import datetime, timedelta


def saisir_distance():
    while True:
        try:
            distance = float(
                input("Entrez la distance parcourue par les pigeons (en mètres) : "))
            if distance <= 0:
                print("La distance doit être un nombre positif.")
                continue
            return distance
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre pour la distance.")


def saisir_nombre_pigeons():
    while True:
        try:
            nombre = int(input("Entrez le nombre de pigeons : "))
            if nombre <= 0:
                print("Le nombre de pigeons doit être un entier positif.")
                continue
            return nombre
        except ValueError:
            print("Entrée invalide. Veuillez entrer un entier pour le nombre de pigeons.")


def saisir_heure(prompt):
    while True:
        heure_str = input(prompt)
        try:
            return datetime.strptime(heure_str, "%H:%M")
        except ValueError:
            print("Format invalide. Veuillez entrer l'heure au format HH:MM.")


def main():
    print("# Programme de calcul des résultats d'un concours de pigeons voyageurs\n")

    # Saisie des données
    distance = saisir_distance()
    nombre_pigeons = saisir_nombre_pigeons()

    pigeons = []

    # Heure de départ
    heure_lacher = "08:00"  # Vous pouvez rendre cela dynamique si nécessaire
    tps_depart = datetime.strptime(heure_lacher, "%H:%M")

    # Collecte des données pour chaque pigeon
    for i in range(nombre_pigeons):
        print(f"\n--- Pigeon {i + 1} ---")
        nom = input("Entrez le nom ou numéro du pigeon : ").strip()
        heure_arrivee = saisir_heure(
            f"Entrez l'heure d'arrivée du pigeon {nom} (format HH:MM) : ")

        # Gérer le cas où l'arrivée est le lendemain
        if heure_arrivee < tps_depart:
            # Ajouter un jour à l'heure d'arrivée
            tps_arrivee = heure_arrivee + timedelta(days=1)
        else:
            tps_arrivee = heure_arrivee

        # Calcul du temps de vol en minutes
        temps_vol = (tps_arrivee - tps_depart).total_seconds() / \
            60  # Conversion en minutes

        # Calcul de la vitesse en m/min
        vitesse = distance / temps_vol if temps_vol > 0 else 0  # Éviter la division par zéro

        # Ajouter les données du pigeon à la liste
        pigeons.append((nom, vitesse))

    # Classement par vitesse décroissante
    pigeons.sort(key=lambda x: x[1], reverse=True)

    # Affichage des résultats
    print("\nRésultats du concours :")
    print("{:<5} | {:<15} | {:>15}".format(
        "Rang", "Pigeon", "Vitesse (m/min)"))
    print("-" * 40)
    for rang, (nom, vitesse) in enumerate(pigeons, start=1):
        print("{:<5} | {:<15} | {:>15.2f}".format(rang, nom, vitesse))


if __name__ == "__main__":
    main()
