mydict = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
}
keys = mydict.keys()
values = mydict.values()
keys_list=list(keys)
values_list=list(values)
print(keys_list)
print(values_list)
#print("Keys:", keys)
#print("Values:", values)
def combination(numbers_list):
    l=[],k=0
    while k!=len(numbers_list):
        str=""
        k=k+1
        for i in numbers_list:
        
            str=str+keys_list[i-1]
        print(str)
        


def passing_ways(n):
    t=n
    l=[]
    while t!=0:
        l.append(t%10)
        t=t//10
    l.reverse()
    combination(l)
    

  
n=int(input("Enter the number to decode ways : \n "))
passing_ways(n)