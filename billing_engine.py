import sqlite3

# =====================================================================
# DATABSE SETUP (SQL Initialization)
# =====================================================================
def init_db():
    conn = sqlite3.connect("billing_system.db")
    cursor = conn.cursor()
    # Data tables banana jahan real schema store hoga
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            bill_type TEXT,
            consumer_name TEXT,
            units_consumed INTEGER,
            solar_exported INTEGER,
            total_bill REAL
        )
    """)
    conn.commit()
    conn.close()

# Database ko initialized karna code chalne se pehle
init_db()


# =====================================================================
# CORE LOGIC CLASSES (Meters Framework)
# =====================================================================
class UtilityBill:
    def __init__(self, consumer_name, units_consumed):
        self.consumer_name = consumer_name
        if units_consumed < 0:
            raise ValueError("Units consumed cannot be negative!")
        self.units_consumed = units_consumed
        self.rate_per_unit = 25  
        self.bill_type = "Standard"

    def calculate_bill(self):
        return self.units_consumed * self.rate_per_unit

    def save_to_database(self, solar_exp=0):
        # Professional Database Insertion System
        final_amount = self.calculate_bill()
        conn = sqlite3.connect("billing_system.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO invoices (bill_type, consumer_name, units_consumed, solar_exported, total_bill)
            VALUES (?, ?, ?, ?, ?)
        """, (self.bill_type, self.consumer_name, self.units_consumed, solar_exp, final_amount))
        conn.commit()
        conn.close()
        
        print("\n" + "="*50)
        print(f"✅ Success! {self.bill_type} Bill Saved to SQLite Database.")
        print(f"Consumer: {self.consumer_name} | Total Payable: Rs. {final_amount}")
        print("="*50)


class CommercialBill(UtilityBill):
    def __init__(self, consumer_name, units_consumed):
        super().__init__(consumer_name, units_consumed)
        self.bill_type = "Commercial"

    def calculate_bill(self):
        standard_amount = self.units_consumed * self.rate_per_unit
        return standard_amount + (standard_amount * 0.20)


class SmartMeterBill(UtilityBill):
    def __init__(self, consumer_name, units_consumed, solar_exported):
        super().__init__(consumer_name, units_consumed)
        if solar_exported < 0:
            raise ValueError("Solar exported units cannot be negative!")
        self.solar_exported = solar_exported  
        self.bill_type = "Smart/Solar"

    def calculate_bill(self):
        net_units = self.units_consumed - self.solar_exported
        if net_units < 0:
            net_units = 0
        return net_units * self.rate_per_unit


# =====================================================================
# THE INTERACTIVE INTERFACE (Main Menu Loop)
# =====================================================================
def main_menu():
    while True:
        print("\n⚡ ENTERPRISE-GRADE UTILITY BILLING SYSTEM ⚡")
        print("1. Generate Standard Home Bill")
        print("2. Generate Commercial Shop Bill")
        print("3. Generate Smart/Solar Grid Bill")
        print("4. View All Saved Invoices (From SQL Database)")
        print("5. Exit System")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '5':
            print("\nShutting down billing engine. Goodbye! 👋")
            break
            
        if choice in ['1', '2', '3']:
            name = input("Enter Consumer Name: ")
            try:
                units = int(input("Enter Units Consumed: "))
                
                if choice == '1':
                    bill = UtilityBill(name, units)
                    bill.save_to_database()
                elif choice == '2':
                    bill = CommercialBill(name, units)
                    bill.save_to_database()
                elif choice == '3':
                    solar = int(input("Enter Solar Units Exported: "))
                    bill = SmartMeterBill(name, units, solar)
                    bill.save_to_database(solar_exp=solar)
                    
            except ValueError as error:
                print(f"\n❌ Input Error: Details: {error}")
                
        elif choice == '4':
            print("\n" + "-"*60)
            print(" ID  | TYPE       | CONSUMER NAME    | CONSUMED | SOLAR | TOTAL BILL")
            print("-"*60)
            
            # Fetching data using pure SQL query
            conn = sqlite3.connect("billing_system.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM invoices")
            rows = cursor.fetchall()
            conn.close()
            
            if not rows:
                print("No records found in the database.")
            else:
                for row in rows:
                    print(f" {row[0]:<3} | {row[1]:<10} | {row[2]:<16} | {row[3]:<8} | {row[4]:<5} | Rs. {row[5]}")
            print("-"*60)
        else:
            print("❌ Invalid Choice! Select between 1 and 5.")

if __name__ == "__main__":
    main_menu()
