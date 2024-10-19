import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",    
    user="root",         
    password="Aruldeva@273", 
    database="food_monitoring"
)

cursor = conn.cursor()

# Function to add food item
def add_food_item(name, quantity, expiry_date):
    query = "INSERT INTO food_items (name, quantity, expiry_date) VALUES (%s, %s, %s)"
    values = (name, quantity, expiry_date)
    cursor.execute(query, values)
    conn.commit()
    print(f"Food item '{name}' added successfully!")

# Function to view all food items
def view_food_items():
    query = "SELECT * FROM food_items"
    cursor.execute(query)
    results = cursor.fetchall()
    if results:
        print("ID | Name         | Quantity | Expiry Date")
        print("------------------------------------------")
        for row in results:
            print(f"{row[0]}  | {row[1]} | {row[2]}      | {row[3]}")
    else:
        print("No food items found.")

# Function to delete food item by ID
def delete_food_item(item_id):
    query = "DELETE FROM food_items WHERE id = %s"
    cursor.execute(query, (item_id,))
    conn.commit()
    print(f"Food item with ID {item_id} deleted successfully!")

# Menu to interact with the system
def menu():
    while True:
        print("\n=== Food Monitoring System ===")
        print("1. Add Food Item")
        print("2. View Food Items")
        print("3. Delete Food Item")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter food name: ")
            quantity = int(input("Enter quantity: "))
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
            try:
                expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()
                add_food_item(name, quantity, expiry_date)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        elif choice == '2':
            view_food_items()
        
        elif choice == '3':
            item_id = int(input("Enter food item ID to delete: "))
            delete_food_item(item_id)
        
        elif choice == '4':
            print("Exiting the system...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()

# Close the connection when done
cursor.close()
conn.close()
