mijn_lijst = [2, 4, 10, 12]
def mijn_functie(a):
    global mijn_lijst
    if a in mijn_lijst:
        return a **2
    else:
        return "niets"
print (mijn_functie(12))

mijn_lijst2 = [(12,3), (12,2), (10,5), (100,20)]
def mijn_functie_2(a,b):
    global mijn_lijst2
    if (a,b) in mijn_lijst2:
        return [a + b, a - b, a * b, a / b]
    else:
        return "niets"
print (mijn_functie_2(12,3))
