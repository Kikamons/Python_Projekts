print("Ir sācies vasaras brīvlaiks!")
print("Tu ar saviem diviem draugiem, Tomasu un Jāni, esat izdomājuši apmeklēt spocīgu māju!")
print("Vai vēlies iet iekšā viens pats, ar draugiem vai iet mājās?")
print("")
print("Izvēles opcijas: Viens, Kopā vai Iet mājās")
nauda = 0
sakums = input("> ")
if sakums.lower().strip() == "viens":
    print("Viens")
elif sakums.lower().strip() == "kopā":
    print("Kopā")
else:
    print("Mājas")