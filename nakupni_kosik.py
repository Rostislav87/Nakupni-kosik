# TODO proměnné
potraviny = {
    "mleko":    [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso":     [100, 1],
    "banan":    [30, 10],
    "jogurt":   [10, 5],
    "chleb":    [20, 5],
    "jablko":   [10, 10],
    "pomeranc": [15, 10]
}

nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomeranc  |    15,-  |
+-----------+----------+
"""

# kosik = dict()
kosik = {}

oddelovac = "=" * 40


# TODO Pozdrav a nabídka
print(
    "Vitejte v nasem online nakupnim centru", 
    oddelovac,
    nabidka,
    "Zvol si zbozi, pro zaplaceni stiskni 'q'.", 
    sep="\n")

# TODO celý cyklus
while (zbozi := input("Zadej nazev zbozi:")) != "q":
    # TODO pokud zboží nebude v nabídce

    # TODO pokud vybrané zboží není v nákupním košíku

    # TODO pokud zboží je v košíku

    # TODO pokud zboží již není skladem

# TODO výpis košíku