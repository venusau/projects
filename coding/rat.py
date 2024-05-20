r = int(input("Enter the of rats in a area :"))
if r> 0 :
    unit=int(input("Enter the amount of food each rat needs : "))
    if unit >0:
        n=int(input("Enter the length of the array : "))
        l=[]
        for i in range(n):
            l.append(int(input(f"Enter the amount of food in the house number {i+1}: ")))
        unit=unit*r
        if len(l) !=0:
            sum=0
            c=0
            for i in l:
                if sum <unit:
                    sum=sum+i
                    c=c+1
                else:
                    print(c) 
                    exit(0)
                
            if not sum>=unit :
                print(0)
        else: 
            print(-1)
    else:
        print("The unit must be greater than zero !")
else:
    print("The number of rats must be greater than zero !")