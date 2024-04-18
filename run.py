import gspread
from google.oauth2.service_account import Credentials
import random
import pandas as pd
import numpy as np
import openpyxl

# Set scope for Google IAM authentication for the APIs the program has
# access to.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Declaring CONSTS
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('subshop')

# Extracting data to be used in program
items = SHEET.worksheet('items')
items_data = items.get_all_values()
stock = SHEET.worksheet('stock')
stock_data = stock.get_all_values()


def run_intro():
    """
    This function will introduce the user to the application
    and notifies them of the program scope.
    """
    # Multiline print statement will show the necessary information to the user for
    # program operation. Creating visual clarity through line separation.
    print('''
<==============================================================================================>
Welcome to the Subshop! Coded by Gaurav Jagpal (c) 2024.
        
The Subshop's inventory tool will easily calculate your shop requirements so you know what 
is needed for the next day.
        
The Subshop tool will ask you to provide information such as:
    - new/update (to know whether you plan on adding a new item or update an existing one)
    - If you select "new", it will also ask you for the item name, the min stock required,
      the time to make, cost of the item, sale price and it will calculate the profit.
      It will then append this to the "items" tab and "stock" tab of your worksheet.
    - If you select "update", it will automatically bring the item_code from the "items" tab,
      it will ask you how many items were sold, the minimum stock required and then it will
      calculate the stock on hand and the amount you need to make.

<==============================================================================================>
    ''')

def input_type():
    """
    User input for whether to add a new item or to update an item
    """
    while True:
        print('Would you like to add a new item or update sales figures?')
        data_str = input('Please enter "new" for new item or "update" for updating an item or "delete" to remove an existing item: \n')

        if validate_data(data_str):
            break

    return data_str

# Giving the user more variety for initial input
new = ["new", "NEW", "New"]
updater = ["update", "UPDATE", "Update"]
delete = ["delete", "DELETE", "Delete"]
# Combining the options
user_options = new + updater + delete

def validate_data(data):
    """
    Test user input matches options provided
    """
    try:
        if data not in user_options:
            raise ValueError(f'You entered {input}, you need to enter "new", "update" or "delete" to continue')
    except ValueError as e:
        print(f'Invalid data: {e}, please try again. \n')

    return True


def update(data):
    if data in new:
        """
        Add new items into item tab
        """
        item_name = input('Please enter product name: \n')
        df = SHEET.worksheet('items')
        first_col_items = df.col_values(1)
        if item_name in first_col_items:
            print('This item is already being produced. Please choose to update instead.')
        else:
            item_code = item_name[0:3] + str(random.randrange(100,999))
            min_stock = int(input('Please enter the minimum stock required: \n'))
            make_time_mins = int(input('Please enter how long the item takes to cook (in minutes): \n'))
            cost = float(input('How much does this item cost to prepare? (e.g 0.20) \n'))
            sale_price = float(input('How much will this item sell for: (e.g 1.30)\n'))
            profit = sale_price - cost
            items_to_update = [item_name, item_code, min_stock, make_time_mins, cost, sale_price, profit]
            items.append_row(items_to_update)
            sales = 0
            stock_on_hand = min_stock - sales
            to_make = min_stock - stock_on_hand
            total_profit = profit * sales
            stock_to_update = [item_name, item_code, sales, min_stock, stock_on_hand, to_make, total_profit]
            stock.append_row(stock_to_update)
        
    elif data in updater:
        """
        Update existing items located in stock tab
        """
        item_name = input('Please enter product name: \n')
        df = SHEET.worksheet('items')
        first_col_stock = df.col_values(1)
        df1 = SHEET.worksheet('stock')
        first_col_stock = df1.col_values(1)
        if item_name in first_col_stock:
            df = pd.DataFrame(items_data)
            grade = np.where(df[:][0] == item_name)
            index = (grade[0])[0]

            #User inputs
            sales = int(input('Please enter how many items were sold:\n'))
            min_stock = int(input('Please enter the minimum stock required for tomorrow:\n'))
            make_time_mins = int(input('How many minutes will it take to make the item:\n'))
            cost = float(input('How much does this item cost to prepare? (e.g 0.20) \n'))
            sale_price = float(input('How much will this item sell for: (e.g 1.30)\n'))

            #Formulas
            stock_on_hand = min_stock - sales
            to_make = min_stock - stock_on_hand
            profit = sale_price - cost
            total_profit = profit * sales

            #Update items tab
            items.update_cell(index+1,3, min_stock)
            items.update_cell(index+1,4, make_time_mins)
            items.update_cell(index+1,5, cost)
            items.update_cell(index+1,6, sale_price)
            items.update_cell(index+1,7, profit)

            #update stock page
            df = pd.DataFrame(items_data)
            grade1 = np.where(df[:][0] == item_name)
            index1 = (grade1[0])[0]
            stock.update_cell(index1+1,3, sales)
            stock.update_cell(index1+1,4, min_stock)
            stock.update_cell(index1+1,5, stock_on_hand)
            stock.update_cell(index1+1,6, to_make)
            stock.update_cell(index1+1,7, total_profit)
        else:
            print('This item is not in the current stock. Please add as a new item.\n')
        return data
    
    elif data in delete:
        item_name = input('Please enter the product name of what you would like to remove from your store: \n')
        df = SHEET.worksheet('items')
        first_col_items = df.col_values(1)
        if item_name in first_col_items:
            df = pd.DataFrame(items_data)
            grade = np.where(df[:][0] == item_name)
            index = int((grade[0])[0])
            SHEET.worksheet('items').delete_rows(index+1)
            SHEET.worksheet('stock').delete_rows(index+1)
        else:
            print('You do not currently produce this item')    
    else:
        print('You do not currently produce this item')


def reuse():
    again = input('Would you like to input more data? Please enter "Yes" or any key to escape\n')
    yes = ['yes','Yes', 'y', 'Y']
    if again in yes :
        main()


def return_data(stock_data):
    """
    Displays the output of the latest data set as a DataFrame
    """
    df = pd.DataFrame(stock_data)
    print(df)

def main():
    """
    run all functions
    """
    input = input_type()
    update(input)
    items2 = SHEET.worksheet('items')
    items_data2 = items2.get_all_values()
    stock2 = SHEET.worksheet('stock')
    stock_data2 = stock2.get_all_values()
    print('\n')
    print('Your stores product details are as below:')
    return_data(items_data2)
    print('\n')
    print('You store has the below requirements')
    return_data(stock_data2)
    reuse()

#Run intro first as if the user wants to reuse the tool, we don't want the intro to run again
run_intro()
print("Welcome to the Subshop \n")
main()

