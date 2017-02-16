import random
import json
from footwear import Boot, DressShoe, CasualShoe


def make_catalog(n):
    styles = (("Cowboy", "Hiking", "Rain", "Riding"),
              ("Loafer", "Oxford", "Pump", "Sling-back", "Wing-tip"),
              ("Athletic", "Hightop", "Moccasin", "Sandal"))

    sizes = (5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5,
             12, 12.5, 13, 13.5, 14)

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


def get_catalog(fname):
    """Read catalog from json encoded fname file."""
    f = open(fname, 'r')
    catdat = f.read()
    f.close()
    catalog = json.loads(catdat)
    for index, item in enumerate(catalog):
        style, size, sku = item['style'], item['size'], item['sku']
        if item['type'] == 'Boot':
            catalog[index] = Boot(style, size, sku)
        elif item['type'] == 'DressShoe':
            catalog[index] = DressShoe(style, size, sku)
        else:
            catalog[index] = CasualShoe(style, size, sku)

    return catalog   


def save_catalog(catalog, fname):
    """Write catalog to json encoded fname file."""
    f = open(fname, 'w')
    catalog = [item.__dict__ for item in catalog]
    f.write(json.dumps(catalog))
    f.close()


if __name__ == '__main__':
    import doctest
    doctest.testfile("warehouse_tests.txt")
