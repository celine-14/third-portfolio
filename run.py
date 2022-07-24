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


def get_participant_data():
    """
    Get participant's details from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of first name,
    last name, and 4 numbers separated by commas.
    The loop will repeatedly request data until it is valid.
    """
    while True:
        print("Please enter participant's data.")
        print(
            "Data should include first name, last name, piano level,"
            "musicianship level, solfa level and conducting level,"
            "separated by commas without spaces."
            )
        print("Example: Jane,Doe,4,2,1,3\n")
        data_str = input("Enter your data here:\n")
        participant_data = data_str.split(",")
        data_integer = [int(value) for value in participant_data[2:]]
        participant_data = participant_data[:2] + data_integer

        if validate_data(participant_data):
            print("Data is valid!")
            break
    return participant_data


def validate_data(values):
    """
    Inside the try, convert last 4 input values into integers,
    and validate first 2 input strings.
    Raise ValueError if last 4 string inputs cannot be converted into int,
    if there aren't exactly 6 values, if first and last names are not provided.
    """
    error_message = ""
    for value in values[:2]:
        if not value.isalpha():
            error_message = "First and Last name must be in alphabets"
        elif len(value) < 2:
            error_message = "Names must be more than 1 letter"         
    if len(values) != 6:
        error_message = f"Exaclty 6 values required, you provided {len(values)}"

    print(error_message)
    return error_message == ""


def update_participant_data(data):
    """
    Append the participant's worksheet to the data source
    """
    print("Updating participants worksheet...\n")
    participants_worksheet = SHEET.worksheet("participants")
    participants_worksheet.append_row(data)
    print("Participants worksheet updated successfully.\n")


def calculate_average_level(participant_levels):
    """
    Calculate average music level for each paricipants,
    and round up to the nearest integer.
    """
    print("Calculating average level...\n")
    average_data = []
    level_average = int(round((sum(participant_levels)) / 4))
    average_data.append(level_average)
    print(average_data)
    return average_data


def update_participant_data_levels(data):
    """
    Append the levels worksheet add new row with the names provided.
    """
    print("Updating levels worksheet...\n")
    levels_worksheet = SHEET.worksheet("levels")
    levels_worksheet.append_row(data)
    print("Levels worksheet updated successfully.\n")


def main():
    """
    Run all program functions
    """
    data = get_participant_data()
    participant_names = [name.capitalize() for name in data[:2]]
    participant_levels = [int(num) for num in data[2:]]
    participant_data = participant_names + participant_levels
    update_participant_data(participant_data)

    new_average_level = calculate_average_level(participant_levels)
    participant_average_level = participant_names + new_average_level
    update_participant_data_levels(participant_average_level)


print("Welcome to Participants Data Automation")

if __name__ == '__main__':
    main()
