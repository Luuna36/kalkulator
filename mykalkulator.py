def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        return "Błąd: nie można dzielić przez zero."
    return a / b

def kalkulator():
    print("Witaj w kalkulatorze!")
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wprowadź numer operacji (1/2/3/4): ")

    if wybor in ['1', '2', '3', '4']:
        a = float(input("Wprowadź pierwszą liczbę: "))
        b = float(input("Wprowadź drugą liczbę: "))

        if wybor == '1':
            print(f"Wynik: {a} + {b} = {dodawanie(a, b)}")
        elif wybor == '2':
            print(f"Wynik: {a} - {b} = {odejmowanie(a, b)}")
        elif wybor == '3':
            print(f"Wynik: {a} * {b} = {mnozenie(a, b)}")
        elif wybor == '4':
            print(f"Wynik: {a} / {b} = {dzielenie(a, b)}")
    else:
        print("Nieprawidłowy wybór operacji!")

# Uruchom kalkulator
kalkulator()
