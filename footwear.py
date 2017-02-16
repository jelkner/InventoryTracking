class Footwear:
    """
      >>> f = Footwear('Sling-back', 8.5, '1234-0')
      >>> f.style
      'Sling-back'
      >>> f.size
      8.5
      >>> f.sku
      '1234-0'
      >>> f.type
      'Unspecified'
      >>> f.print_size()
      'size 8½'
      >>> f2 = Footwear('Hightop', 10, '1234-19')
      >>> f2.print_size()
      'size 10'
      >>> print(f)
      Sling-back (size 8½)
      >>> print(f2)
      Hightop (size 10)
      >>> f3 = Footwear('Hightop', 10, '1234-19')
      >>> f4 = Footwear('Lowtop', 12, '1234-19')
      >>> f2 == f3
      True
      >>> f2 == f4
      False
    """
    def __init__(self, style, size, sku, shoetype='Unspecified'):
        self.style = style
        self.size = size
        self.sku = sku
        self.type = shoetype

    def print_size(self):
        if int(self.size) == self.size:
            return 'size {0}'.format(int(self.size))
        return 'size {0}½'.format(int(self.size))

    def __str__(self):
        return '{0} ({1})'.format(self.style, self.print_size())

    def __eq__(self, other):
        return self.type == other.type and self.style == other.style and \
               self.size == other.size and self.sku == other.sku


class Boot(Footwear):
    """
      >>> b = Boot('Hiking', 11.5, '1234-10')
      >>> print(b)
      Boot - Hiking (size 11½)
    """
    def __init__(self, style, size, sku, shoetype='Boot'):
        Footwear.__init__(self, style, size, sku, shoetype)

    def __str__(self):
        return '{0} - {1}'.format(self.type, Footwear.__str__(self))


class Shoe(Footwear):
    """
      >>> s = Shoe('Generic', 9.5, '1234-23')
      >>> print(s)
      Shoe - Generic (size 9½)
    """
    def __init__(self, style, size, sku, shoetype='Shoe'):
        Footwear.__init__(self, style, size, sku, shoetype)

    def __str__(self):
        return '{0} - {1}'.format(self.type, Footwear.__str__(self))


class DressShoe(Shoe):
    """
      >>> ds = DressShoe('Sling-back', 8.5, '1234-43')
      >>> print(ds)
      Dress Shoe - Sling-back (size 8½)
    """
    def __init__(self, style, size, sku, shoetype='Dress Shoe'):
        Shoe.__init__(self, style, size, sku, shoetype)


class CasualShoe(Shoe):
    """
      >>> cs = CasualShoe('Moccasin', 12.5, '1234-62')
      >>> print(cs)
      Casual Shoe - Moccasin (size 12½)
    """
    def __init__(self, style, size, sku, shoetype='Casual Shoe'):
        Shoe.__init__(self, style, size, sku, shoetype)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
