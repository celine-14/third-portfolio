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
SHEET = GSPREAD_CLIENT.open('level_of_participants')


def get_participants_data():
    """
    Get participants details from the user
    """
    print("Please enter participants data.")
    print("Data should include first name, last name, piano level, musicianship level, solfa level and conducting level, separated by commas.")
    print("Example: Jane, Doe, 4, 2, 1, 3\n")

    data_str = input("Enter your data here: ")

    participants_data = data_str.split(",")
    validate_data(participants_data)


def validate_data(values):
    """
    Inside the try, convert last 4 input values into integers.
    Raise ValueError if last 4 string inputs cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values[2:]]
        if len(values) != 6:
            raise ValueError(
                f"Exaclty 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


get_participants_data()
