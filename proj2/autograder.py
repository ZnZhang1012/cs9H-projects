import doctest

from converter import convert


def test_convert():
    """
    # Distances
    >>> convert("1 m in km")
    1 m = 0.001000 km
    >>> convert("1.23456 m in km")
    1.23456 m = 0.001235 km
    >>> convert("2 cm in mm")
    2 cm = 20.000000 mm
    >>> convert("1.5 cm in in")
    1.5 cm = 0.590551 in
    >>> convert("9 ft in mm")
    9 ft = 2743.200000 mm
    >>> convert("3 ft in in")
    3 ft = 36.000000 in
    >>> convert("1 yd in m")
    1 yd = 0.914400 m
    >>> convert("1 mi in km")
    1 mi = 1.609344 km

    # Volumes
    >>> convert("1 L in mL")
    1 L = 1000.000000 mL
    >>> convert("1.0 L in mL")
    1.0 L = 1000.000000 mL
    >>> convert("0.5 floz in mL")
    0.5 floz = 14.786765 mL
    >>> convert("2 cup in floz")
    2 cup = 16.000000 floz
    >>> convert("1 pint in mL")
    1 pint = 473.176473 mL
    >>> convert("3 qt in pint")
    3 qt = 6.000000 pint
    >>> convert("2.2 gal in L")
    2.2 gal = 8.327906 L

    # Error Handling
    >>> convert("1") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("1 L mL") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("1m in cm") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("1 m in cm in km") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("a m in L") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("1 m in L") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("1 mL in cm") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("1 mL in LL") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("1 LL in mL") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("1 abc in edf") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("1 aaaaaaaaa in L") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    >>> convert("1 m on cm") # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    Error: ...
    """


if __name__ == '__main__':
    test_result = doctest.testmod(exclude_empty=True)
    print("Autograder Result: {}/{} success, {} failed."
          .format((test_result.attempted - test_result.failed), test_result.attempted, test_result.failed))
