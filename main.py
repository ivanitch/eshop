from src.category import Category
from src.product import Product

if __name__ == '__main__':
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        "Серый",
        5
    )

    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        "Gray",
        8
    )

    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        "Синий",
        14
    )

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    cat_desc1 = ("Смартфоны, как средство не только коммуникации, но и получения дополнительных "
                 "функций для удобства жизни")
    category1 = Category("Смартфоны", cat_desc1, [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, "black", 7)

    cat_desc2 = "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    category2 = Category("Телевизоры", cat_desc2, [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
