# Final Fantasy XIV Character Data Retrieval Script


This script allows you to retrieve various information about a character in Final Fantasy XIV using the XIVAPI. It fetches data such as character attributes, class/job information, equipment, achievements, mounts, and minions.

## Features

    Fetches character information from the XIVAPI based on the character name and server.
    Retrieves the character's basic details, including name, ID, race, and active class/job.
    Extracts additional attributes like guardian deity, nameday, town/city, grand company, free company, and title.
    Retrieves class/job information, including the active class/job, level, and icon. It also provides a list of all class/jobs the character has.
    Retrieves information about the character's equipped main-hand weapon and other gear slots.
    Retrieves achievement details, including the total achievement points and a list of achievements earned by the character.
    Retrieves the list of mounts and minions owned by the character.

## Requirements

    Python 3.x
    requests library (can be installed using pip install requests)

## Usage

    Install the required dependencies by running pip install -r requirements.txt.
    Replace 'YOUR_API_KEY' in the script with your XIVAPI key. If you don't have an API key, you can register and obtain one from the XIVAPI website.
    Modify the script to specify the character name and server for which you want to retrieve the data.
    Run the script using python script.py.
    The script will fetch the character data from the XIVAPI and display it on the console.

Please note that the availability and accuracy of certain data fields may depend on the character's subscription status and recent activity in the game.

Feel free to customize the script to suit your specific requirements and integrate the retrieved data into your Tableau dashboard or any other application.
License

## This script is provided under the MIT License.

![image](https://user-images.githubusercontent.com/95504135/236994624-48b52021-ef1d-48dc-8483-04aa63f5143b.png)

*"Thanks for checking out this repo, kupo!"*
