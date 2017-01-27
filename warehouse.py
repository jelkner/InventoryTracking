class BinItem:
    """
      >>> item = BinItem('12345-27', 2136)
      >>> item.sku
      '12345-27'
      >>> item.quantity
      2136
      >>> print(item)
      SKU 12345-27: 2136
    """
    def __init__(self, sku, quantity):
        self.sku = sku
        self.quantity = quantity

    def __str__(self):
        return "SKU {0}: {1}".format(self.sku, self.quantity)


class Bin:
    """
      >>> a_bin = Bin('A')
      >>> a_bin.name
      'A'
      >>> a_bin.contents
      []
      >>> print(a_bin)
      Bin A:
      >>> a_bin.add(BinItem('12345-45', 500))
      >>> print(a_bin)
      Bin A:
        SKU 12345-45: 500
      >>> a_bin.add(BinItem('12345-27', 4320))
      >>> print(a_bin)
      Bin A:
        SKU 12345-27: 4320
        SKU 12345-45: 500
    """
    def __init__(self, name):
        self.name = name
        self.contents = []

    def __str__(self):
        s = "Bin {0}:".format(self.name)
        for item in self.contents:
            s += '\n  ' + item.__str__()
        return s

    def add(self, item):
        self.contents.append(item)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
