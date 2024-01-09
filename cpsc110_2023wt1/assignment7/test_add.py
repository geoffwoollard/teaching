from add import list_addition

def test_list_addition():
    assert list_addition([1,2,3], [4,5,6]) == [5,7,9]
    assert list_addition([-1,1,-1], [1,-1,1]) == [0,0,0]
    assert list_addition([1,2.5,3], [4,5,6]) == [5,7.5,9]

def main():
    test_list_addition()
    print('All tests passed')
    
if __name__ == '__main__':
    test_list_addition()
    print('All tests passed')