from rewrite import function

def function_while(alist):
  j = len(alist)-1
  while j > 0:
    i=0
    while i < j:
        if alist[i]>alist[i+1]:
          temp = alist[i]
          alist[i] = alist[i+1]
          alist[i+1] = temp
        i=i+1
    j=j-1

def test_function():
    alist = [54,26,93,17,77,31,44,55,20]
    blist = alist.copy()
    function_while(alist)
    assert alist != blist
    function(blist)
    assert alist == blist

def main():
    test_function()
    print('all tests passed for rewrite.py')

if __name__ == '__main__':
    main()
