# Shoe Inventory Management Program

## Overview
This Python program allows users to manage a shoe inventory system. The program provides functionalities to read shoe data from a file, add new shoes, view all shoes, re-stock shoes, search for specific shoes, calculate the total value for each shoe item, and find the shoe with the highest quantity.

## Features
- Read shoe data from a text file (inventory.txt) and create shoe objects.
- Add new shoes to the inventory.
- View all the shoes in a tabulated format.
- Re-stock shoes by increasing their quantity and updating the file.
- Search for specific shoes by their code and display their details.
- Calculate the total value for each shoe item (value = cost * quantity).
- Find the shoe with the highest quantity in stock.

## Dependencies
- Python 3.x
- tabulate module (to display data in tabulated format)

## How to Use
1. Clone the repository to your local machine.
2. Install the tabulate module if you haven't already:

pip install tabulate

3. Run the `inventory.py` script to launch the program.
4. Choose options from the menu to perform different operations.

## Data File (inventory.txt)
- The inventory data should be in CSV format with the following columns: "Country, Code, Product, Cost, Quantity"
- Example:

Country,Code,Product,Cost,Quantity
South Africa,SKU44386,Air Max 90,2300,20
China,SKU90000,Jordan 1,3200,50

## License
This project is licensed under the [MIT License](LICENSE).

Feel free to use, modify, and distribute this program as per the terms of the license.

## Author
Jesús Aryaváchin Márquez (https://www.linkedin.com/in/aryavachin/)

Let me know if you need any further assistance or clarification!
