import sqlite3

def show_menu():
    print("\n--- 💎 NITRO SHINE CRM - PANEL ZARZĄDZANIA ---")
    print("1. Pokaż listę usług")
    print("2. Dodaj nowego klienta")
    print("3. Pokaż wszystkich klientów")
    print("0. Wyjście")
    return input("Wybierz opcję: ")

def list_services():
    conn = sqlite3.connect('nitro_shine.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM services")
    services = cursor.fetchall()
    print("\n--- DOSTĘPNE USŁUGI ---")
    for s in services:
        print(f"[{s[0]}] {s[1]} - {s[2]} PLN")
    conn.close()

def add_client():
    name = input("Imię i nazwisko klienta: ")
    phone = input("Numer telefonu: ")
    car = input("Model samochodu: ")
    
    conn = sqlite3.connect('nitro_shine.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clients (name, phone, car_model) VALUES (?, ?, ?)", (name, phone, car))
    conn.commit()
    print(f"✅ Klient {name} dodany pomyślnie!")
    conn.close()

def list_clients():
    conn = sqlite3.connect('nitro_shine.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    print("\n--- BAZA KLIENTÓW NITRO SHINE ---")
    for c in clients:
        print(f"ID: {c[0]} | {c[1]} | Auto: {c[3]} | Tel: {c[2]}")
    conn.close()


def main():
    while True:
        choice = show_menu()
        if choice == '1':
            list_services()
        elif choice == '2':
            add_client()
        elif choice == '3':
            list_clients()
        elif choice == '0':
            print("Zamykanie systemu... Do zobaczenia w Nitro Shine! 👋")
            break
        else:
            print("❌ Nieprawidłowa opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main()