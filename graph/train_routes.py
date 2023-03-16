from faker import Faker
import csv
import random


def generate(num_stations=10, min_distance=10, max_distance=50, p_direct_connection=0.3, p_path_connection=0.4,
             out_path='data/graph/train_routes.csv'):
    fake = Faker()
    stations = [fake.city() for i in range(num_stations)]
    distances = {}

    # Generate the connections between stations
    for i in range(num_stations):
        for j in range(i+1, num_stations):
            if random.random() < p_direct_connection:
                # Create a direct connection between stations i and j
                distance = random.randint(min_distance, max_distance)
                distances[(stations[i], stations[j])] = distance
            elif random.random() < p_direct_connection + p_path_connection:
                # Create a path connection between stations i and j
                path_length = random.randint(2, 5)
                path_stations = random.sample(range(num_stations), path_length)
                distance = sum([random.randint(min_distance, max_distance) for k in range(path_length-1)])
                for k in range(path_length-1):
                    distances[(stations[path_stations[k]], stations[path_stations[k+1]])] = distance
            else:
                # No connection between stations i and j
                pass

    # Write the data to a CSV file
    with open(out_path, 'w', newline='') as file:
        field_names = ['Source', 'Destination', 'Distance']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for key, value in distances.items():
            if key[0] < key[1]:
                # Only write the connection once (e.g., (A,B), not (B,A))
                writer.writerow({'Source': key[0], 'Destination': key[1], 'Distance': value})
    print(f'Successfully generated train routes graph records for {num_stations} stations in {out_path}.')
