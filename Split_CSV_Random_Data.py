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
    "USERNAME", "EMAIL", "FIRSTNAME", "LASTNAME", "CITY",
    "STATE", "ZIPCODE"
]

product_header = [
    "PRODUCTID", "PRODUCTLINE", "CUSTOMER", "PURCHASE_DATE", "PURCHASE_METHOD", "PURCHASE_TIME"
]

customer_data = []
product_data = []
start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 12, 31)

# Generate customer data
for i in range(1001, 2002):
    username = fake.user_name()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    city = fake.city()
    state = fake.state_abbr()
    zip_code = fake.zipcode()

    customer_row = [
        username, email, first_name, last_name, city,
        state, zip_code
    ]
    customer_data.append(customer_row)

    # Generate product data for each customer
    product_id = i
    product_line = random.choice(product_lines)
    purchase_date = fake.date_between_dates(start_date, end_date).strftime('%Y-%m-%d')
    purchase_method = random.choice(["Online", "In-store"])
    purchase_time = fake.time()

    product_row = [
        product_id, product_line, username, purchase_date, purchase_method, purchase_time
    ]
    product_data.append(product_row)

# Write customer data to "customers.csv"
with open("customers.csv", "w", newline="") as customer_file:
    csvwriter = csv.writer(customer_file)
    csvwriter.writerow(customer_header)
    csvwriter.writerows(customer_data)

# Write product data to "products.csv"
with open("products.csv", "w", newline="") as product_file:
    csvwriter = csv.writer(product_file)
    csvwriter.writerow(product_header)
    csvwriter.writerows(product_data)
