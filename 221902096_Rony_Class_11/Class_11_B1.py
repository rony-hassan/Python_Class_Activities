import random

with open('/home/student_user/Desktop/example.txt','w') as file:
    for num in range(100):
        number = random.randint(1,100)
        file.write(f'{number} \n')
file.close()