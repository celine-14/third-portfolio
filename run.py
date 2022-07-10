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
    print(f"The data provided is {data_str}")

get_participants_data()
