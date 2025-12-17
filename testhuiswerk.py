inkomsten={
    "Aardbeien-ijs-totaal":1000,
    "Vanille-ijs-totaal":2000,
    "Chocolade-ijs-totaal":1500,
    "Waterijsjes-totaal":750
}

def som(inkomsten):
    optel=sum(inkomsten.values())
    return optel

for key in inkomsten:
    print(key)

for value in inkomsten.values():
    print(value)

for key, value in inkomsten.items():
    print(f"{key} : {value} euro")
print(40 * "=")
print(f"Totaal: {som(inkomsten)} euro")

def presenteer(inkomsten, value):
    print(f"Aardbeien-ijs-totaal:", inkomsten["Aardbeien-ijs-totaal"])
    print(f"Vanille-ijs-totaal:", inkomsten["Vanille-ijs-totaal"])
    print(f"Chocolade-ijs-totaal:", inkomsten["Chocolade-ijs-totaal"])
    print(f"Waterijsjes-totaal:", inkomsten["Waterijsjes-totaal"])
    print(40*"=")
    print(f"Totaal: {som(inkomsten)} euro")
print(presenteer(inkomsten, value))



















