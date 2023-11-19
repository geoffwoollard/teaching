from nilakantha import nilakanthaSeries
import time


def nilakanthaSeries_old(terms):
    for counter in range(terms):
        result = 3
        denom = 2
        for n in range(counter):
            result = result + (-1.0)**(n)*4.0/(denom*(denom+1)*(denom+2))
            denom = denom + 2
        pi = result
    return pi

def test_nilakanthaSeries():
    for terms in [10,30,100]:
        assert nilakanthaSeries(terms) == nilakanthaSeries_old(terms)

    terms = 10000
    start = time.time()
    pi = nilakanthaSeries_old(terms)
    end = time.time()
    old_time = end - start
    print('time of nilakanthaSeries_old', old_time)

    start = time.time()
    pi = nilakanthaSeries(terms)
    end = time.time()
    new_time = end - start
    print('time of nilakanthaSeries', new_time)
    assert new_time < old_time/1000


def main():
    test_nilakanthaSeries()
    print('All tests passed!')

if __name__ == '__main__':
    main()
