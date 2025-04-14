from algemene_functies import mijn_functie_2

def mijn_aanbieding_1(smaak, prijs, korting):    
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro"
    return uitvoer
print (mijn_aanbieding_1 ("aardbei", 4, 0.1)) 

lijst_inkomsten = [220, 430, 125, 160, 205, 90, 345]
def inkomsten_totaal(inkomsten, btw):
    global lijst_inkomsten
    inkomsten = sum(lijst_inkomsten)
    btw_bedrag = inkomsten * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {inkomsten}, waarover {btw_bedrag} euro btw betaald dient te worden"
    return uitvoer
print(inkomsten_totaal(lijst_inkomsten, 0.09))

def laag_en_hoog(mijn_lijst):
    global lijst_inkomsten
    mijn_lijst = max(lijst_inkomsten), min(lijst_inkomsten)
    return mijn_lijst
print(laag_en_hoog(lijst_inkomsten))

def gemiddelde(mijn_lijst):
    global lijst_inkomsten
    mijn_lijst = sum(lijst_inkomsten) / len(lijst_inkomsten)
    uitvoer = f"De gemiddelde inkomsten deze week zijn {mijn_lijst} euro."
    return uitvoer
print(gemiddelde(lijst_inkomsten))

lijst_hoog_laag = [10,5,3,2,1,2,9]
def meervoudig(invoer_lijst):
    global lijst_hoog_laag
    invoer_lijst = laag_en_hoog(lijst_hoog_laag)
    return invoer_lijst
print(meervoudig(lijst_hoog_laag))


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie(100))