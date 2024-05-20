import hashlib

def sha256_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

def main():
    text = input("Enter the string to hash: ")
    hash_choice = input("Choose hashing algorithm:\n1. SHA256\n2. MD5\nEnter your choice: ")

    if hash_choice == '1':
        hashed_text = sha256_hash(text)
        print("SHA256 Hash:", hashed_text)
    elif hash_choice == '2':
        hashed_text = md5_hash(text)
        print("MD5 Hash:", hashed_text)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
