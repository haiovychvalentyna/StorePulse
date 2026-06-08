import csv
import random
from datetime import datetime, timedelta

def generate_storepulse_data():
    print("Старт генерації даних...")

    
    start_date = datetime(2024, 1, 1)

    cities = ["Київ", "Львів", "Одеса", "Харків", "Вінниця", "Ужгород", "Івано-Франківськ", "Дніпро", "Полтава", "Запоріжжя"]
    first_names = ["Іван", "Марія", "Олександр", "Олена", "Дмитро", "Анна", "Сергій", "Тетяна", "Андрій", "Ольга", "Микола", "Наталія"]
    last_names = ["Петренко", "Коваль", "Шевченко", "Бондаренко", "Ткаченко", "Кravchenko", "Олійник", "Поліщук", "Лисенко", "Мороз"]
    
    customers = []
   
    for c_id in range(1, 121):
        full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        city = random.choice(cities)
        
        reg_date = start_date + timedelta(days=random.randint(0, 365))
        
        customers.append({
            "full_name": full_name,
            "city": city,
            "registration_date": reg_date.strftime("%Y-%m-%d")
        })

    #  КАТАЛОГ ТОВАРІВ (Products)
    product_templates = [
        # --- ЕЛЕКТРОНІКА ---
        ("Смартфон Apple iPhone 15 Pro", "Електроніка", 49999.00),
        ("Смартфон Samsung Galaxy S24 Ultra", "Електроніка", 45999.00),
        ("Смартфон Xiaomi Redmi Note 13", "Електроніка", 9500.00),
        ("Ноутбук Asus ZenBook 14", "Електроніка", 39999.00),
        ("Ноутбук Apple MacBook Air M3", "Електроніка", 54999.00),
        ("Ноутбук Lenovo IdeaPad Gaming", "Електроніка", 29999.00),
        ("Планшет Apple iPad Air", "Електроніка", 26500.00),
        ("Smart-годинник Apple Watch 9", "Електроніка", 18500.00),
        ("Smart-годинник Xiaomi Smart Band 8", "Електроніка", 1690.00),
        ("Навушники AirPods Pro 2", "Електроніка", 9999.00),
        ("Навушники Sony WH-1000XM5", "Електроніка", 14500.00),
        ("Ігрова консоль Sony PlayStation 5", "Електроніка", 22499.00),
        
        # --- ПОБУТОВА ТЕХНІКА ---
        ("Кавомашина DeLonghi Magnifica", "Побутова техніка", 17999.00),
        ("Електрочайник Bosch", "Побутова техніка", 1850.00),
        ("Блендер Tefal", "Побутова техніка", 2300.00),
        ("Робот-пилосос RoboRock", "Побутова техніка", 13999.00),
        ("Мікрохвильова піч Samsung", "Побутова техніка", 4200.00),
        ("Мультиварка Philips", "Побутова техніка", 3999.00),
        ("Тостер Braun", "Побутова техніка", 1450.00),
        
        # --- ОДЯГ ТА ВЗУТТЯ ---
        ("Зимова куртка Columbia", "Одяг", 6500.00),
        ("Джинси Levi's 501", "Одяг", 2900.00),
        ("Кросівки Nike Air Max", "Одяг", 4200.00),
        ("Кросівки Adidas Originals", "Одяг", 3800.00),
        ("Футболка Puma Classic", "Одяг", 850.00),
        ("Спортивний костюм Under Armour", "Одяг", 3200.00),
        ("Худі Reebok", "Одяг", 1950.00),
        
        # --- КНИГИ ---
        ("Художня книга 'Дюна'", "Книги", 450.00),
        ("Підручник 'Чистий Код' (Роберт Мартін)", "Книги", 680.00),
        ("Підручник з SQL для аналітиків", "Книги", 550.00),
        ("Книга 'Атомні звички'", "Книги", 390.00),
        ("Історія України (Ярослав Грицак)", "Книги", 480.00),
        ("Біографія Стіва Джобса", "Книги", 520.00)
    ]
    
    products = []
    for p_id, template in enumerate(product_templates, start=1):
        products.append({
            "product_id": p_id,
            "product_name": template[0],
            "category": template[1],
            "price": template[2]
        })

    orders = []
    order_items = []
    
    order_id_counter = 1
    
    for _ in range(400):
     
        customer_index = random.randint(0, len(customers) - 1)
        customer_id = customer_index + 1
        cust_reg_date = datetime.strptime(customers[customer_index]["registration_date"], "%Y-%m-%d")

        days_after_reg = random.randint(0, 120)
        o_date = cust_reg_date + timedelta(days=days_after_reg)
        
        num_items = random.randint(1, 4)
        chosen_products = random.sample(products, num_items)
        
        total_amount = 0.0
        
        for prod in chosen_products:
            qty = random.randint(1, 2)  
            price_per_item = prod["price"]
            subtotal = qty * price_per_item
            total_amount += subtotal
            
            order_items.append({
                "order_id": order_id_counter,
                "product_id": prod["product_id"],
                "quantity": qty,
                "item_price": price_per_item
            })
            
        orders.append({
            "customer_id": customer_id,
            "order_date": o_date.strftime("%Y-%m-%d"),
            "total_amount": round(total_amount, 2)
        })
        
        order_id_counter += 1

    with open("customers.csv", mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["full_name", "city", "registration_date"])
        for c in customers:
            writer.writerow([c["full_name"], c["city"], c["registration_date"]])
            
    with open("products.csv", mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["product_name", "category", "price"])
        for p in products:
            writer.writerow([p["product_name"], p["category"], p["price"]])

    with open("orders.csv", mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["customer_id", "order_date", "total_amount"])
        for o in orders:
            writer.writerow([o["customer_id"], o["order_date"], o["total_amount"]])


    with open("order_items.csv", mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["order_id", "product_id", "quantity", "item_price"])
        for oi in order_items:
            writer.writerow([oi["order_id"], oi["product_id"], oi["quantity"], oi["item_price"]])

    print("Успіх!")

if __name__ == "__main__":
    generate_storepulse_data()