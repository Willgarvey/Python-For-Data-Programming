#!/usr/bin/env python3

import csv
# local db.py file that contains functions to load and save data
import db
# local sales.py file that contains the function to manually add sales data
import sales       

def command_menu():
    # displays the command options to the user
    print("SALES DATA IMPORTER")
    print()
    print("COMMAND MENU")
    print("view\t- View all sales")
    print("add\t- Add sales")
    print("import\t- Import sales from a file")
    print("menu\t- Show menu")
    print("exit\t- Exit program")
    
def view_sales(all_sales):
    # check if the the all_sales list is empty
    if len(all_sales) == 0:
        print()
        print("There are no sales to view. Enter sales data and try again")
    # displays all sales data in the all_sales list
    else:
        print()
        print("Year\tDate\tQuarter\tAmount")
        print("-----------------------------------------")
        i=1
        total=0.0
        # quarter is calculated based on the month entry
        for sale in all_sales:
            m = int(sale[2])
            if m > 9:
                quarter=4
            elif m > 6 and m < 9:
                quarter=3
            elif m > 3 and m < 6:
                quarter=2
            else:
                quarter=1
            # display each list in the all_sales list a row in a table
            print(f"{i}.\t{sale[1]}-{sale[2]}-{sale[3]}\t{quarter}\t${(round(float(sale[0]), 2))}")
            i=i+1
            # calculate total sales to display
            total=total+float(sale[0])
        print("-----------------------------------------")
        print(f"TOTAL:\t\t\t\t${round(total,2)}")
        print()
             
def import_sales(all_sales):
    # import sales data from new .csv files and
    # validate data before adding to sales list
    import_history = []
    invalid_data = False
    
    # ask the user to input the csv file name
    sales_file = input(str("Enter name of file to import: "))
    
    # load the import_history.txt into the import_history list or create a new one
    try:
        import_history = []
        with open("import_history.txt") as file:  
            for line in file:
                line = line.strip()
                import_history.append(line)
    # creates a txt file to track import history
    except FileNotFoundError:
        print("import_history.txt file not found.")
        print()
        print("Creating import_history.txt now...")
        with open("import_history.txt", "w") as outfile:
            outfile.write(" ")
        with open("import_history.txt") as file:  
            for line in file:
                line = line.strip()
                import_history.append(line)
                
    # check if file name inputted by user has already been imported
    for filename in import_history:        
        if filename == sales_file:
            print("File has already been imported.")
            return all_sales
    while True:
        try:
            # load the sales data from the csv file to a list to validate the data
            sales_data = []
            with open(sales_file, newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    sales_data.append(row)
                    
            # check each entry in the csv for valid data
            # based on the requirements for each list index
            # depending on the expected data type
            # if any data is found to be invalid the
            # boolean "invalid_data" is set to true to display
            # results once iteration is complete
            for data in sales_data:
                try:
                    data[0] = float(data[0])
                except ValueError:
                    data[0] = "*" + data[0]
                    invalid_data = True
                try:
                    data[1] = int(data[1])
                except ValueError:
                    data[1] = "*" + data[1]
                    invalid_data = True
                try:
                    data[2] = int(data[2])
                except ValueError:
                    data[2] = "*" + data[2]
                    invalid_data = True
                try:
                    data[3] = int(data[3])
                except ValueError:
                    data[3] = "*" + data[3]
                    invalid_data = True
        except:
            print(f"File with name {sales_file} was not found. Please enter another file name and try again. ")
            break
        # display the data from the csv file with asterisks in front of any
        # data entries that have invalid data in them based on the parameters
        # to validate the data
        if invalid_data == True:
            print(f"{sales_file} contains data formatted improperly. ")
            print()
            print("Year\tMonth\tDay\tAmount")
            print("--------------------------------------")
            for data in sales_data:
                mark="  "
                try:
                    if any("*" in s for s in data):
                        mark="? "
                except:
                    mark="  "
                print(f"{mark}{data[1]}\t{data[2]}\t{data[3]}\t{(data[0])}")
            print("--------------------------------------")
            print()
            print("Please review entries with an asterisk and fix before importing and try again.")
            break
        # add sales data to the all_sales list once the data has been validated
        else:    
            with open(sales_file, newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    all_sales.append(row)
                import_history.append(sales_file)
                #add csv file name to import_history.txt file
                with open("import_history.txt", "w") as file:
                    for filename in import_history:
                        file.write(f"{filename}\n")
                # save the all_sales list to the all_sales.csv file
                db.save_sales(all_sales)
                print()
                print(f"{sales_file} has been imported.")
                return all_sales

def main():
    all_sales = []
    # load data from all_sales.csv into the all_sales list
    # if no csv is present the file all_sales.csv is created
    all_sales = db.load_sales(all_sales)
    # display the command manu to the user
    command = "view"
    command_menu()
    # start a loop of user input options that manipulate the data until exit is triggered
    while command != "exit":
        print()
        # input from the user to select a command
        command = input(str("Please enter a command: "))        
        if command == "view":
            view_sales(all_sales)   
        elif command == "add":
            sales.add_sales(all_sales)
            # db.save_sales(all_sales)
        elif command == "import":
            import_sales(all_sales)
        elif command == "menu":
            command_menu()
        elif command == "exit":
            db.save_sales(all_sales)
            print("Bye!")
        # Any option that is not exactly correct will trigger this else statement
        # and prompt the user for another command
        else:
            print()
            print("Please enter a command from the COMMAND WINDOW")
            print()
            
if __name__ == "__main__":
    main()