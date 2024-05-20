class A:

    def check_repetition(a):
        seen = set()
        for char in a:
            if char in seen:
                return False
            seen.add(char)
        return True

    @staticmethod
    def main():
        a = input("Enter the string input: ")
        l = []
        for i in range(len(a)):
            for j in range(len(a), i, -1):
                subs = a[i:j]
                if A.check_repetition(subs):
                    l.append(subs)
        l.sort(key=len, reverse=True)  # Sort by length in descending order
        print(l[0])

if __name__ == '__main__':
    A.main()
