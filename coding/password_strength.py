import re
import random
import string

def is_strong_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False
    
    # Check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False
    
    # Check if the password contains at least one special character
    if not re.search(r'[^A-Za-z0-9]', password):
        return False
    
    return True

def generate_strong_password(username, password):
    # Check if the password is already strong
    if is_strong_password(password):
        return password
    
    # Modify the password to make it strong
    modified_password = ''.join(random.choices(string.ascii_uppercase, k=1))  # Random uppercase letter
    modified_password += ''.join(random.choices(string.ascii_lowercase, k=1))  # Random lowercase letter
    modified_password += ''.join(random.choices(string.digits, k=1))  # Random digit
    modified_password += ''.join(random.choices(string.punctuation, k=1))  # Random special character
    modified_password += password  # Add the original password
    
    return modified_password

# Example usage
username = input("Enter your username: ")
password = input("Enter your password: ")

if not is_strong_password(password):
    print("Password is not strong. Generating a strong password...")
    password = generate_strong_password(username, password)
    print("Your new strong password is:", password)
else:
    print("Password is strong.")
