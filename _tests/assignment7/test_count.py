from count import count_range

def test_count_range():
    assert count_range(0, 10, [1,2,3,4,5,6,7,8,9]) == 9
    assert count_range(0, 10, [1,2,3,4,5,6,7,8,9,10]) == 9
    assert count_range(5, 10, [1,2,3,4,5,6,7,8,9,10,11]) == 5
    assert count_range(1, 11.1, [1,2,3,4,5,6,7,8,9,10,11]) == 11


def main():
    test_count_range()
    print('All tests passed')

if __name__ == '__main__':
    main()