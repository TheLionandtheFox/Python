'''
Python for-Schleifen, die auf verschiedene Arten eingesetzt werden. 
Es ist derselbe Ausgang, aber mit unterschiedlichen Methoden.
In diesem Beispiel wird eine Liste von Preisen durchlaufen.
Ziel: Alle Preise, die kleiner oder gleich 1200 sind, 
in die Liste 'bezahlbar' zu speichern.
'''

preise = [6000, 2500, 210, 100, 3050, 1500, 1000, 75, 800, 500, 100, 430]
bezahlbar = []

'''
1. Standard-Iteration (Direkter Zugriff):
Das ist die häufigste (einfachste) Form, 
bei der jedes Element der Liste direkt angesprochen wird .
'''
bezahlbar = []

# Jedes Element 'i' wird nacheinander aus der Liste 'preise' gezogen

for i in preise:
    if i <= 1200:
        bezahlbar.append(i)
    else:
        print(f"1.{i} ist zu teuer.")

print(f"1. Bezahlbare Preise sind: {bezahlbar}.")


'''
2. Numerische Schleife mit range():
Hier nutzen wir den Index (die Position), um auf die Elemente zuzugreifen. 
Sinnvoll, wenn man die Position im Code verändern oder berechnen muss.
'''
bezahlbar = [] 
for i in range(len(preise)):
    if preise[i] <= 1200:
        bezahlbar.append(preise[i])
    else:
        print(f"2. Index {i}: {preise[i]} ist zu teuer.")

print(f"2. Bezahlbare Preise sind: {bezahlbar}.")


'''
3. Iteration mit enumerate():
Diese Variante kombiniert den Index und den Wert.
Wir erhalten zwei Informationen gleichzeitig: 
Den Index (idx) und den eigentlichen Wert (i).
'''
bezahlbar = []
for idx, i in enumerate(preise):
    if i <= 1200:
        bezahlbar.append(i)
    else:
        print(f"3. Position {idx} im Regal: {i} ist zu teuer.")

print(f"3. Bezahlbare Preise sind: {bezahlbar}.")


'''
4. Iteration über Dictionaries:
Wenn Preise Produkten zugeordnet sind, 
iteriert man über Schlüssel-Wert-Paare.
Heißt: Hier sind die Preise an Namen gekoppelt. 
'produkt' ist der Name, 'i' ist der Preis.
'''
katalog = {"Fernseher": 6000, "Handy": 500, "Kabel": 10}
# .items() gibt sowohl den Namen (Key) als auch den Preis (Value) zurück
for produkt, i in katalog.items():
    if i <= 1200:
        print(f"4. {produkt} kostet {i} und ist bezahlbar.")
    else:
        print(f"4. {produkt} kostet {i} und ist zu teuer.")


'''
5. List Comprehension (Kompakte Form):
Dies ist ein Spezialfall der for-Schleife, 
um eine neue Liste in einer einzigen Zeile zu erstellen.
Das 'i' links ist das, was in die Liste geschrieben wird.
'''

# Erstelle die Liste 'bezahlbar' direkt durch Filtern der 'preise'
bezahlbar = [i for i in preise if i <= 1200]
# Für die Fehlermeldungen müsste man dennoch eine normale Schleife nutzen
print(f"5. Bezahlbar (kompakt): {bezahlbar}")


'''
6. Die for ... else Besonderheit
Das 'else' gehört hier zur 'for'-Schleife, nicht zum 'if'.
Der else-Block wird nur ausgeführt, 
wenn die Schleife nicht durch ein break abgebrochen wurde.'''
limit = 7000
for i in preise:
    if i > limit:
        print(f"6. Abbruch: {i} ist über dem absoluten Limit!")
        break 
else:
    # Dieser Teil erscheint nur, wenn kein einziges 'i' das Limit gesprengt hat
    print("6. Check bestanden: Kein Preis war ueber dem Limit.")
