import sqlite3

connection = sqlite3.connect('nitro_shine.db')
cursor = connection.cursor()

print("--- 📋 LISTA USŁUG NITRO SHINE ---")

cursor.execute("SELECT * FROM services")
services = cursor.fetchall()

for s in services:
    print(f"ID: {s[0]} | Usługa: {s[1]:<30} | Cena: {s[2]} PLN")

print("\n--- 👤 TWOI KLIENCI ---")

cursor.execute("SELECT * FROM clients")
clients = cursor.fetchall()

for c in clients:
    print(f"ID: {c[0]} | Imię: {c[1]:<10} | Auto: {c[3]}")

connection.close()