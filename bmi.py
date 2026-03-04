def oblicz_bmi(masa, wzrost):
    return masa/(wzrost**2)

def interpretacja_bmi(bmi):
    if bmi < 18.5:
        return "niedowaga"
    elif bmi <= 25:
        return "waga prawidłowa"
    elif bmi <= 30:
        return "nadwaga"
    else:
        return "otyłość"

masa = float(input("Podaj masę ciała (w kilogramach): "))
wzrost = float(input("Podaj wzrost (w metrach): "))

bmi = oblicz_bmi(masa, wzrost)
print(f"BMI = {bmi:.2f}")
print(interpretacja_bmi(bmi))