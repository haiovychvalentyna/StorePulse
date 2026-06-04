import sqlite3
import csv
import os

def import_csv_to_sqlite():
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    os.chdir(current_folder)
    print(f"Robocha papka zminena na: {current_folder}")
  
    conn = sqlite3.connect("storepulse.db")
    cursor = conn.cursor()
    

    tables = ["customers", "products", "orders", "order_items"]
    
    print("\n--- Start importu danykh v SQL ---")
    
    for table in tables:
        csv_name = f"{table}.csv"
        
        if not os.path.exists(csv_name):
            print(f"Error: File {csv_name} ne znaydeno в папці!")
            continue
            
    
        with open(csv_name, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)  
            
        
            columns_str = ", ".join([f"{h} TEXT" for h in headers])
            cursor.execute(f"DROP TABLE IF EXISTS {table}")
            cursor.execute(f"CREATE TABLE {table} ({columns_str})")
            
    
            placeholders = ", ".join(["?"] * len(headers))
            rows = [row for row in reader]
            cursor.executemany(f"INSERT INTO {table} VALUES ({placeholders})", rows)
            
        print(f"Tablytsya [{table}] uspishno zavantazhena! Ryadkiv: {len(rows)}")
        
    conn.commit()
    conn.close()
    print("\n--- Import zaversheno! 'storepulse.db' gotovyi! ---")

if __name__ == "__main__":
    import_csv_to_sqlite()
