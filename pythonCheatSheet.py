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