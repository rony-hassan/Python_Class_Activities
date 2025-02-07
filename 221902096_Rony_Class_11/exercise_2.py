import csv

try:
    with open('/home/student_user/Downloads/SampleFile.csv') as file:
        reader = csv.DictReader(file)

        lst = list()
        for row in reader:
            print(row)
            if row['Program'].startswith('EEE'):
                lst.append(row)
        print(len(lst))
except FileNotFoundError:
    print('File does not exist')
finally:
    file.close()