from faker import Faker
import csv
import random
import os.path


def generate(num_rows=100, percent_dot=15, percent_dotdot=20, out_path='data/tabular/unix_paths.csv', valid_path_prefix='/home/nku/cmf/bm'):
    fake = Faker()

    while True:
        data = [valid_path_prefix]
        for i in range(num_rows):
            r_val = random.randint(1, 100)

            if r_val <= percent_dotdot:
                data.append('..')
            elif r_val <= percent_dot + percent_dotdot:
                data.append('.')
            else:
                data.append(fake.word())
        if test_data(data):
            break

    stack_data = data2stack(data)
    print("Full path: " + stack2path(stack_data))
    with open(out_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow([row])
    print(f'Successfully generated {num_rows} UNIX filepath records in {out_path}.')


def test_data(l):
    stack = [l[0]]
    for i in l[1:]:
        if i == '..':
            if len(stack) > 0:
                stack.pop()
            else:
                return False
        elif i == '.':
            pass
        else:
            stack.append(i)
    return True


def data2stack(l):
    stack = [l[0]]
    for i in l[1:]:
        if i == '..':
            stack.pop()
        elif i == '.':
            pass
        else:
            stack.append(i)
    return stack


def stack2path(l):
    fullpath = os.path.join(*l)
    return fullpath



