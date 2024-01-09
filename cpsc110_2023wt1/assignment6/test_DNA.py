from DNA import check_complementary


def test_check_complementary():
    assert check_complementary("GTGCCACG",'CACGGTGC') == True
    assert check_complementary("GTGCCATG",'AACCGTGC') == False
    assert check_complementary('ATCG','TAGC') == True
    assert check_complementary('ATCG','TAGG') == False, check_complementary('ATCG','TAGG')
    assert check_complementary('ATCG','TAG') == False
    assert check_complementary('ATCG','TAGCC') == False

def main():
    test_check_complementary()
    print('all tests passed for DNA.py')

if __name__ == '__main__':
    main()