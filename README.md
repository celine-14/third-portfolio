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
  - Entered and added CREDS in the field for key and copied the entire creds.json file from the workspace into the value field
  - Entered and added PORT in the field for key and 8000 in the field for value
  - Navigated to the Buildpacks section and clicked "Add buildpack"
  - Selected Python and saved changes
  - Selected node.js and saved changes
  - Navigated to the Deploy tab
  - Selected GitHub as the deployment method
  - Confirmed connection to Github and searched "third-portfolio" as the Github repository name to connect
  - Manually deployed by using deploy branch option
  - Clicked the "Deploy" button
  - Terminal is up and running and no errors, indicating the successful deployment

The live link can be found here - https://celine-14.github.io/third-portfolio/

## Credits

- The flowchart is generated from [Lucid](https://lucid.app/).














![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome celine-14,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!