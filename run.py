import gspread
from google.oauth2.service_account import Credentials

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


def validate_data(input):
    """
    Test user input matches options provided
    """
    try:
        if (input not in ("new", "update")):
            raise ValueError(f'You entered {input}, you need to enter "new" or "update" to continue')
    except ValueError as e:
        print(f'Invalid data: {e}, please try again. \n')

    return True

def update(input):
    if input == "new":
        return input
    elif input == "update":
        return input








def main():
    """
    run all functions
    """
    input = input_type()
    update(input)
print("Welcome to the Subshop")
main()
