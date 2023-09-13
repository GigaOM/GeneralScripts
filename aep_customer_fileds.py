import csv
import json
import random
from faker import Faker

fake = Faker()

# List of email domains
email_domains = ["yahoo.com", "comcast.net", "gmail.com", "hotmail.com", "live.com"]

def generate_person_data():
    data = []

    for i in range(1001, 2002):
        person = {
            "personID": i,
            "personalEmail.address": fake.email(domain=random.choice(email_domains)),
            "person.name.firstName": fake.first_name(),
            "person.name.lastName": fake.last_name(),
            "homeAddress.city": fake.city(),
            "homeAddress.state": fake.state_abbr(),
            "mailingAddress.postalCode": fake.zipcode(),
            "_acpstardust.WorkaroundTrue": True  # Set the last column to True
        }
        data.append(person)

    return data

def convert_and_save_to_csv(data, csv_filename):
    # Extract headers from the first data entry
    headers = data[0].keys()

    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
        csv_writer.writeheader()  # Write the header row
        csv_writer.writerows(data)  # Write the data rows

def main():
    person_data = generate_person_data()
    person_json_filename = "aep_person_data.json"
    person_csv_filename = "aep_person_data.csv"

    # Save the JSON data for persons
    with open(person_json_filename, "w") as person_json_file:
        json.dump(person_data, person_json_file, indent=4)

    # Convert and save person data to CSV
    convert_and_save_to_csv(person_data, person_csv_filename)
    print(f"Generated person data saved to {person_json_filename}")
    print(f"Converted person data saved to {person_csv_filename}")

if __name__ == "__main__":
    main()
