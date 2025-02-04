"""
Створи XML-файл, що містить інформацію про продукти магазину:
Назва продукту
Ціна
Кількість на складі
--------------------
<products>
    <product>
        <name>Молоко</name>
        <price>25</price>
        <quantity>50</quantity>
    </product>
    <product>
        <name>Хліб</name>
        <price>10</price>
        <quantity>100</quantity>
    </product>
</products>
--------------------
2.Напиши програму, яка:
Читає XML-файл і виводить назви продуктів та їхню кількість.
Змінює кількість товару та зберігає зміни в XML-файл.
"""
import xml.etree.ElementTree as ET

def read_products_xml() -> "list":
    """
    read product info from products.xml
    :return:
    """
    products = []
    tree = ET.parse('products.xml')
    root = tree.getroot()
    for user in root.findall('product'):
        name = user.find('name').text
        price = user.find('price').text
        quantity = user.find('quantity').text
        products.append(f'{name} is cost {price}, {quantity} available')
    return products

def change_product(product_name, new_count) -> "str":
    """
    Change product count and return result in string
    :return:
    """
    tree = ET.parse('products.xml')
    root = tree.getroot()
    product_is_here = False
    count = 0
    for user in root.findall('product'):
        if user.find('name').text == product_name:
            user.find('quantity').text = str(new_count)
            product_is_here = True
            count += 1
    if product_is_here:
        tree.write('products.xml', encoding="utf-8")
        msg = f"Product {product_name} count changed in {count} places!"
    else:
        msg = f"Product name {product_name} is not available!"
    return msg

def add_product(name, price, quantity) -> "str":
    """
    adding new product with inner parameters
    :param name:
    :param price:
    :param quantity:
    :return:
    """
    msg = ""
    try:
        tree = ET.parse('products.xml')
        root = tree.getroot()

        products = ET.Element("products")
        product = ET.SubElement(products,"product")
        ET.SubElement(product, 'name').text = name
        ET.SubElement(product, 'price').text = str(price)
        ET.SubElement(product, 'quantity').text = str(quantity)
        root.insert(0, product)

        tree = ET.ElementTree(root)
        tree.write("products.xml", encoding="utf-8")
        msg = "Product added!"
    except:
        msg = "Product not added!"
    return msg

for prod in read_products_xml():
    print(prod)
print(change_product("Milk", 30))
# print(add_product("Coffe", 47, 57))
