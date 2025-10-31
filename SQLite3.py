import sqlite3
import pandas as pd
import time

# Create or connect to SQLite database file
db = sqlite3.connect("pocketdir.db")
cursor = db.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contact_information(
        name TEXT PRIMARY KEY,
        age INTEGER,
        gender TEXT,
        address TEXT,
        phone_no TEXT,
        email TEXT
    );
""")

def intro():
    print(Fore.CYAN + "=" * 80)
    print(Fore.YELLOW + "{:^80s}".format("💼 POCKET DIRECTORY"))
    print(Fore.CYAN + "{:^80s}".format("📇 CONTACT MANAGEMENT SYSTEM"))
    print(Fore.MAGENTA + "-" * 80)
    print(Fore.GREEN + "{:^80s}".format("A Smart Way to Manage Your Contacts"))
    print(Fore.MAGENTA + "-" * 80)
    print(Fore.BLUE + "{:^80s}".format("TEAM PROJECT_5"))
    print(Fore.WHITE + "{:^80s}".format("Ayush Sahu • Abhay Niranjan • Arjun Verma • Divyanshu • Keshav Singh"))
    print(Fore.CYAN + "=" * 80)
    print(Style.BRIGHT + "\nLoading system modules...\n")
    time.sleep(1)


def create_record():
    name = input("Enter Contact Name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    address = input("Enter Contact Residential/Official Address: ")
    phone_no = input("Enter Phone Number: ")
    email = input("Enter Valid Email id: ")
    sql = "INSERT INTO contact_information (name, age, gender, address, phone_no, email) VALUES (?, ?, ?, ?, ?, ?)"
    record = (name, age, gender, address, phone_no, email)
    try:
        cursor.execute(sql, record)
        db.commit()
        print("Contact Record Entered Successfully...\n")
    except sqlite3.IntegrityError:
        print("Error: Contact with this name already exists.\n")

def search(name):
    sql = "SELECT * FROM contact_information WHERE name = ?"
    cursor.execute(sql, (name,))
    record = cursor.fetchone()
    if record is None:
        print("No Such Record Exists..Try Again")
    else:
        print('Name of Contact:', record[0])
        print('Age of Contact:', record[1])
        print('Gender of Contact:', record[2])
        print('Address of Contact:', record[3])
        print('Phone Number of Contact:', record[4])
        print('E-mail id of Contact:', record[5])

def display_all():
    cursor.execute("SELECT * FROM contact_information")
    records = cursor.fetchall()
    if records:
        df = pd.DataFrame(records, columns=['Name', 'Age', 'Gender', 'Address', 'Phone Number', 'Email'])
        print(df.to_string(index=False))
    else:
        print("No contact records found.")

def delete_record(name):
    sql = "DELETE FROM contact_information WHERE name = ?"
    cursor.execute(sql, (name,))
    db.commit()
    if cursor.rowcount == 0:
        print("Record Not Found...Please Enter Correct Name")
    else:
        print("Record Deleted Successfully...")

def modify_record(name):
    cursor.execute("SELECT * FROM contact_information WHERE name = ?", (name,))
    record = cursor.fetchone()
    if record is None:
        print("No Such Record Exists...Please Enter Correct Data")
    else:
        while True:
            print("\nPress the Option You Want to Edit: ")
            print("1. Name of Contact")
            print("2. Age of Contact")
            print("3. Gender of Contact")
            print("4. Address of Contact")
            print("5. Phone Number of Contact")
            print("6. Email id of Contact")
            print("7. Move Back to the Main Menu")
            ch = int(input("Select Your Option (1-7): "))
            
            if ch == 1:
                new_name = input("Enter New Name of Contact: ")
                cursor.execute("UPDATE contact_information SET name = ? WHERE name = ?", (new_name, name))
            elif ch == 2:
                new_age = input("Enter New Age of Contact: ")
                cursor.execute("UPDATE contact_information SET age = ? WHERE name = ?", (new_age, name))
            elif ch == 3:
                new_gender = input("Enter New Gender of Contact: ")
                cursor.execute("UPDATE contact_information SET gender = ? WHERE name = ?", (new_gender, name))
            elif ch == 4:
                new_address = input("Enter New Address of Contact: ")
                cursor.execute("UPDATE contact_information SET address = ? WHERE name = ?", (new_address, name))
            elif ch == 5:
                new_phone_no = input("Enter New Phone no. of Contact: ")
                cursor.execute("UPDATE contact_information SET phone_no = ? WHERE name = ?", (new_phone_no, name))
            elif ch == 6:
                new_email = input("Enter New Email id of Contact: ")
                cursor.execute("UPDATE contact_information SET email = ? WHERE name = ?", (new_email, name))
            elif ch == 7:
                print("\nReturning to main menu...")
                break
            else:
                print("Invalid choice! Try again.")

            db.commit()
            print("Contact Record Updated Successfully...")

def main():
    intro()
    while True:
        print("\nMAIN MENU ")
        print("1. ADD NEW CONTACT RECORD")
        print("2. SEARCH CONTACT RECORD")
        print("3. DISPLAY ALL CONTACT RECORDS")
        print("4. DELETE A CONTACT RECORD")
        print("5. MODIFY A CONTACT RECORD")
        print("6. EXIT")
        ch = int(input("Select your option (1-6): "))
        print()
        
        if ch == 1:
            create_record()
        elif ch == 2:
            name = input("Enter Name: ")
            search(name)
        elif ch == 3:
            display_all()
        elif ch == 4:
            name = input("Enter Name: ")
            delete_record(name)
        elif ch == 5:
            name = input("Enter Name: ")
            modify_record(name)
        elif ch == 6:
            print("Thanks for Using Contact Information Management System")
            print("Please Visit Us Again")
            db.close()
            break
        else:
            print("Invalid choice")

main()
