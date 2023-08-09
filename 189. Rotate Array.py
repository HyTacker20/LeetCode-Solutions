books = ["01001001", "01001002", "01002001", "01002002", "01002003", "02001001", "02001002", "02001003"]


def filterBible(scripture, book, chapter):
    result = []
    for b in scripture:
        if b[:2] != book and b[2:5] != chapter:
            scripture.remove(b)
    return scripture


print(filterBible(books, '01', '001'))