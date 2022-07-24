## Table of Contents
* [Introduction](#introduction)
* [Data Model](#data-model)
* [Testing](#testing)
    * [User Input Testing Testing](#user-input-testing)
    * [Validator Testing](#validator-testing)
* [Deployment](#deployment)
    * [Live Link](#live-link)
    * [Repository](#repository)
* [Credits](#credits)

# Participants Data Automation

## Introduction
This data automation collects participants' data, calculate the average level and assigns participants to their respective class levels. The different music areas that takes into account when assigning classes are piano level, musicianship level, solfa level and conducting level. Flow chart below shows the logic of my project.

![Lucid Chart](https://github.com/celine-14/third-portfolio/blob/main/docs/screenshots/lucid_chart.png?raw=true)


## Data Model
A [Google Sheet](https://docs.google.com/spreadsheets/d/1NDjFUzCVzWmVwDyq-RfDqaUb0VehFTpRIXjt0rYkl9I/edit#gid=248498461) is used to store participants' data including their first and last names, piano level, musicianship level, solfa level and conducting level.

![Google Sheet](https://github.com/celine-14/third-portfolio/blob/main/docs/screenshots/google_sheet.png?raw=true)

### API Credentials
To allow access from the project to Google Sheets, credentials must be generated and provided.

## Testing

### User Input Testing
- Parameters: First Name, Last Name, Piano Level, Musicianship Level, Solfa Level and Conducting Level
  - An error message will be printed to the console if the following requirements are not met:
    - Has 6 input values
    - Values are separated by commas without space
    - First 2 inputs in alphabets and last 4 inputs in numbers
    - First and last names provided must be more than one letter
  - The terminal will repeatedly request for data until data is valid

### Validator Testing
- No errors were returned when passing through code validation [PEP8](https://pep8online.com/)


## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows:
  - In order for the project to run on Heroku, list of dependencies are installed into requirements.txt file
  - Clicked "create new app" button to create app and named "level_of_participants"
  - Selected "Europe" as the region and clicked "Create app"
  - Navigated to the Config vars section under the Settings tab in Heroku
  - Entered and added "CREDS" in the field for key and copied the entire creds.json file from the workspace into the value field
  - Entered and added "PORT" in the field for key and "8000" in the field for value
  - Navigated to the Buildpacks section and clicked "Add buildpack" button
  - Selected Python and saved changes
  - Selected node.js and saved changes
  - Navigated to the Deploy tab in Heroku
  - Selected GitHub as the deployment method
  - Confirmed connection to Github and searched "third-portfolio" as the Github repository name to connect
  - Manually deployed by using deploy branch option
  - Clicked the "Deploy" button
  - Terminal is up and running and no errors, indicating the successful deployment

### Live Link
[Participants Data Automation](https://level-of-participants.herokuapp.com/)

### Repository
[Github Repository](https://github.com/celine-14/third-portfolio)


## Credits

- The flowchart is generated from [Lucid](https://lucid.app/).