from easy import stats_range, stats_mean, stats_median, stats_mode

numbers = [1,2,2,2,3,4,5,5,6,7,8,9,9,9,10,11]

def test_stats_range():
    assert stats_range(numbers) == 10

def test_stats_mean():
    assert stats_mean(numbers) == 5.8125

def test_stats_median():
    assert stats_median(numbers) == 5.5

def test_stats_mode():
    assert stats_mode(numbers) == 2

def main():
    test_stats_range()
    test_stats_mean()
    test_stats_median()
    test_stats_mode()
    print('All tests passed for easy.py!')

if __name__ == '__main__':
    main()