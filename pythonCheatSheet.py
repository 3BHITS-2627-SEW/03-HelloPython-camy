## Dies ist ein kleines Cheat Sheet fuer die 
## Anwendung von Python fuer C und C++ Programmierer
eineVariable = 13
print("EineVariable", eineVariable)
eineVariable = " blablabla"
print ("eineVariable", eineVariable)
# Typisierung in Python: Ducktyping
# Daher: bitte immer nach Moeglichkeit typisieren:
eineZweiteVariable : int = 14
print ("eineZweiteVariable", eineZweiteVariable**3)
eineZweiteVariable = "Text"
# erzeugt leider erste den Fehler zur Laufzeit
#print("eineZweiteVaraible", eineZweiteVariable**3)
datenTyp = type(eineVariable)
print("Datentyp von eineVariable: ", datenTyp)
eineVariable = 15
datenTyp = type(eineVariable)
print("Datentyp von eineVariable: ", datenTyp)

# formatierte Ausgabe
# C: printf("Zahl lautet %i und ist Cool")
# print("Zahl lautet %i \n und ist Cool", eineVariable)
#formatierte Strings
einText = f"Zahl lautet %i \n und ist Cool!"
print(einText)
#alternativText = "Zahl lautet "+(eineVariable**2)+" \n und ist Cool"
print(einText)
#print("Alternativ-Text:", alternativText)
# int i = 0;
# printf("Bitte Zahl eingeben: \n");
# scanf(&i);
eingeleseneZahl = input("Bitte eine Zahl eingeben: ")
print("Zahl eingelesen vom Typ", type (eingeleseneZahl))