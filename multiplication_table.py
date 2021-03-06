def multiplication_table():
    ''' (NoneType) -> NoneType

    Returns a multiplication table of digits in range 1-9, inclusive.
    The first row and column are axes of the digits being multiplied.
    
    >>>multiplication_table()
    0   1   2   3   4   5   6   7   8   9

    1   1   2   3   4   5   6   7   8   9

    2   2   4   6   8   10  12  14  16  18

    3   3   6   9   12  15  18  21  24  27

    4   4   8   12  16  20  24  28  32  36

    5   5   10  15  20  25  30  35  40  45

    6   6   12  18  24  30  36  42  48  24

    7   7   14  21  28  35  42  49  56  63

    8   8   16  24  32  40  48  56  64  72

    9   9   18  27  36  45  54  63  72  81
    '''

    for i in range(0, 10):
        print(i, end = '\t')
        multiplier = 0
        for d in range(1, 10):
            multiplier += 1
            if i == 0:
                print(i + multiplier, end = '\t')
                if d == 9:
                    print('\n\n')
            else:
                print(i * multiplier, end = '\t')
                if d == 9:
                    print('\n\n')

# Test call function
multiplication_table()
