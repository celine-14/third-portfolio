## Table of Contents
* [Introduction](#introduction)
* [Testing](#testing)
    * [User Input Testing Testing](#user-input-testing)
    * [Validator Testing](#validator-testing)
* [Deployment](#deployment)
* [Credits](#credits)

# Participants Data Automation

## Introduction


![Lucid Chart](https://github.com/celine-14/third-portfolio/blob/main/docs/screenshots/lucid_chart.png?raw=true)

## Testing

### User Input Testing

### Validator Testing


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

The live link can be found here - https://celine-14.github.io/third-portfolio/

## Credits

- The flowchart is generated from [Lucid](https://lucid.app/).