import csv

def load_sales(sales):
    # try to load data from all_sales.csv
    try:
        with open("all_sales.csv", newline="") as file:
            reader = csv.reader(file)
            sales = list(reader)
            return sales
    # create the all_sales.csv file if not present
    except FileNotFoundError:
        print()
        print("Could not find contacts file!")
        print("Creating new sales file...")
        print()
        with open("all_sales.csv", "w") as file:
            writer = csv.writer(file)
            return sales
 
def save_sales(sales):
    #save the sales list to all_sales.csv
    with open("all_sales.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(sales)
    return sales  