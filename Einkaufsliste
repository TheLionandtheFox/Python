einkaufsliste = []

while True:
    aktion = input("Möchtest du einen Artikel hinzufügen, entfernen oder anzeigen? (hinzufügen/entfernen/anzeigen/beenden ")

    #hinzufügen von Artikeln
    if aktion == "hinzufügen":
        artikel = input("Welchen Artikel möchtest du hinzufügen? ")
        einkaufsliste.append(artikel)
        print(f"Artikel {artikel} wurde hinzugefügt.")

    # entfernen von Artikeln
    elif aktion == "entfernen":
        artikel = input("Welchen Artikel möchtest du entfernen? ")
        if artikel in einkaufsliste:
            einkaufsliste.remove(artikel)
            print(f"Artikel {artikel} wurde entfernt.")
        else:
            print(f"Artikel {artikel} nicht gefunden.")

    # anzeigen von Artikeln
    elif aktion == "anzeigen":
        print(f"Deine Liste beinhaltet die Artikel {einkaufsliste}.")

    # beenden
    elif aktion == "beenden":
        print(f"Deine Einkaufsliste ist fertig. Das sind deine Artikel: {einkaufsliste}")
        break

    #bei Tippfehler
    else:
        print("Du hast dich vertippt. Bitte versuche es nochmal.")
