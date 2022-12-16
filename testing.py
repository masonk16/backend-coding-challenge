import json
import sqlite3


# Create connection to database
connection = sqlite3.connect('planning.db')
cursor = connection.cursor()

# Create database tables
cursor.execute('Create Table if not exists talent(id Text, name Text, grade Text, Unique(id))')
cursor.execute('Create Table if not exists client(id Text, name Text, industry Text, Unique(id))')
cursor.execute('Create Table if not exists skills(name Text, category Text, Unique(name))')
cursor.execute('Create table if not exists planning(id Integer, original_id Text,'
               'talent_id Text,'
               'booking_grade Text, operating_unit Text, office_city Text, office_postal_code Text,'
               'job_manager_id Text,'
               'total_hours Real, start_date Text, end_date Text,'
               'client_id Text,'
               'is_unassigned Integer,'
               'Foreign Key(talent_id) References talent(id),'
               'Foreign Key(client_id) References client(id),'
               'Foreign Key(job_manager_id) References talent(id),'
               'Unique(id, original_id))')

# Load planning.json file into data variable
data = json.load(open("planning.json"))

# Iterate through each row of data
for item in data:

    # Capture talent variables
    talent_id = item["talentId"]
    talent_name = item["talentName"]
    talent_grade = item["talentGrade"]

    # Create a tuple for talent variables
    talent = (talent_id, talent_name, talent_grade)

    # Insert values into talent table using the talent tuple
    cursor.execute('insert or ignore into talent values(?, ?, ?)', talent)

    client_id = item["clientId"]
    client_name = item["clientName"]
    industry = item["industry"]
    client = (client_id, client_name, industry)

    cursor.execute('insert or ignore into client values(?, ?, ?)', client)

    for index in range(len(item["requiredSkills"])):
        for skill in item["requiredSkills"][index]:
            rq_skill_name = item["requiredSkills"][index]["name"]
            rq_skill_category = item["requiredSkills"][index]["category"]
            required_skill = (rq_skill_name, rq_skill_category)

            cursor.execute('insert or ignore into skills values(?, ?)', required_skill)

    for index in range(len(item["optionalSkills"])):
        for skill in item["optionalSkills"][index]:
            op_skill_name = item["optionalSkills"][index]["name"]
            op_skill_category = item["optionalSkills"][index]["category"]
            optional_skill = (op_skill_name, op_skill_category)

            cursor.execute('insert or ignore into skills values(?, ?)', optional_skill)


    id = item["id"]
    original_id = item["originalId"]
    talent_id = item["talentId"]
    booking_grade = item["bookingGrade"]
    operating_unit = item["operatingUnit"]
    office_city = item["officeCity"]
    office_postal_code = item["officePostalCode"]
    job_manager_id = item["jobManagerId"]
    total_hours = item["totalHours"]
    start_date = item["startDate"]
    end_date = item["endDate"]
    client_id = item["clientId"]
    is_unassigned = item["isUnassigned"]
    # required_skills = required_skill
    # optional_skills = optional_skill

    planning = (id, original_id, talent_id, booking_grade, operating_unit, office_city,
                office_postal_code, job_manager_id, total_hours, start_date, end_date,
                client_id, is_unassigned)

    cursor.execute('insert or ignore into planning values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', planning)



    print(f'{talent_id} data inserted Succefully')
    print(f'{client_id} data inserted Succefully')



connection.commit()
connection.close()
