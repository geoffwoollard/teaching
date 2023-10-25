from max import max_index


def test_max_index():
    assert max_index([1,2,3,10,5,10]) == 3
    assert max_index([1,1,1]) == 0
    assert max_index([1.1,1.1,1.1]) == 0

def main():
    test_max_index()
    print('all tests passed for max.py')

if __name__ == '__main__':
    main()
