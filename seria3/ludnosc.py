import matplotlib.pyplot as plt
import json

if __name__ == "__main__":
    plik = open("ludnosc.json")
    dane = json.load(plik)
    plik.close()
    
    wojewodztwo = input("wojewodztwo: ")
    statystyka = input("statystyka: ") #ludność, powierzchnia km2, gęstość zaludnienia
    
    ludnosci = []
    powierzchnie = []
    for rok in dane.keys():
        if wojewodztwo == "Polska":
            suma_ludnosci = 0
            suma_powierzchni = 0
            for woj in dane[rok].keys():
                suma_ludnosci += dane[rok][woj]["ludność"]
                suma_powierzchni += dane[rok][woj]["powierzchnia km2"]
            ludnosci.append(suma_ludnosci)
            powierzchnie.append(suma_powierzchni)
        else:
            ludnosci.append(dane[rok][wojewodztwo]["ludność"])
            powierzchnie.append(dane[rok][wojewodztwo]["powierzchnia km2"])
    
    gestosci = [ludnosci[i]/powierzchnie[i] for i in range(len(ludnosci))]
    
    if statystyka == "ludność":
        plt.plot(range(2013, 2026), ludnosci)
    if statystyka == "powierzchnia km2":
        plt.plot(range(2013, 2026), powierzchnie)
    if statystyka == "gęstość zaludnienia":
        plt.plot(range(2013, 2026), gestosci)
    
    plt.show()
