import csv
import random
from faker import Faker
from faker.providers import person


def generate(num_events=100000, out_path='data/tabular/earthquake.csv'):
    fake = Faker('tr_TR')
    fake.add_provider(person)

    with open('tabular/tr_cities.csv', 'r') as f:
        cities = [city.strip() for city in f.readlines()]

    # Generate data for the CSV file
    data = []
    for i in range(num_events):
        date = fake.date_between(start_date='-10y', end_date='today')
        city = random.choice(cities)
        magnitude = round(random.uniform(2.0, 7.5), 1)
        depth = random.randint(1, 20) * 5
        duration = round(random.uniform(0.1, 30), 1)
        latitude = round(random.uniform(36.5, 42), 2)
        longitude = round(random.uniform(26, 45), 2)
        data.append([date, city, magnitude, depth, duration, latitude, longitude])

    # Write the data to a CSV file
    with open(out_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'City', 'Magnitude', 'Depth (km)', 'Duration (s)', 'Latitude', 'Longitude'])
        for row in data:
            writer.writerow(row)
    print(f'Successfully generated {num_events} earthquake records in {out_path}.')
