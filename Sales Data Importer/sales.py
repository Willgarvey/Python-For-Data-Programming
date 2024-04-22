def add_sales(sales):
    # input from the user for the sale amount
    while True:
        try:
            amount = input(str("Amount:\t\t\t"))
            amount = float(amount)
        except ValueError:
            print("Invalid input. Enter a number greater than zero and try again")
            continue
        if amount <= 0:
            print("Invalid input. Enter a number greater than zero and try again")
            continue
        else:
            break
    # input from the user about the year
    while True:
        try:
            year = input(str("Year:\t\t\t"))
            year = int(year)
        except ValueError:
            print("Invalid integer. Please enter a year greater than 2000.")
            continue
        # input must be between 200 and 9999
        if year < 2000 or year > 9999:
            print("Invalid integer. Please enter an integer greater than 2000.")
            continue
        else:
            break
    # input from the user about the month
    while True:
        try:     
            month = input(str("Month (1-12):\t\t"))
            month = int(month)
        except ValueError:
            print("Invalid integer. Enter an integer between 1 and 12.")
            continue
        if month < 1 or month > 12:
            print("Invalid integer. Enter an integer between 1 and 12.")
            continue
        else:
            break
    while True:
        # input from user for moth 2 must be between 1 and 28
        if month == 2:
            try:
                day = input(str("Day (1-28):\t\t"))
                day = int(day)
            except ValueError:
                print("Invalid integer. Enter an integer between 1 and 28.")
            if day < 1 or day > 28:
                print("Invalid integer. Enter an integer between 1 and 28.")
                continue
            else:
                break
        # input from user for moth 4, 6, 9, and 11 must be between 1 and 30
        elif month == 4 or month == 6 or month == 9 or month == 11:
            try:
                day = input(str("Day (1-30):\t\t"))
                day = int(day)
            except ValueError:
                print("Invalid integer. Enter an integer between 1 and 30.")
            except TypeError:
                print("Invalid integer. Enter an integer between 1 and 30.")
                continue
            if day < 1 or day > 30:
                print("Invalid integer. Enter an integer between 1 and 30..")
                continue
            else:
                break
        # input from months 1, 3, 5, 7 and 9 must be between 1 and 31
        else:
            try:
                day = input(str("Day (1-31):\t\t"))
                day = int(day)
            except ValueError:
                print("Invalid integer. Enter an integer between 1 and 31.")
                continue
            except TypeError:
                print("Invalid integer. Enter an integer between 1 and 31.")
                continue
            if day < 1 or day > 31:
                print("Invalid integer. Enter an integer between 1 and 31.")
                continue 
            else:
                break
    # create a list of the validate user input called entry
    entry = [amount,year,month,day]
    # add entry list to the sales list
    sales.append(entry)
    print()
    # confirm added sale and display the data of the sale
    print(f"Sales for {year}-{month}-{day} added.")
    return sales
    