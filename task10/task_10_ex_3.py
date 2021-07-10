"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""
import csv
from collections import namedtuple

student = namedtuple("Student", ("name", "age", "mark"))


def get_top_performers(file_path: str,
                       number_of_top_students: int = 5) -> list:
    """Receives file path and returns names of top performer students."""
    with open(file_path, 'r', newline='') as file:
        csv_reader = csv.reader(file, delimiter=",")
        headers = next(csv_reader)
        students = [student(*data) for data in csv_reader]
    sorted_students = sorted(students, key=lambda x: float(x.mark),
                             reverse=True)
    students_name = [student_.name for student_ in sorted_students]
    return students_name[:number_of_top_students]


def write_students_age_desc(file_path: str, output_file_path: str) -> None:
    """receives the file path with students info and writes CSV student
    information to the new file in descending order of age."""
    with open(file_path, 'r', newline='') as input_file, \
            open(output_file_path, 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file, delimiter=",")
        csv_writer = csv.writer(output_file, delimiter=",")
        csv_writer.writerow(next(csv_reader))

        students = [student(*data) for data in csv_reader]
        sorted_students = sorted(students, key=lambda x: int(x.age),
                                 reverse=True)
        for data in sorted_students:
            csv_writer.writerow(data)
