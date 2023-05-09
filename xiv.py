import requests

# Define the API endpoint URL
api_url = 'https://xivapi.com/character/search'

# Define your API key if required (check the XIVAPI documentation for details)
api_key = 'API_KEY'

# Define the character name you want to search for
character_name = 'Rael Eruyt'

# Define the server or world the character belongs to
server_name = 'Midgardsormr'

# Prepare the request parameters
params = {
    'name': character_name,
    'server': server_name,
    'key': api_key
}

# Send the API request
response = requests.get(api_url, params=params)

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Check if any character data is found
    if data['Pagination']['ResultsTotal'] > 0:
        # Extract the first character from the search results
        character = data['Results'][0]

        # Extract relevant character data with fallback values
        character_name = character['Name']
        character_id = character['ID']
        character_race = character.get('Race', 'Unknown')
        character_job = character.get('ClassJob', 'Unknown')

        # Character Attributes
        guardian_deity = character.get('GuardianDeity', 'Unknown')
        nameday = character.get('Nameday', 'Unknown')
        town = character.get('Town', 'Unknown')
        grand_company = character['GrandCompany']['Name'] if 'GrandCompany' in character else 'Unknown'
        free_company = character['FreeCompany']['Name'] if 'FreeCompany' in character else 'Unknown'
        title = character['Title']['Name'] if 'Title' in character else 'Unknown'

        # Class/Job Information
        active_job = character['ActiveClassJob']['Job']['Name'] if 'ActiveClassJob' in character else 'Unknown'
        active_job_level = character['ActiveClassJob']['Level'] if 'ActiveClassJob' in character else 'Unknown'
        active_job_icon = character['ActiveClassJob']['Job']['Icon'] if 'ActiveClassJob' in character else None
        class_jobs = character.get('ClassJobs', [])

        # Equipment
        main_hand_weapon = character['Character']['GearSet']['MainHand']['Name'] if 'Character' in character and 'GearSet' in character['Character'] and 'MainHand' in character['Character']['GearSet'] else 'Unknown'
        gear_slots = character['Character']['GearSet']['Gear'] if 'Character' in character and 'GearSet' in character['Character'] else []

        # Achievements
        achievement_points = character['AchievementPoints'] if 'AchievementPoints' in character else 0
        achievements = character.get('Achievements', [])

        # Mounts
        mounts = character['Mounts']['Mounts'] if 'Mounts' in character else []

        # Minions
        minions = character['Minions']['Minions'] if 'Minions' in character else []

        # Display the extracted data
        print('Character Name:', character_name)
        print('Character ID:', character_id)
        print('Character Race:', character_race)
        print('Character Job:', character_job)
        print('Guardian Deity:', guardian_deity)
        print('Nameday:', nameday)
        print('Town:', town)
        print('Grand Company:', grand_company)
        print('Free Company:', free_company)
        print('Title:', title)