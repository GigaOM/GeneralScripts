import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

product_lines = [
    "Raspberry Pi", "Arduino", "Galaxy Tablet", "Bose Headphones",
    "Bose QuietComfort Earbuds II", "AirPods", "Oculus VR", "Apple Smartwatch",
    "JBL Charge 4 Speakers", "2022 Macbook Pro", "Harmony Microphone",
    "Apple Ipad", "AIMES Mens Watches", "ASUS Zenbook S 13",
    "Apple 2023 Mac Mini M2 Chip"
]

customer_header = [
    "userId", "email", "firstName", "lastName", "address_city",
    "address_state", "address_zip"
]

purchases_header = [
    "purchaseId", "productLine", "customerId", "purchaseDate", "purchaseMethod", "purchaseTime"
]

customer_data = []
purchases_data = []
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

# Generate customer data
for i in range(1001, 2002):
    userId = i
    email = fake.email()
    firstName = fake.first_name()
    lastName = fake.last_name()
    address_city = fake.city()
    address_state = fake.state_abbr()
    address_zip = fake.zipcode()

    customer_row = [
        userId, email, firstName, lastName, address_city,
        address_state, address_zip
    ]
    customer_data.append(customer_row)

    # Generate purchases data for each customer
    purchaseId = i
    productLine = random.choice(product_lines)
    customerId = userId
    purchaseDate = fake.date_between_dates(start_date, end_date).strftime('%Y-%m-%d')
    purchaseMethod = random.choice(["Online", "In-store"])
    purchaseTime = fake.time()

    purchases_row = [
        purchaseId, productLine, customerId, purchaseDate, purchaseMethod, purchaseTime
    ]
    purchases_data.append(purchases_row)

# Write customer data to "customers.csv"
with open("customers.csv", "w", newline="") as customer_file:
    csvwriter = csv.writer(customer_file)
    csvwriter.writerow(customer_header)
    csvwriter.writerows(customer_data)

# Write purchases data to "purchases.csv"
with open("purchases.csv", "w", newline="") as purchases_file:
    csvwriter = csv.writer(purchases_file)
    csvwriter.writerow(purchases_header)
    csvwriter.writerows(purchases_data)
