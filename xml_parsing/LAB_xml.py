import xml.etree.ElementTree as ET

class Product:
    products = []
    def __init__(self, category, name, type, producer, price, currency):
        self.category = category
        self.name = name
        self.type = type
        self.producer = producer
        self.price = price
        self.currency = currency
        self.products.append(self)

Product('Vegan', 'sunshine', 'cereal', 'OpenEDG', 9.90, 'USD')
Product('Vegan', 'spahgetti', 'pasta', 'programmers', 15.49, 'eur')
Product('Vegan', 'fantastic', 'beverage', 'drinks4coders', 19.90, 'USD')

root = ET.Element('shop')
category = ET.SubElement(root, 'category', {'name':'Vegan Products'})
for product in Product.products:
    product_name = ET.SubElement(category, 'product', {'name':product.name})
    product_type = ET.SubElement(product_name, 'type')
    product_type.text = product.type
    product_prod = ET.SubElement(product_name, 'producer')
    product_prod.text = product.producer
    product_price = ET.SubElement(product_name, 'price')
    product_price.text = str(product.price)
    product_currency = ET.SubElement(product_name, 'type')
    product_currency.text = product.currency
tree = ET.ElementTree(root)
tree.write('products.xml', 'UTF-8', True)
