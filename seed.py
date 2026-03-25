import sqlite3

connection = sqlite3.connect('nitro_shine.db')
cursor = connection.cursor()


services_to_add = [
    ('Ceramika 3-letnia', 2500.00),
    ('Korekta lakieru 1-etapowa', 1200.00),
    ('Kompleksowe mycie detailingowe', 350.00),
    ('Pranie tapicerki', 450.00)
]

cursor.executemany('INSERT INTO services (service_name, price) VALUES (?, ?)', services_to_add)


cursor.execute("INSERT INTO clients (name, phone, car_model) VALUES (?, ?, ?)", 
               ('Miłosz', '500-600-700', 'Audi A3 8V'))

connection.commit()
print("✅ Usługi i pierwszy klient dodani do bazy!")
connection.close()