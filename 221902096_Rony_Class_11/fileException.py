try:
    file = open('notExist.txt','r')
    content = file.read()
except FileNotFoundError:
    print("The file does not exist.")
