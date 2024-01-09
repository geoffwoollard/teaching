from intersection import intersection

def test_intersection():
    assert intersection([1,2,3,4,5,6,7,8,9], [2,4,6,8,10,12,14,16,18]) == [2,4,6,8]
    assert intersection([1,2,3,4,5,6,7,8,9], [10,12,14,16,18]) == []
    assert intersection([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9]) == [1,2,3,4,5,6,7,8,9]
    assert intersection([1,2,3,4,5,6,7,8,9], []) == []
    assert intersection([], [1,2,3,4,5,6,7,8,9]) == []
    assert intersection([], []) == []
    assert intersection(['a','b','c'], ['a','b','c']) == ['a','b','c']
    assert intersection(['a','b','c'], ['a','b','c','d']) == ['a','b','c']
    assert intersection(['a','b','c'], ['d','e','f']) == []
    assert intersection(['a','b','c'], []) == []
    assert intersection([], ['a','b','c']) == []


def main():
    test_intersection()
    print('All tests passed')

if __name__ == '__main__':
    main()