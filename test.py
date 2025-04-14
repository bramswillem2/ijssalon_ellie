mijn_lijst2 = [(12,3), (12,2), (10,5), (100,20)]
def mijn_functie(a,b):
    global mijn_lijst2
    if (a,b) in mijn_lijst2:
        return [a + b, a - b, a * b, a / b]
    else:
        return "niets"
print (mijn_functie(12,2))