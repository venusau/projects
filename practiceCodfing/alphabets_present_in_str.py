st = input("Enter the string to be checked: ").upper()
last_index = -1

for i in range(65, 91):  # Iterate over ASCII values of uppercase English alphabets
    char = chr(i)
    if char in st:
        index = st.index(char)
        if index < last_index:
            print("Not all the alphabets are in correct order.")
            exit(0)
        last_index = index
    else:
        print("Not all the alphabets are present.")
        exit(0)

print("All the alphabets are in correct order!")
