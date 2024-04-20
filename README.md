
![Image source Logo](/images/subshop.png)

Program live link: The app has succesfully been deployed and can be viewed on <a href="https://subshop-ceb451619694.herokuapp.com/" target="_blank">Heroku</a>

Accompanying Spreadsheet: [Google Sheets](https://docs.google.com/spreadsheets/d/18cGqHrZWaSvZ3V6-gzhmV5peyCnDMR-ogmTHfpfYHII/edit#gid=0)

*Right/Middle click to open in a new tab*

---

## Contents
[Overview](#overview)
* Usage Scenario

[Google Sheets integration](#google-sheets-integration)

[Planning](#planning)

[UX](#ux)

[User Stories](#user-stories)

[Design Process](#design-process)
* API Integration
* Main Function

[Features](#features)
* Display Program Introduction

[Testing](#testing)
* User Stories Testing

[Validation and Version Control](#validation-and-version-control)

[Bugs and Known issues](#bugs-and-known-issues)
* Bugs
* Known Issues

[Project Outcome Summary](#project-outcome-summary)

[Deployment](#deployment)

[Cloning and Forking](#cloning-and-forking)

[Technologies Used](#technologies-used)

[Future Ideas](#future-ideas)

[Credits](#credits)

[Acknowledgement](#acknowledgement)

---

## Overview

<a href="https://subshop-ceb451619694.herokuapp.com/" target="_blank">Welcome to the Subshop,</a>

This app is a data-driven Python program which is integrated with Google Sheets. The aim is to boost efficiency in the store for daily tasks, by helping keep track of what is needed for the next day.

#### Usage Scenario

The planning for what is needed on any given day is done the night before. The store currently makes a fresh batch of stock at the minimum stock required level.

For efficieny and to reduce food waste, this tool will calculate the true predicted value for how much stock the user will need and it will help the store manage what products are selling well.


## Google Sheets integration
[Please refer to the program's accompanying spreadsheet](https://docs.google.com/spreadsheets/d/18cGqHrZWaSvZ3V6-gzhmV5peyCnDMR-ogmTHfpfYHII/edit#gid=0)

Stock plans are created by a manager each day. The Google Sheet serves to replicate 
this database. In the deployed program, the sheet uses "real-world" figures from 
the stores sales data. Figures are updated daily. In real-world deployment, 
the app would me modified to take sales data directly from the register to remove a 
stage of human input, creating an ongoing communication between the database and program.
However, this scenario has been simulated so a user can update at the end of the day.

The program refers to two sheets. An item and stock sheet which are updated depending on user inputs.


<details>
<summary>Items reference sheet</summary>

![items](/images/items.png)
</details>

<details>
<summary>Stock reference sheet</summary>

![stock](/images/stock.png)
</details>

It is important to note that the naming conventions in the worksheets must be followed, as the app relies on worksheet data and user inputs to function.

The item reference sheet contains data on each individual item for the program to address. Data such as the item name are integral to the program flow.

The items and stock sheet work on a wipe and reload basis. After a user updates their figures, the previous data will be overwritten. 

## Planning
Creating the program involved writing down on paper the columns in the sheet and how the main function would reference and update these.

Initially in planning, the tool was only going to accept new or update items. During the building phase, the decision to allow for deleting rows was also added.

## UX
The program flow is clear and asks the user for minimal information with minimal text. The program is designed to be simple to use and easy for the user to update the inventory.

## User Stories
### User goals:

* Add a new item to the subshop
* Update an item from the subshop
* Delete an item from the subshop

## Design Process
### API Integration:
Before writing any functions, I first had to setup any dependencies and test the API for Google Sheets integration. This required the libraries for gspread and google-auth.

Tests were made to confirm API function by printing vars made by gspread methods. See commit c60a69c (3rd commit of project)

After API integration was confirmed. I proceeded to test functions were able to extract the required data from the Google Sheet.
At this point I decided I also needed to add "*import pandas as pd* and *import numpy as np*"

### Main Function:

 My initial goal for this project was to have 2 sheets and 2 options. Entering a new item and updating an existing item. As I got into the programs development I decided to add a delete option, to remove entries from the database.
 
 When I was initially testing each function in the project, I was testing for correct values only. After completing the initial build, I realised that I also needed to add in validations and loops for when a user enters in blank spaces or incorrect values.


<details>
<summary>Flow Chart</summary>

![flowchart](/images/flowchart.png)
</details>

## Features
This section will cover how and why each step in the program is included. The below will have screenshots in chronological order of output. Starting with the correct inputs for: new, update, delete. The validation messages will be shown in the validation testing section, found in the TESTING.md.

### Display Program Introduction

On program start, the user will be presented with the option to add a new item, update or delete an existing one. 

![intro](/images/intro.png)

#### Add a new item:
The below screen shot is the options provided to the user to add a new item. In order, they will be asked to input:
* Product Name
* Minimum Stock Required
* Time taken to cook an item
* The cost to prepare the item
* How much the item sells for

Output: These inputs will be appended to the "items" tab and the "stock" tab in the worksheet.

![new inputs](/images/new-inputs.png)

#### Update an item
The below screen shot is the options provided to the user to update an item. In order, they will be asked to input:
* Product Name
* How many items sold
* Minimum Stock Required
* Time taken to cook an item
* The cost to prepare the item
* How much the item sells for

![update inputs](/images/update-inputs.png)

Output: The items row will be updated in the "stock" tab

#### Delete an item
The below screen shot is the options provided to the user to update an item. In order, they will be asked to input:
* Product Name

Output: This will delete the row requested, from both the "stock" and "items" tabs.

![delete inputs](/images/delete-inputs.png)

#### Final output

Regardless of which options are chosen. The user will see the current status of both sheets, as seen below:

#### Items table:
![Items Table](/images/output-table1.png)

#### Stock table:
![Stock Table](/images/output-table2.png)




## Testing
All testing can be found in the [Testing file](TESTING.md)


## Validation and Version Control

By following best practice guidelines throughout development, my code has fully
passed through the [CI Python Linter](https://pep8ci.herokuapp.com/) with no errors found.
This can be verified by pasting the 'run.py' file through the CI Python Linter link:

![PEP8 Validator](/images/pep8-validator.png)

## Bugs and Known issues
### Bugs
Testing was thorough during development as many bugs came up. Issues as follows:
* Columns being overwritten instead of rows being updated
* Data types not matching so the code would not run
* Incorrect user inputs breaking the code
* Blank spaces could be used as a user input

*All issues that were found and fixed before final deployment.*

### Known issues
There are no issues that have been found and are unresolved.

## Project Outcome Summary
This project was built with logical steps in mind of how a company could manage their stock, by consdering user stories at a basic level. 
Each function was designed and built with the user in mind and how they could manipulate their data sets.

Errors are managed throughout the program through validations and while loops.
Where inputs pass the validation, they are moved onto the next stage of inputs.
The program has not been found to crash as a result of user input.
Exception handling is implemented to cover all of the opportunities for user input error.
In all instances, the error and solution is communicated to the user.

Throughout the code, every effort has been made to implement efficient, well documented code.
I utilised the main() function which contained all code. This was particularly helpful when testing code-breaks.

## Deployment
The program was hosted on Heroku due to its ability to handle dynamic content.
I integrated my code with the CI Python template to create the 'mock-terminal' feature seen on the live site.
This feature enables users to engage directly with the code, similar to executing the run.py file in an IDE.

Deploying this project involved multiple steps, which are more intricate compared to deploying from GitHub Pages.
By adhering to these steps sequentially, you can deploy the application to the web:

1. Generate a list of requirements for Heroku. These are the dependencies used in the Gitpod VS Code workspace.
To generate, ensure there is a requirements.txt file in your project root.
Then enter pip3 freeze > requirements.txt into your terminal.
This will build a list of dependencies that Heroku will use to build the project.

2. Make sure to save, commit, and push all files to ensure that Heroku can utilise them later on.

3. Login or Sign up 

4. Ensure that your account is set up correctly and your Eco Dynos plan is active in Heroku

5. Select 'Create new app' from your Heroku Dashboard.

6. Create a unique name for your app and select your region. Select 'Create app'.

7. Select 'Reveal Config Vars'. Here you will add KEY:VALUE pairs to adjust app behaviour.
Remember that there is an untracked file in the project containing credentials for API function.
    1. 'KEY' = CREDS
    2. 'VALUE' = Paste from your CREDS.json file.
    3. Select 'Add'
    4. 'KEY' = PORT
    5. 'VALUE' = 8000
    6. Select 'Add'

8. Select 'Add buildpack'. Add the following buildpack in order.
These can be re-ordered by drag-and-drop if needed.
    1. heroku/python
    2. heroku/nodejs

9. In the "Deploy" tab. Under 'Deployment method', select 'GitHub' and proceed to follow the prompts to establish a connection.

10. When the correct repo is located, select 'Connect'.

11. Finally, under "Manual deploy", select the correct branch and click 'Deploy Branch'.
A build log will begin running. A link will be provided to the site after this process.

12. Click the "View" button to view the deployed app.


## Cloning and Forking
### How to Clone

To clone the repository:

1. Login (or signup) to Github.
2. Go to my repository for the project, [gauravjagpal/subshop](https://github.com/gauravjagpal/subshop).
3. Click on the Green code button, choose whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Launch the terminal within your code editor and set the current working directory to the desired location for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

### How to Fork

To fork the repository:

1. Login (or signup) to Github.
2. Go to my repository for the project, [gauravjagpal/subshop](https://github.com/gauravjagpal/subshop).
3. Click the Fork button in the top right corner.


## Technologies Used
[Code Institute Python Template](https://github.com/Code-Institute-Org/python-essentials-template)
\- This formed the foundation for the project, which integrated with the CI mock
terminal that the project is presented in.
IDE: VS Code in [Gitpod](https://www.gitpod.io/)

[Google Account](https://www.google.com/account/about/?hl=en-US) Services for
 API integration:

- Google Cloud
- Google Sheets
- Google Drive

Deployment Platform: [Heroku](https://www.heroku.com/)

Flowchart Editor: [draw.io](https://app.diagrams.net/)

Language: Python 3.8.11

Python Libraries - latest versions imported and installed from terminal:

- [gspread](https://docs.gspread.org/en/latest/) - The basis of the Google Sheets
  integration

- [google-auth.Credentials](https://google-auth.readthedocs.io/en/stable/reference/google.auth.credentials.html)
  \- For authorizing gspread scope in the Google Sheets API

- [pandas](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) - for its
  [list flattening method](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html)

- [numpy](https://numpy.org/doc/stable/index.html) - for working with data sets

## Future Ideas

Future ideas I have had for this project are as follows:
1. Create user accounts so you can see the user who last edited it
2. Create an sales tab so each sales data is appended for storage purposes
3. Add a feature to print out what the user input and then ask for confirmation
4. In the initial design there was an idea to loop back to the start of the program. This was removed at a latter stage and would be reimplemented with full functionality.

## Credits
Sites used:
1. [Google Sheets - subshop dataset](https://docs.google.com/spreadsheets/d/18cGqHrZWaSvZ3V6-gzhmV5peyCnDMR-ogmTHfpfYHII/edit#gid=480423322)
2. [CI Python Linter](https://pep8ci.herokuapp.com/)
3. [Image for README](https://www.unileverfoodsolutions.com.au/recipe/baguette-with-roasted-salmon-and-lime-chilli-mayonnaise-R0022179.htm)

## Acknowledgement
Stack-overflow for helping me figure out solutions when I was hitting a block

And a massive thank you to my mentor, Jubril, for reviewing and providing feedback on my code