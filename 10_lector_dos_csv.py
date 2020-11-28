# Utilizando modulo csv para lectura de archivos con extension csv
import csv

filename = 'employees.csv'

with open(filename, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # print(type(row))
        # print(row['Salary'])
        s = row.get('employee_id', 'N/A')
        n = row.get('Name')
        print(f'{n} earns {s}')
