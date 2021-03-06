# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment 1: getallen

(c) 2019 Hogeschool Utrecht,
Bart van Eijkelenburg en
Tijmen Muller (tijmen.muller@hu.nl)


Opdracht:
Werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

naam = "Joselyne de Zeeuw"
klas = "TICT-ICT-V1B"
studentnummer = 1809264


def is_even(n):
    # Divide by 2, if the remainder is 0, num is even. If there's a remainder, num is uneven
    if n % 2 == 0:
        return True
    else:
        return False


def floor(real):
    floor = int(real // 1)
    return floor


def ceil(real):
    ceil = int(-1 * real // 1 * -1)
    return ceil


def div(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    return sorted(divisors)


def is_prime(n):
    divisors = div(n)
    if len(divisors) > 2 or len(divisors) == 1:
        return False
    else:
        return True


def primes(num):
    primelist = []
    for number in range(1, num+1):
        if number < num:
            if is_prime(number):
                primelist.append(number)

    return sorted(primelist)


def primefactors(n):
    num = 2
    factors = []
    while num * num <= n:
        if n % num:
            num += 1
        else:
            n //= num
            factors.append(num)
    if n > 1:
        factors.append(n)
    return sorted(factors)


def gcd(a, b):
    numsa = []
    numsb = []
    for num in div(a):
        numsa.append(num)
    for num in div(b):
        numsb.append(num)
    numsa = numsa[::-1]
    numsb = numsb[::-1]
    for numa in numsa:
        for numb in numsb:
            if numa == numb:
                return numa


def lcm(a, b):
    lcm = (a*b)//gcd(a, b)
    return lcm


def add_frac(n1, d1, n2, d2):
    div = lcm(d1, d2)
    n3 = n1 * (div / d1)
    n4 = n2 * (div / d2)
    num = n3 + n4
    while True:
        if is_even(num) and is_even(div):
            num = num / 2
            div = div / 2
        else:
            break

    return int(num), div


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_is_even():
    testcases = [
        ((1,), False),
        ((2,), True),
        ((3,), False),
        ((4,), True)
    ]

    for case in testcases:
        __my_assert_args(is_even, case[0], case[1])


def test_floor():
    testcases = [
        ((1.05,), 1),
        ((1.95,), 1),
        ((-1.05,), -2),
        ((-1.95,), -2),
        ((0.05,), 0),
        ((-0.05,), -1),
        ((0.0,), 0),
        ((1.0,), 1),
        ((-1.0,), -1)
    ]

    for case in testcases:
        __my_assert_args(floor, case[0], case[1])


def test_floor_simulated():
    import random
    import math

    for _ in range(10):
        x = random.uniform(-10.0, 10.0)
        __my_assert_args(floor, (x,), math.floor(x))


def test_ceil():
    testcases = [
        ((1.05,), 2),
        ((1.95,), 2),
        ((-1.05,), -1),
        ((-1.95,), -1),
        ((0.05,), 1),
        ((-0.05,), 0),
        ((0.0,), 0),
        ((1.0,), 1),
        ((-1.0,), -1)
    ]

    for case in testcases:
        __my_assert_args(ceil, case[0], case[1])


def test_ceil_simulated():
    import random
    import math

    for _ in range(10):
        x = random.uniform(-10.0, 10.0)
        __my_assert_args(ceil, (x,), math.ceil(x))


def test_div():
    testcases = [
        ((1,), [1]),
        ((2,), [1, 2]),
        ((3,), [1, 3]),
        ((4,), [1, 2, 4]),
        ((8,), [1, 2, 4, 8]),
        ((12,), [1, 2, 3, 4, 6, 12]),
        ((19,), [1, 19]),
        ((25,), [1, 5, 25]),
        ((929,), [1, 929]),
        ((936,), [1, 2, 3, 4, 6, 8, 9, 12, 13, 18, 24, 26, 36, 39, 52, 72, 78, 104, 117, 156, 234, 312, 468, 936])
    ]

    for case in testcases:
        __my_assert_args(div, case[0], sorted(case[1]))


def test_is_prime():
    testcases = [
        ((1,), False),
        ((2,), True),
        ((3,), True),
        ((4,), False),
        ((5,), True),
        ((6,), False),
        ((9,), False),
        ((29,), True)
    ]

    for case in testcases:
        __my_assert_args(is_prime, case[0], case[1])


def test_primefactors():
    testcases = [
        ((-1,), []),
        ((1,), []),
        ((2,), [2]),
        ((3,), [3]),
        ((4,), [2, 2]),
        ((8,), [2, 2, 2]),
        ((12,), [2, 2, 3]),
        ((2352,), [2, 2, 2, 2, 3, 7, 7]),
        ((9075,), [3, 5, 5, 11, 11])
    ]

    for case in testcases:
        __my_assert_args(primefactors, case[0], sorted(case[1]))


def test_primes():
    testcases = [
        ((1,), []),
        ((2,), []),
        ((3,), [2]),
        ((4,), [2, 3]),
        ((5,), [2, 3]),
        ((6,), [2, 3, 5]),
        ((30,), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    ]

    for case in testcases:
        __my_assert_args(primes, case[0], sorted(case[1]))


def test_gcd():
    testcases = [
        ((60, 1), 1),
        ((60, 6), 6),
        ((60, 7), 1),
        ((60, 8), 4),
        ((60, 9), 3),
        ((60, 11), 1),
        ((60, 13), 1),
        ((60, 14), 2),
        ((60, 15), 15),
        ((60, 16), 4),
        ((60, 18), 6)
    ]

    for case in testcases:
        __my_assert_args(gcd, case[0], case[1])


def test_gcd_simulated():
    import random
    import math

    for _ in range(10):
        a = random.randrange(3, 201, 3)
        b = random.randrange(4, 201, 4)
        __my_assert_args(gcd, (a, b), math.gcd(a, b))


def test_lcm():
    testcases = [
        ((60, 1), 60),
        ((60, 2), 60),
        ((60, 7), 420),
        ((60, 8), 120),
        ((60, 9), 180),
        ((60, 10), 60),
        ((60, 11), 660),
        ((60, 18), 180)
    ]

    for case in testcases:
        __my_assert_args(lcm, case[0], case[1])


def test_add_frac():
    testcases = [
        ((1, 3, 1, 5), (8, 15)),
        ((1, 2, 1, 4), (3, 4)),
        ((2, 3, 3, 2), (13, 6)),
        ((1, 2, 1, 6), (2, 3)),
        ((3, 4, 1, 6), (11, 12)),
        ((1, 6, 3, 4), (11, 12)),
        ((1, 2, 1, 3), (5, 6)),
        ((1, 2, 2, 3), (7, 6))
    ]

    for case in testcases:
        __my_assert_args(add_frac, case[0], case[1])


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")  # Groene tekstkleur
        test_id()

        test_is_even()
        print("Je functie is_even(n) werkt goed!")

        test_floor()
        test_floor_simulated()
        print("Je functie floor(real) werkt goed!")

        test_ceil()
        test_ceil_simulated()
        print("Je functie ceil(real) werkt goed!")

        test_div()
        print("Je functie div(n) werkt goed!")

        test_is_prime()
        print("Je functie is_prime(n) werkt goed!")

        test_primefactors()
        print("Je functie primefactors(n) werkt goed!")

        test_primes()
        print("Je functie primes(num) werkt goed!")

        test_gcd()
        test_gcd_simulated()
        print("Je functie gcd(a, b) werkt goed!")

        test_lcm()
        print("Je functie lcm(a, b) werkt goed!")

        test_add_frac()
        print("Je functie add_frac(n1, d1, n2, d2) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")


    except AssertionError as ae:
        print("\x1b[31m")  # Rode tekstkleur
        print(ae)

    print("\x1b[0m")  # Reset tekstkleur


if __name__ == '__main__':
    __main()
