import xml.etree.ElementTree as ET

def display_book(book):

    root = ET.parse(source="library.xml")

    info = root.iter("catalog")
    
    print info

    for elem in info:
        print elem
        name = elem.find("book").attrib['id']
        print name

        if name == book:
            print(name)

    return "Book Not Found"

#Main
display_book("bk105")
