import mysql.connector
import pandas as pd  
import time

db = mysql.connector.connect(host="localhost",user="root",password="Ayush@123")

cursor = db.cursor()
cursor.execute("""
    CREATE DATABASE IF NOT EXISTS pocketdir;
""")

cursor.execute("""
    USE pocketdir;
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS contact_information(
        name varchar(30) primary key,
        age int,
        gender char(2),
        address varchar(100),
        phone_no varchar(100),
        email varchar(30)
    );
""")


def intro():
    print("=" * 80)
    print("{:^80s}".format("POCKET DICTIONARY"))
    print("{:^80s}".format("CONTACT"))
    print("{:^80s}".format("MANAGEMENT SYSTEM"))
    print("{:^80s}".format("WE ARE HERE TO KEEP YOUR CONTACT DATA ORGANIZED AND ACCESSIBLE"))
    print("{:^80s}".format("MADE BY: SHUBHAM KUMAR, SOUNAK MAITI AND AYUSH SAHU"))
    print("{:^80s}".format("CLASS XII SCIENCE"))
    print("=" * 80)
    print()
    time.sleep(0.5)


def create_record():
    name = input("Enter Contact Name: ")
    age=input("Enter your age:")
    gender=input("Enter your gender:")
    address = input("Enter Contact Residential/Official Address: ")
    phone_no = input("Enter Phone Number: ")
    email = input("Enter Valid Email id: ")
    sql = "INSERT INTO contact_information(name,age,gender,address,phone_no,email) VALUES (%s,%s,%s,%s,%s,%s)"
    record = (name,age,gender,address,phone_no,email)
    cursor.execute(sql, record)
    db.commit()
    print("Contact Record Entered Successfully...\n")


def search(name):
    sql = "SELECT * FROM contact_information WHERE name = %s"
    value = (name,)
    cursor.execute(sql, value)
    record = cursor.fetchone()
    if record is None:
        print("No Such Record Exists..Try Again")
    else:
        print('Name of Contact:', record[0])
        print('Age of Contact:',record[1])
        print('Gender of Contact:',record[2])
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
    sql = "DELETE FROM contact_information WHERE name = %s"
    value = (name,)
    cursor.execute(sql, value)
    db.commit()
    if cursor.rowcount == 0:
        print("Record Not Found...Please Enter Correct Name")
    else:
        print("Record Deleted Successfully...")


def modify_record(name):
    sql = "SELECT * FROM contact_information WHERE name = %s"
    new_name=name
    value = (name,)
    cursor.execute(sql, value)
    record = cursor.fetchone()
    if record is None:
        print("No Such Record Exists...Please Enter Correct Data")
    else:
        while True:
            name=new_name
            print("\nPress the Option You Want to Edit: ")
            print("1. Name of Contact")
            print("2. Age of Contact")
            print("3. Gender of Contact")
            print("4. Address of Contact")
            print("5. Phone Number of Contact")
            print("6. Email id of Contact")
            print("7. Move Back to the Main Menu")
            print()
            ch = int(input("Select Your Option (1-7): "))
            if ch == 1:
                new_name = input("Enter New Name of Contact: ")
                sql = "UPDATE contact_information SET name = %s WHERE name = %s"
                values = (new_name, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Contact Record Updated Successfully...")
            elif ch == 2:
                new_age = input("Enter New Age of Contact: ")
                sql = "UPDATE contact_information SET age = %s WHERE name = %s"
                values = (new_age, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Contact Record Updated Successfully...")

            elif ch == 3:
                new_gender = input("Enter New Gender of Contact: ")
                sql = "UPDATE contact_information SET gender = %s WHERE name = %s"
                values = (new_name, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Contact Record Updated Successfully...")

            elif ch == 4:
                new_address = input("Enter New Address of Contact: ")
                sql = "UPDATE contact_information SET address = %s WHERE name = %s"
                values = (new_address, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Address Updated Successfully...")
            elif ch == 5:
                new_phone_no = input("Enter New Phone no. of Contact : ")
                sql = "UPDATE contact_information SET phone_no = %s WHERE name = %s"
                values = (new_phone_no, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Phone Number Updated Successfully...")
            elif ch == 6:
                new_email = input("Enter New Email id of Contact : ")
                sql = "UPDATE contact_information SET email = %s WHERE name = %s"
                values = (new_email, name)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "Email id Updated Successfully...")
            elif ch == 7:
                print("\n_________Thank you______________")
                break
            else:
                print("Invalid choice !!! ...Please enter appropriate choice(1/2/3/4/5/6/7)\n")


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
        print()
        ch = int(input("Select your option from the above menu(1-6): "))
        print()
        if ch == 1:
            print("ADD NEW CONTACT RECORD")
            create_record()
        elif ch == 2:
            print("SEARCH CONTACT RECORD BY NAME")
            name = input("Enter Name: ")
            search(name)
        elif ch == 3:
            print("DISPLAY ALL CONTACT RECORDS")
            display_all()
        elif ch == 4:
            print("DELETE A CONTACT RECORD")
            name = input("Enter Name: ")
            delete_record(name)
        elif ch == 5:
            print("MODIFY A CONTACT RECORD")
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
