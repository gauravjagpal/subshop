import gspread
from google.oauth2.service_account import Credentials
import random
import pandas as pd
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
data = items.get_all_values()

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
        item_code = item_name[0:3] + str(random.randrange(100,999))
        min_stock = int(input('Please enter the minimum stock required: \n'))
        bake_time_mins = input('Please enter how long the item takes to cook (in minutes): \n')
        cost = float(input('How much does this item cost to prepare? (e.g 0.20) \n'))
        sale_price = float(input('How much will this item sell for: (e.g 1.30)\n'))
        profit = sale_price - cost
        items_to_update = [item_name, item_code, min_stock, bake_time_mins, cost, sale_price, profit]
        items.append_row(items_to_update)
        return items_to_update
        
    elif data == "update":
        """
        Update existing items
        """
        item_name = input('Please enter product name: \n')
        df = SHEET.worksheet('items')
        first_col = df.col_values(1)
        for i in first_col:
            if i == item_name:
                print('This item is already being produced. Please choose to update instead')
            else:
                #item_code = *VLOOKUP*
                sales = int(input('Please enter how many items were sold: \n'))
                min_stock = int(input('Please enter the minimum stock required: \n'))
                stock_on_hand = min_stock - sales
                to_bake = min_stock - stock_on_hand
                items_to_update = [item_name, item_code, sales, min_stock, stock_on_hand, to_bake]
        return data








def main():
    """
    run all functions
    """
    input = input_type()
    update(input)
print("Welcome to the Subshop")
main()
