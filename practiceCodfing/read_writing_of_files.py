with open('tst.txt', 'r+') as file:

    data = file.read()
    print(data)
    file.write('\nwriting from the python source code /n')
    data=file.read()
    print(data)
# File is automatically closed when the block exits, even if an exception occurs
