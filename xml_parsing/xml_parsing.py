import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
print(f'root tag  = {root.tag}')
# root through elements in root
print('root has the following children:')
for child in root:
    print(child.tag, child.attrib)

# root through elements in root
print()
print('My books:')
for book in root:
    print(f'Title: {book.attrib["title"]}')
    print(f'Author: {book[0].text}')
    print(f'Year: {book[1].text}')

# recursivly find elements through all nests
print()
for author in root.iter('author'):
    print(author.text)

# find element of direct childern only
print()
for book in root.findall('book'):
    print(book.get('title'))

# find only first match
print()
print(root.find('book').get('title'))

print()
class TempConverter:
    def convert_celcius_to_fahrenheit(temp):
        return round(9/5*temp+32, 2)

class ForecatXmlParser:
    def parse(xml_file):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for child in root:
            print(f'{child[0].text}: {child[1].text} Celsius, {TempConverter.convert_celcius_to_fahrenheit(int(child[1].text))} Fahrenheit')

ForecatXmlParser.parse('forecast.xml')

print()
tree = ET.parse('books.xml')
root = tree.getroot()
for child in root:
    child.tag = 'movie'
    child.remove(child.find('author'))
    child.remove(child.find('year'))
    child.set('rate', '5')
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)
tree.write('movies.xml', 'UTF-8', True)

print()
root = ET.Element('data')
movie_1 = ET.SubElement(root, 'movie', {'title':'The Little Prince', 'rate':'5'})
movie_1_1 = ET.SubElement(movie_1, 'myTitle')
movie_1_1.text = 'Prince'
movie_2 = ET.SubElement(root, 'movie', {'title':'Hamlet', 'rate':'5'})
# ET.dump(root)
tree  = ET.ElementTree(root)
tree.write('test.xml', 'UTF-8', True)
