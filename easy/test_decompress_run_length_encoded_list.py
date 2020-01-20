def decompressRLElist(nums):
    decompressed = []
    for i, num in enumerate(nums):
        if i % 2 == 0:
            count = num
        else:
            value = num
            for i in range(count):
                decompressed.append(value)
    return decompressed


def test_1():
    assert decompressRLElist([1, 2, 3, 4]) == [2, 4, 4, 4]


def test_2():
    assert decompressRLElist([4, 6, 2, 4]) == [6, 6, 6, 6, 4, 4]


def test_3():
    assert decompressRLElist([55, 11, 70, 26, 62, 64]) == [
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        11,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        26,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
        64,
    ]

