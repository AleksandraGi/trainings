# source: https://www.youtube.com/watch?v=XCIBOl3FTKo&list=PLzMcBGfZo4-kBvY2DaxdSvoN_jGpzbw5V&index=3

import random
import string

def generate_password(minimum_length, numbers=True, special_characters=True):       # we want numbers and special characters
    letters = string.ascii_letters                  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 
    digits = string.digits                          # 0123456789 
    special_chars = string.punctuation              # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    characters = letters
    if numbers == True:
        characters += digits
    if special_characters == True:
        characters += special_chars

    password = ""
    has_number = False
    has_special = False
    meets_criteris = False
    # meets_criteris = has_number or has_special

    while not meets_criteris or len(password) < minimum_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special_chars:
            has_special = True
        
        meets_criteris = True
        if numbers:
            meets_criteris = has_number
        if special_characters:
            meets_criteris = meets_criteris and has_special

    return password

min_length = int(input("Enter the minimu  length: "))
has_number = input("Do you want to have numbers? (y/n)").lower() == "y"
has_special = input("Do you want to special characters? (y/n)").lower() == "y"


pwd = generate_password(min_length, has_number, has_special)
print(pwd)





# generate_password(10, False)            # minimum_length=10, numbers=False, special_characters=True