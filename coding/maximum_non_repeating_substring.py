st=input("Enter the string to be checked : ")

substr=""
for j in range(len(st)):
    strcopy=""
    for i in st:
        if not i in strcopy :
            strcopy=strcopy+i
            if len(strcopy)>len (substr):
                substr=strcopy
        else:
            break
print(substr)