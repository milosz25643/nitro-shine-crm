import sqlite3


connection = sqlite3.connect('nitro_shine.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    car_model TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    price REAL
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    service_id INTEGER,
    order_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients (id),
    FOREIGN KEY (service_id) REFERENCES services (id)
)
''')

print("✅ Baza danych 'nitro_shine.db' oraz tabele zostały pomyślnie stworzone!")

connection.commit()
connection.close()