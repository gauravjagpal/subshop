import gspread
from google.oauth2.service_account import Credentials
import random
import pandas as pd
import seaborn as sns
import numpy as np

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('subshop')

items = SHEET.worksheet('items')
items_data = items.get_all_values()
stock = SHEET.worksheet('stock')
stock_data = items.get_all_values()


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
          
    The Subshop's inventory tool will easily calculate your shop requirements so you
    know what is needed for the next day.
          
    The Subshop tool will ask you to provide information such as:
          - new/update (to know whether you plan on adding a new item or update an existing one)
          - If you select "new", it will also ask you for the item name, the min stock required,
            the time to bake, cost of the item, sale price and it will calculate the profit.
            It will then append this to the "items" tab and "stock" tab of your worksheet.
          - If you select "update", it will automatically bring the item_code from the "items" tab,
            it will ask you how many items were sold, the minimum stock required and then it will
            calculate the stock on hand and the amount you need to bake.

    <==============================================================================================>
    ''')

def input_type():
    """
    User input for whether to add a new item or to update an item
    """
    while True:
        print('Would you like to add a new item or update sales figures?')
        data_str = input('Please enter "new" for new item or "update" for updating an item: \n')

        if validate_data(data_str):
            break

    return data_str


def validate_data(data):
    """
    Test user input matches options provided
    """
    try:
        if (data not in ("new", "update")):
            raise ValueError(f'You entered {input}, you need to enter "new" or "update" to continue')
    except ValueError as e:
        print(f'Invalid data: {e}, please try again. \n')

    return True


def update(data):
    if data == "new":
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
            bake_time_mins = int(input('Please enter how long the item takes to cook (in minutes): \n'))
            cost = float(input('How much does this item cost to prepare? (e.g 0.20) \n'))
            sale_price = float(input('How much will this item sell for: (e.g 1.30)\n'))
            profit = sale_price - cost
            items_to_update = [item_name, item_code, min_stock, bake_time_mins, cost, sale_price, profit]
            items.append_row(items_to_update)
            sales = 0
            stock_on_hand = min_stock - sales
            to_bake = min_stock - stock_on_hand
            stock_to_update = [item_name, item_code, sales, min_stock, stock_on_hand, to_bake]
            stock.append_row(stock_to_update)
            return items_to_update
        
    elif data == "update":
        """
        Update existing items
        """
        item_name = input('Please enter product name: \n')
        df = SHEET.worksheet('stock')
        first_col_stock = df.col_values(1)
        if item_name in first_col_stock:
            df = pd.DataFrame(items_data)
            grade = np.where(df[:][0] == item_name)
            index = int(grade[0])
            item_code = (items_data[index])[1]
            sales = int(input('Please enter how many items were sold: \n'))
            min_stock = int(input('Please enter the minimum stock required: \n'))
            stock_on_hand = min_stock - sales
            to_bake = min_stock - stock_on_hand
            stock.update_cell(index+1,3, sales)
            stock.update_cell(index+1,4, min_stock)
            stock.update_cell(index+1,5, stock_on_hand)
            stock.update_cell(index+1,6, to_bake)
        else:
            print('This item is not in the current stock. Please add as a new item.')
        return data








def main():
    """
    run all functions
    """
    run_intro()
    input = input_type()
    update(input)
print("Welcome to the Subshop \n")
main()