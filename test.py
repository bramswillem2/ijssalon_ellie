mijn_lijst2 = [(12,3), (12,2), (10,5), (100,20)]
def mijn_functie(a,b):
    global mijn_lijst2
    if (a,b) in mijn_lijst2:
        return [a + b, a - b, a * b, a / b]
    else:
        return "niets"
print (mijn_functie(12,2))

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
        btw_bedrag = totaal * btw
        uitvoer = f"het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden"
        return uitvoer
print(inkomsten_totaal([200,100,300],0.21))

def laag_en_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer
print(laag_en_hoog([100,20,10]))

def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)
    uitvoer = [tijdelijk[0],tijdelijk[1]]
    return uitvoer
print(meervoudig([150,5,20,50]))


