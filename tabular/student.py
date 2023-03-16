import csv
from faker import Faker
import random


def generate(num_students=1000, start_id=1000000000, end_id=2999999999, min_gpa=1.0, max_gpa=4.0,
             departments=['Computer Engineering', 'Electrical and Electronics Engineering', 'Mechanical Engineering',
                          'Civil Engineering', 'Chemical Engineering', 'Industrial Engineering', 'Food Engineering',
                          'Environmental Engineering', 'Architecture', 'Business Administration', 'Law', 'Psychology',
                          'Sociology',
                          'History', 'Literature', 'Physics', 'Mathematics', 'Chemistry', 'Biology',
                          'Agricultural Engineering',
                          'Maritime Studies', 'Tourism'],
             min_enrollment_year=2010, max_enrollment_year=2022, min_birth_year=1950, max_birth_year=2005,
             out_path='data/tabular/student.csv'):

    """
    Generate fake student data and save it to a CSV file.

    Args:
        num_students (int): The number of students to generate.
        start_id (int): The starting value for student IDs.
        end_id (int): The ending value for student IDs.
        min_gpa (float): The minimum GPA value to generate.
        max_gpa (float): The maximum GPA value to generate.
        departments (list): A list of department names to choose from when generating department values.
        min_enrollment_year (int): The minimum enrollment year to generate.
        max_enrollment_year (int): The maximum enrollment year to generate.
        min_birth_year (int): The minimum birth year to generate.
        max_birth_year (int): The maximum birth year to generate.
        out_path (str): The file name to save the generated student data to.
    """

    """
    faker = Faker('tr_TR')  # Set locale to Turkish
    departments=['Bilgisayar Mühendisliği', 'Elektrik Elektronik Mühendisliği', 'Makine Mühendisliği',
                                            'İnşaat Mühendisliği', 'Kimya Mühendisliği', 'Endüstri Mühendisliği', 'Gıda Mühendisliği',
                                            'Çevre Mühendisliği', 'Mimarlık', 'İşletme', 'Hukuk', 'Psikoloji', 'Sosyoloji',
                                            'Tarih', 'Edebiyat', 'Fizik', 'Matematik', 'Kimya', 'Biyoloji', 'Ziraat Mühendisliği',
                                            'Denizcilik', 'Turizm'],
    """

    field_names = ['Name', 'Surname', 'Student ID', 'GPA', 'Department', 'Enrollment Year', 'Date of Birth']
    students = set()  # Keep track of generated student IDs

    faker = Faker()

    with open(out_path, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()

        for i in range(num_students):
            name = faker.first_name()
            surname = faker.last_name()

            # Generate unique student ID within the given range
            student_id = None
            while student_id is None or student_id in students:
                student_id = random.randint(start_id, end_id)
            students.add(student_id)

            gpa = round(random.uniform(min_gpa, max_gpa), 2)
            department = faker.random_element(elements=departments)
            enrollment_year = random.randint(min_enrollment_year, max_enrollment_year)

            # Generate date of birth for students within the given range
            dob_year = random.randint(min_birth_year, max_birth_year)
            dob_month = random.randint(1, 12)
            dob_day = random.randint(1, 28)  # Assume all months have 28 days
            date_of_birth = f'{dob_year}-{dob_month:02d}-{dob_day:02d}'

            writer.writerow({'Name': name, 'Surname': surname, 'Student ID': student_id, 'GPA': gpa,
                             'Department': department, 'Enrollment Year': enrollment_year,
                             'Date of Birth': date_of_birth})
        print(f'Successfully generated {num_students} student records in {out_path}.')





