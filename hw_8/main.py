import zipfile
import json
import csv
import os


PATH_TO_INITIAL_ZIP = 'students.zip'
PATH_TO_NEW_ZIP = 'new_students.zip'
PATH_TO_JSON = 'students.json'
PATH_TO_CSV = 'students.csv'


def extract_zip():
    with zipfile.ZipFile(PATH_TO_INITIAL_ZIP, 'r') as zip_ref:
        zip_ref.extract(PATH_TO_JSON, '.')


def get_students_from_json():
    with open(PATH_TO_JSON, 'r') as json_file:
        students_data = json.load(json_file)[0]
    return students_data


def write_students_to_csv(students):
    with open(PATH_TO_CSV, 'w', newline='') as csv_file:
        fieldnames = ['firstname', 'lastname']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        for student in students:
            writer.writerow({'firstname': student['firstname'], 'lastname': student['lastname']})


def zip_csv():
    with zipfile.ZipFile(PATH_TO_NEW_ZIP, 'w') as zip_ref:
        zip_ref.write(PATH_TO_CSV)


def remove_old_files():
    os.remove(PATH_TO_JSON)
    os.remove(PATH_TO_CSV)


def main():
    extract_zip()
    students = get_students_from_json()
    write_students_to_csv(students=students)
    zip_csv()
    remove_old_files()


if __name__ == "__main__":
    main()
