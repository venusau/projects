"""Input:   {1, 0}
            {0, 0}

Output:        {1, 1}
               {1, 0}

    Input:      {0, 0, 0}
                {0, 0, 1}

Output:         {0, 0, 1}
                {1, 1, 1}
 

    Input:      {1, 0, 0, 1}
                {0, 0, 1, 0}
                {0, 0, 0, 0}


Output:         {1, 1, 1, 1}
                {1, 1, 1, 1}
                {1, 0, 1, 1}"""

l=[[]]
n=int(input("Enter the length of the list : "))

for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input(f"Enter the element at the index of ({i})({j}): ")))
        if not (row[j]==1 or row[j]==0):
            print("You can only enter 0 or 1:")
            exit()
    l.append(row)

print("Input : ")
for row in l:
    c=len(row)
    for element in row:
        if c>1:
            print(element, end=",")
            c=c-1
        else:
            print(element,end="")
    print()

choice=input("Enter Y for proceding or N for exiting choice (y/N): ")

choice=choice.upper()

if not choice=='Y':
    print("Ok Fine !\nGood luck !")
    exit()
else:
    def make_one(l, row_index, column_index):
        for i in range(len(l)):
            row=l[i]
            for j in range(len(row)):
                if i!=row_index:
                    l[i][column_index]=1
                else:
                    l[row_index][j]=1
    temp_list = []  # Initialize an empty list

    for row_index in range(len(l)):
        row = l[row_index]
        for column_index in range(len(row)):
            if l[row_index][column_index] == 1:
                temp_list.append([row_index, column_index])
                # make_one(l, row_index, column_index)
    print(temp_list)

    for row in temp_list:
        make_one(l,row[0], row[1])

    print("Output : ")
    for row in l:
        c=len(row)
        for element in row:
            if c>1:
                print(element, end=",")
                c=c-1
            else:
                print(element,end="")
        print()

    # choice=input("Do you want to save the output in a file (y/N): ")

    # choice=choice.upper()

    # if not choice=='Y':
        # print("Ok Fine !\nGood luck !")
    #     exit()
    else:
    #     file_name=input("Enter the file name : ")

    #     file_name=file_name+".txt"

    #     file=open(file_name,"w")

    #     for row in l:
    #         c=len(row)

    #         for element in row:
    #             if c>1:
    #                 file.write(str(element)+",")
    #                 c=c-1
    #             else:
    #                 file.write(str(element))
    #         file.write("\n")

    #     file.close()

    #     print("File saved successfully !")

    #     print("Thank you for using this program !")

    #     exit()