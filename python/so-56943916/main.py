import xml.etree.ElementTree as ET

def display_book(book):

    root = ET.parse(source="library.xml")

    info = root.iter("catalog")
    
    for elem in info:
        books = elem.findall("book")
        for book in books:
            print book.attrib['id']
            

    return "Book Not Found"

#Main
display_book("bk105")
