import csv
from faker import Faker
import random


def generate(num_accounts=10, max_following=5, out_path='data/graph/social_media.csv'):
    fake = Faker()

    # Generate the data for the CSV file
    data = []
    for i in range(num_accounts):
        account_handle = fake.user_name()
        account_name = fake.first_name()
        account_surname = fake.last_name()
        account_age = fake.random_int(min=18, max=80)
        account_email = fake.email(domain='example.com')
        num_posts = fake.random_int(min=0, max=1000)
        following = random.sample(range(num_accounts), random.randint(0, max_following))
        data.append({
            'Handle': account_handle,
            'Name': account_name,
            'Surname': account_surname,
            'Age': account_age,
            'Email': account_email,
            'Total Post Count': num_posts,
            'Following': following,
        })

    # Write the data to a CSV file
    with open(out_path, 'w', newline='', encoding='utf-8') as file:
        field_names = ['Handle', 'Name', 'Surname', 'Age', 'Email', 'Total Post Count', 'Following']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for row in data:
            for user in row['Following']:
                csv_row = row.copy()
                csv_row['Following'] = user
                writer.writerow(csv_row)
        print(f'Successfully generated  social media graph records for {num_accounts} in {out_path}.')

