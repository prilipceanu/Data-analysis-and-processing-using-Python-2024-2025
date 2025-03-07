
#V1 - filter + functie
lista = [12, 2, 31, 50, 300, 10]

def lungimea_5(intreg):
    return intreg > 5


print(list(filter(lungimea_5, lista)))

[intreg for intreg in lista if intreg > 5]