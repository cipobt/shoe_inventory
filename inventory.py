from tabulate import tabulate


class Shoe:
    """
    Class representing a shoe item.

    Attributes:
        country (str): Shoe's country of origin.
        code (str): Shoe item's code.
        product (str): Shoe item's product name.
        cost (float): Shoe item's cost.
        quantity (int): Shoe item's quantity in stock.
    """

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """
        :return: Shoe item's cost
        """
        return self.cost

    def get_quantity(self):
        """
        :return: Shoe item's quantity
        """
        return self.quantity

    def __str__(self):
        """
        :return: Shoe item's full description in a single string
        """
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


shoe_list = []


def read_shoes_data():
    """
    Reads the inventory.txt file to create Shoe objects.
    Then appends Shoe objects to shoe_list.
    """
    try:
        with open('inventory.txt', 'r') as f:
            next(f)
            for line in f:
                line = line.strip().split(',')
                shoe = Shoe(line[0], line[1], line[2], float(line[3]), int(line[4]))
                shoe_list.append(shoe)
        print("Shoe data has been read from inventory.txt and added to shoe list.")
    except FileNotFoundError:
        print("inventory.txt file not found.")


def capture_shoes():
    """
    Receives input from user to create a Shoe object.
    Then appends Shoe objects to shoe_list.
    """
    while True:
        try:
            country = input("Country of origin: ")
            code = input("Shoe code: ")
            product = input("Product name: ")
            cost = float(input("Cost: "))
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Invalid input!")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    stock_file = open("inventory.txt", 'a')
    stock_file.write(f"\n{country},{code},{product},{cost},{quantity}")
    stock_file.close()
    print(f"{product} added to the inventory.")


def view_all():
    """
    Iterates over the shoe_list and prints a table of shoe data.
    """
    if shoe_list:
        headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity']
        rows = [[shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity] for shoe in shoe_list]
        print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))  # orgtbl
    else:
        print("No shoe in stock")


def re_stock():
    """
    Finds the Shoe object with the lowest quantity and asks the user to add more.
    Updates the Shoe object's quantity and the inventory.txt file.
    """
    # I followed https://medium.com/analytics-vidhya/how-to-use-key-function-in-max-and-min-in-python-1fdbd661c59c
    # for guidance on how to use key=lambda
    if shoe_list:
        lowest_quantity_shoe = min(shoe_list, key=lambda x: x.get_quantity())
        print(f"The shoe with the lowest quantity is: {lowest_quantity_shoe.product}")
        answer = input(f"Do you want to add more {lowest_quantity_shoe.product} shoes? (y/n) ")
        if answer == 'y':
            while True:
                try:
                    additional_quantity = int(input("How many more shoes do you want to add? "))
                    break
                except ValueError:
                    print("Please introduce a number")
            lowest_quantity_shoe.quantity += additional_quantity
            # update the inventory.txt file with the new quantity
            try:
                with open('inventory.txt', 'r') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if i == 0:
                            continue
                        shoe_data = line.strip().split(',')
                        if shoe_data[1] == lowest_quantity_shoe.code:
                            shoe_data[4] = str(lowest_quantity_shoe.quantity)
                            lines[i] = ','.join(shoe_data) + '\n'
                            break
                with open('inventory.txt', 'w') as f:
                    f.writelines(lines)
                print(f"{lowest_quantity_shoe.product} has been restocked.")
            except FileNotFoundError:
                print("inventory.txt not found.")
        else:
            print("No shoe in stock")


def search_shoe():
    """
    Searches for a Shoe object with a given shoe code and returns it.
    """
    if shoe_list:
        code = input("Enter the shoe code (CAPS SENSITIVE): ")
        for shoe in shoe_list:
            if shoe.code == code:
                print('Country    Code     Product    Cost  Quantity')
                print(shoe)
                return
        print("Shoe not found.")
    else:
        print("No shoe in stock")


def value_per_item():
    """
    Calculates the total value for each shoe item and prints the result.
    """
    if shoe_list:
        headers = ['Product', 'Value']
        rows = [[shoe.product, shoe.cost * shoe.quantity] for shoe in shoe_list]
        print(tabulate(rows, headers=headers, tablefmt='fancy_grid'))
    else:
        print("No shoe in stock")


def highest_qty():
    """
    Finds the Shoe object with the highest quantity and prints it.
    """
    if shoe_list:
        highest_quantity_shoe = max(shoe_list, key=lambda x: x.get_quantity())
        print(f"The shoe with the highest quantity is: {highest_quantity_shoe.product}")
    else:
        print("No shoe in stock")


#==========Main Menu=============
def main():
    """
    Nike warehouse Inventory Management System
    """
    read_shoes_data()

    while True:
        print("\nNike Warehouse Inventory Management System\n")
        print("1. Add a new shoe")
        print("2. View all shoes")
        print("3. Re-stock a shoe")
        print("4. Search for a shoe")
        print("5. Calculate the total value of each shoe item")
        print("6. Find the shoe with the highest quantity")
        print("7. Quit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            capture_shoes()
        elif choice == '2':
            view_all()
        elif choice == '3':
            re_stock()
        elif choice == '4':
            search_shoe()
        elif choice == '5':
            value_per_item()
        elif choice == '6':
            highest_qty()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
