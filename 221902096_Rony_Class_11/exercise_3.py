import csv

def findCourseAndStudentInfo(reader):
    CourseStudentInfo = dict()
    for row in reader:
        if row['Title'] in CourseStudentInfo:
            CourseStudentInfo[row['Student Name']].append(row['Student Id'])
        else:
            CourseStudentInfo[row['Student Name']] = [row['Student Id']]
    print(CourseStudentInfo)

try:
    with open('/home/student_user/Downloads/SampleFile.csv') as file:
        reader = csv.DictReader(file)

        findCourseAndStudentInfo(reader)

except FileNotFoundError:
    print('File does not exist')
finally:
    file.close()