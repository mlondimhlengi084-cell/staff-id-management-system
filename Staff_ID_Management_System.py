# Staff ID Management System 

# read a file named StaffID.txt
Staff_ID = []

def read_file():
    try:


        with open("StaffID.txt", "r") as file:
            for line in file:
                Staff_ID.append(int(line))
        return Staff_ID
    except FileNotFoundError:
        print("Errror. The file you want to access was not found.")


# Display menu

def display_menu():
    print("\n1. Display all staff IDs")
    print("2. Add a new staff ID.")
    print("3. Remove a staff ID.")
    print("4. Show senior staff member.")
    print("5. Save the list to file.")
    print("6. Exit.")

# 1. Display all staff IDs.

def display_IDs(Staff_ID):
    print("\n===== STAFF IDs =====")
    print("-" * 25 )

    for i in range(len(Staff_ID)):
        print(f"{1 + i}. {Staff_ID[i]}")

# check ID

def check_ID():

    while True:
        try:
            ID = int(input("Enter ID: "))

            if ID % 6 == 0:
                return ID
            else:
                print("Invalid input. ID must be a positive number divisible by 6.")
        except ValueError:
            print("Error. Please enter a positive whole number divisible by 6.")

# 2. Add a new ID

def add_ID(Staff_ID):

    ID = check_ID()

    Staff_ID.append(ID)

    print(f"ID: {ID} was added successfully.")

# 3. Remove a staff ID

def remove_ID(Staff_ID):

    # display staff IDs to and choose the number you want to remove

    display_IDs(Staff_ID)

    correct = False

    while not correct:
        try:

            ID_remove = int(input("\nPlease enter the number of ID you want to remove: "))

            if ID_remove <= 0 or ID_remove > len(Staff_ID):
                print("The number entered was not found from the IDs numbers.")

            else:
                removed = Staff_ID[ID_remove - 1 ]
                Staff_ID.pop(ID_remove - 1 )
                print(f"ID: {removed} was successfully removed.")

                correct = True
        except ValueError:
            print("Invalid input. Please enter a valid number. Characters are not accepted.")

# 4. Show senior staff member

def show_senior(Staff_ID):

    lowest_ID = Staff_ID[0] 

    for ID in Staff_ID:

        if ID < lowest_ID:
            lowest_ID = ID
    print(f"Senior Member: {lowest_ID}")
          
# 5. Save list to file

def write_file(Staff_ID):
    try:
        with open("StaffID.txt", "w") as file:
            for ID in Staff_ID:
                file.write(f"{ID}\n")
        print("The list was successfully saved to StaffID.txt.")

    except FileNotFoundError:
        print("Error. The file you want to write was not found.")

def save_list(Staff_ID):
    write_file(Staff_ID)

# main function

def main():

    Staff_ID =read_file()

    while True:
        display_menu()
        option = int(input("Option: "))

        if option == 1:
            
            display_IDs(Staff_ID)

        elif option == 2:
            add_ID(Staff_ID)

        elif option == 3:
            remove_ID(Staff_ID)

        elif option == 4:
            show_senior(Staff_ID)

        elif option == 5:
            
            save_list(Staff_ID)

        elif option == 6:
            print("Goodbye...")
            break

        else:
            print("Invalid option. Please enter an option from the menu.")

main()




