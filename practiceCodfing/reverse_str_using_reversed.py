str="vicky"
str1="".join(reversed(str))
str2=""
reverse_str_iterables=list(reversed(str))
for char in reverse_str_iterables:
    str2=str2+char
print(str1)
print(str2)
str2=""
for i in range(len(str)-1,-1,-1):
    str2=str2+str[i]
print(str2)
