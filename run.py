import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('level_of_participants')


def get_participants_data():
    """
    Get participants details from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of first name,
    last name, and 4 numbers separated by commas.
    The loop will repeatedly request data until it is valid.
    """
    while True:
        print("Please enter participants data.")
        print("Data should include first name, last name, piano level, \
musicianship level, solfa level and conducting level, \
separated by commas without spaces.")
        print("Example: Jane,Doe,4,2,1,3\n")
        data_str = input("Enter your data here: ")
        participants_data = data_str.split(",")

        if validate_data(participants_data):
            print("Data is valid!")
            break
    return participants_data


def validate_data(values):
    """
    Inside the try, convert last 4 input values into integers,
    and validate first 2 input strings.
    Raise ValueError if last 4 string inputs cannot be converted into int,
    if there aren't exactly 6 values, if first and last names are not provided.
    """
    try:
        for value in values[:-4]:
            if not value.isalpha():
                raise ValueError(
                    "First and Last name required. Names must be in alphabets"
                    )
            elif len(value) < 2:
                raise ValueError(
                    "Names must be more than 1 letter"
                    )
        [int(value) for value in values[2:]]
        if len(values) != 6:
            raise ValueError(
                f"Exaclty 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_participants_data(data):
    """
    Update participants worksheet, add new row with the list data provided.
    """
    print("Updating participants worksheet...\n")
    participants_worksheet = SHEET.worksheet("participants")
    participants_worksheet.append_row(data)
    print("Participants worksheet updated successfully.\n")


def update_participants_data_levels(data):
    """
    Update levels worksheet, add new row with the list data provided.
    """
    print("Updating levels worksheet...\n")
    levels_worksheet = SHEET.worksheet("levels")
    levels_worksheet.append_row(data)
    print("Levels worksheet updated successfully.\n")


def calculate_average_level(participants_row):
    """
    Calculate average music level for each paricipants
    """
    print("Calculating average level...\n")
    level_sum = sum(participants_row)
    level_average = level_sum / 4
    print(level_average)


def main():
    """
    Run all program functions
    """
    data = get_participants_data()
    participants_data = [name.capitalize() for name in data[:-4]] + [int(num) for num in data[2:]]
    participants_names = [name.capitalize() for name in data[:-4]]
    participants_level = [int(num) for num in data[2:]]
    update_participants_data(participants_data)
    update_participants_data_levels(participants_names)
    calculate_average_level(participants_level)


print("Welcome to Participants Data Automation")
main()
