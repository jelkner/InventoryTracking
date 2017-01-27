import random
from footwear import Boot, DressShoe, CasualShoe


def make_catalog(n):
    styles = [["Cowboy", "Hiking", "Rain", "Riding"],
              ["Loafer", "Oxford", "Pump", "Sling-back", "Wing-tip"],
              ["Athletic", "Hightop", "Moccasin", "Sandal"]]

    sizes = []
    for s in range(5, 14):
        sizes += [s, s + 0.5]
    sizes.append(14)

    catalog = []

    for i in range(n):
        fwtype = random.randint(0, len(styles)-1)
        style = random.choice(styles[fwtype])
        size = random.choice(sizes)
        sku = "1234-" + str(i)

        if fwtype == 0:
            catalog.append(Boot(style, size, sku))
        elif fwtype == 1:
            catalog.append(DressShoe(style, size, sku))
        else:
            catalog.append(CasualShoe(style, size, sku))

    return catalog


if __name__ == '__main__':
    catalog = make_catalog(20)
    for shoe in catalog:
        print(shoe)
