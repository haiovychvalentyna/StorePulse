import sqlite3
import csv
import os

def import_csv_to_sqlite():
    # МАГІЧНИЙ РЯДОК: Дізнаємося точну папку, де лежить цей скрипт
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # Змінюємо робочу папку програми на ту, де лежить наш скрипт
    os.chdir(current_folder)
    print(f"Robocha papka zminena na: {current_folder}")
    
    # 1. Підключаємося до SQLite (файл бази даних створиться поруч)
    conn = sqlite3.connect("storepulse.db")
    cursor = conn.cursor()
    
    # Список наших таблиць для імпорту
    tables = ["customers", "products", "orders", "order_items"]
    
    print("\n--- Start importu danykh v SQL ---")
    
    for table in tables:
        csv_name = f"{table}.csv"
        
        if not os.path.exists(csv_name):
            print(f"Error: File {csv_name} ne znaydeno в папці!")
            continue
            
        # Читаємо CSV файл
        with open(csv_name, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)  # Беремо заголовки
            
            # Створюємо таблицю в SQL
            columns_str = ", ".join([f"{h} TEXT" for h in headers])
            cursor.execute(f"DROP TABLE IF EXISTS {table}")
            cursor.execute(f"CREATE TABLE {table} ({columns_str})")
            
            # Заливаємо рядки
            placeholders = ", ".join(["?"] * len(headers))
            rows = [row for row in reader]
            cursor.executemany(f"INSERT INTO {table} VALUES ({placeholders})", rows)
            
        print(f"Tablytsya [{table}] uspishno zavantazhena! Ryadkiv: {len(rows)}")
        
    conn.commit()
    conn.close()
    print("\n--- Import zaversheno! 'storepulse.db' gotovyi! ---")

if __name__ == "__main__":
    import_csv_to_sqlite()
