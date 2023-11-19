from library import Library

def test_library():
    library1 = Library('Woodward')
    library2 = Library('Barber')
    assert library1.get_name() == 'Woodward'

    library1.stock_book('The Great Gatsby')
    library1.stock_book('The Catcher in the Rye')
    library1.stock_book('To Kill a Mockingbird')
    assert len(library1.books) == 3

    library2.stock_book('The Lord of the Rings')
    library2.stock_book('1984')
    library2.stock_book('Brave New World')

    library1.borrow_book('The Great Gatsby')
    assert len(library1.books) == 2
    library1.return_book('The Great Gatsby')
    assert len(library1.books) == 3
    library1.return_book('NOT A BOOK')
    assert len(library1.books) == 3

    library2.borrow_book('The Lord of the Rings')

    assert type(library1.__str__()) == str

    library3 = library1 + library2
    assert library3 > library2
    assert library2 < library3

    print(library3)

    library3.set_name('Wood-IKB')

if __name__ == '__main__':
    test_library()
    print('Passed!')