import mysql.connector
import csv
import os

def import_csv_to_mysql():
    # Автоматично визначаємо папку, де лежить цей скрипт
    current_folder = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_folder)
    print(f"Робоча папка змінена на: {current_folder}")
    
    # Підключаємося до твого локального phpMyAdmin (XAMPP)
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="storepulse"
        )
        cursor = conn.cursor()
    except mysql.connector.Error as err:
        print(f"Помилка підключення до MySQL: {err}")
        print("Перевірте, чи запущені Apache та MySQL у XAMPP Control Panel!")
        return

    # Список таблиць у строгому порядку через FOREIGN KEY
    tables = ["customers", "products", "orders", "order_items"]
    
    print("\n--- Старт імпорту даних в MySQL (phpMyAdmin) ---")
    
    # Тимчасово вимикаємо перевірку ключів та очищаємо таблиці перед імпортом
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    for table in tables:
        cursor.execute(f"TRUNCATE TABLE {table}")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
    
    for table in tables:
        csv_name = f"{table}.csv"
        
        if not os.path.exists(csv_name):
            print(f"Помилка: Файл {csv_name} не знайдено в папці!")
            continue
            
        with open(csv_name, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)  # пропускаємо перший рядок із заголовками
            
            rows = [row for row in reader]
            
            # Формуємо SQL-запит на вставку
            placeholders = ", ".join(["%s"] * len(headers))
            columns = ", ".join(headers)
            insert_query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            
            cursor.executemany(insert_query, rows)
            print(f"Таблиця [{table}] успішно заповнена! Додано рядків: {len(rows)}")
            
    conn.commit()
    cursor.close()
    conn.close()
    print("\n--- Імпорт завершено! База в phpMyAdmin успішно наповнена! ---")

if __name__ == "__main__":
    import_csv_to_mysql()
