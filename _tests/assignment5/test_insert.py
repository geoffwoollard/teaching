from insert import insert_v1, insert_v2


def test_insert_v1():
    list_a = [1,2,3,4,5]
    list_b = [6,7,8,9,10]
    index = 3
    assert insert_v1(list_a,list_b,index) == [1, 2, 3, 6, 7, 8, 9, 10, 4, 5]

def test_insert_v2():
    list_a = [1,2,3,4,5]
    list_b = [6,7,8,9,10]
    index = 3
    nothing = insert_v2(list_a,list_b,index)
    assert nothing is None
    assert list_a == [1, 2, 3, 6, 7, 8, 9, 10, 4, 5]

def main():
    # test_insert_v1()
    test_insert_v2()
    print('All tests passed for insert.py!')


if __name__ == '__main__':
    main()