import csv
import random
from datetime import datetime, timedelta

# =====================================================================
# 1. НАЛАШТУВАННЯ ТА ШАБЛОНИ ДАНИХ (Константи)
# =====================================================================
NUM_CUSTOMERS = 100  # Скільки покупців створити
NUM_ORDERS = 300     # Скільки замовлень (чеків) зробити

cities = ["Київ", "Львів", "Одеса", "Харків", "Ужгород", "Івано-Франківськ", "Вінниця"]
first_names = ["Іван", "Марія", "Олександр", "Олена", "Дмитро", "Тетяна", "Андрій", "Наталія", "Сергій", "Юлія"]
last_names = ["Петренко", "Коваль", "Шевченко", "Коваленко", "Бойко", "Ткаченко", "Кравченко", "Олійник"]

# Великий каталог товарів: (Назва, Категорія, Ціна в грн)
product_templates = [
    # Електроніка
    ("Смартфон Apple iPhone", "Електроніка", 45000),
    ("Смартфон Samsung Galaxy", "Електроніка", 32000),
    ("Ноутбук Asus ZenBook", "Електроніка", 38000),
    ("Bezdropotovi navushnyky", "Електроніка", 2500),
    ("Smart-godynnyk", "Електроніка", 6000),
    ("Powerbank 20000mAh", "Електроніка", 1200),
    # Одяг
    ("Dzhynsy klasychni", "Одяг", 1800),
    ("Futbolka bavovnyana", "Одяг", 550),
    ("Khudi z kapushonom", "Одяг", 1400),
    ("Sportyvni krosivky", "Одяг", 3200),
    ("Zymova kurtka", "Одяг", 4800),
    # Книги
    ("Roman 'Dyvo'", "Книги", 350),
    ("Pidruchunyk z SQL", "Книги", 650),
    ("Istoriya Ukrainy", "Книги", 450),
    ("Knyga 'Atomni zvychky'", "Книги", 380),
    # Дім та побут
    ("Chashka keramichna", "Дім та побут", 250),
    ("Lampa nastilna", "Дім та побут", 850),
    ("Postilna bilyzna", "Дім та побут", 1900),
    ("Termokukhlyochok", "Дім та побут", 600),
    # Спорт і відпочинок
    ("Kylymok dlya yogy", "Спорт і відпочинок", 750),
    ("Ganteli nabornyki", "Спорт і відпочинок", 1500),
    ("Plyashka dlya vody", "Спорт і відпочинок", 300),
    ("Ryukzak turystychnyi", "Спорт і відпочинок", 2200)
]

def generate_random_date(start_year, end_year):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# =====================================================================
# 2. ГЕНЕРАЦІЯ ДАНИХ
# =====================================================================
print("Start generatsii danykh...")

# --- Створення клієнтів (Customers) ---
customers_table = []
customer_reg_dates = {}

for c_id in range(1, NUM_CUSTOMERS + 1):
    full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
    city = random.choice(cities)
    reg_date_dt = generate_random_date(2024, 2025)
    reg_date_str = reg_date_dt.strftime("%Y-%m-%d")
    
    customers_table.append([c_id, full_name, city, reg_date_str])
    customer_reg_dates[c_id] = reg_date_dt

# --- Створення каталогу продуктів (Products) ---
products_table = []
for p_id, (name, category, price) in enumerate(product_templates, start=1):
    products_table.append([p_id, name, category, price])

# --- Створення замовлень (Orders) та чеків (Order Items) ---
orders_table = []
order_items_table = []
item_id_counter = 1

for o_id in range(1, NUM_ORDERS + 1):
    customer_id = random.randint(1, NUM_CUSTOMERS)
    reg_date = customer_reg_dates[customer_id]
    days_after_reg = random.randint(1, 150)
    order_date_dt = reg_date + timedelta(days=days_after_reg)
    order_date_str = order_date_dt.strftime("%Y-%m-%d")
    
    orders_table.append([o_id, customer_id, order_date_str])
    
    items_count = random.randint(1, 3)
    chosen_products = random.sample(products_table, items_count)
    
    for prod in chosen_products:
        p_id = prod[0]
        price = prod[3]
        quantity = random.randint(1, 2)
        
        order_items_table.append([item_id_counter, o_id, p_id, quantity, price])
        item_id_counter += 1

# =====================================================================
# 3. ЗБЕРЕЖЕННЯ У CSV-ФАЙЛИ
# =====================================================================
def save_to_csv(filename, headers, rows):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"File '{filename}' uspishno stvoreno! Ryadkiv: {len(rows)}")

save_to_csv("customers.csv", ["customer_id", "full_name", "city", "registration_date"], customers_table)
save_to_csv("products.csv", ["product_id", "product_name", "category", "price"], products_table)
save_to_csv("orders.csv", ["order_id", "customer_id", "order_date"], orders_table)
save_to_csv("order_items.csv", ["order_item_id", "order_id", "product_id", "quantity", "price"], order_items_table)

print("\nUra! Generatsiyu zaversheno!")
