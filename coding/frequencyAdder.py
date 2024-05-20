
def countAndSay(n):
    if n == 1:
        return "1"
    
    prev_seq = "1"
    for _ in range(n - 1):
        result = ""
        count = 1
        for i in range(1, len(prev_seq)):
            if prev_seq[i] == prev_seq[i - 1]:
                count += 1
            else:
                result += str(count) + prev_seq[i - 1]
                count = 1
        result += str(count) + prev_seq[-1]
        prev_seq = result
    
    return prev_seq

n = int(input("Enter the value of n: "))
result = countAndSay(n)
print(f"The count-and-say sequence for n = {n} is: {result}")
