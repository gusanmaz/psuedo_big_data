import csv
from faker import Faker
import random
import uuid


def generate(num_accounts=1000, output_file='data/tabular/bank.csv'):
    """
    Generates fake bank account data for customers in CSV format using Python Faker library.

    Args:
        num_accounts (int): The number of bank account records to generate. Default is 1000.
        output_file (str): The name of the CSV file to output the generated data to. Default is 'fake_bank_data.csv'.
    """
    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=[
            'Customer ID',
            'SSN Number',
            'Customer Name',
            'Customer Surname',
            'Email',
            'Address Street',
            'Address State',
            'Address City',
            'Address Country',
            'Address Zipcode',
            'Phone Number',
            'Account Type',
            'Account Balance',
            'Customer Age',
            'Date of Account Opening',
            'Customer Gender',
            'Customer Occupation',
            'Customer Education Level'
        ])
        writer.writeheader()

        faker = Faker()

        for i in range(num_accounts):
            customer_id = str(uuid.uuid4())
            ssn_number = faker.ssn()

            customer_name = faker.first_name()
            customer_surname = faker.last_name()
            email = faker.email()
            address_street = faker.street_address()
            address_state = faker.state()
            address_city = faker.city()
            address_country = "USA"
            address_zipcode = faker.postcode()
            phone_number = faker.phone_number()
            account_type = faker.random_element(elements=('Dollar', 'TL', 'Euro'))
            account_balance = round(random.uniform(0.0, 100000.0), 2)
            customer_age = faker.random_int(min=18, max=80)
            date_of_account_opening = faker.date_this_century(before_today=True, after_today=False).strftime('%Y-%m-%d')
            customer_gender = faker.random_element(elements=('Male', 'Female'))
            customer_occupation = faker.job()
            customer_education_level = faker.random_element(elements=('High School', 'Bachelor', 'Master', 'PhD'))

            writer.writerow({
                'Customer ID': customer_id,
                'SSN Number': ssn_number,
                'Customer Name': customer_name,
                'Customer Surname': customer_surname,
                'Email': email,
                'Address Street': address_street,
                'Address State': address_state,
                'Address City': address_city,
                'Address Country': address_country,
                'Address Zipcode': address_zipcode,
                'Phone Number': phone_number,
                'Account Type': account_type,
                'Account Balance': account_balance,
                'Customer Age': customer_age,
                'Date of Account Opening': date_of_account_opening,
                'Customer Gender': customer_gender,
                'Customer Occupation': customer_occupation,
                'Customer Education Level': customer_education_level
            })

    print(f'Successfully generated {num_accounts} fake bank account records in {output_file}.')