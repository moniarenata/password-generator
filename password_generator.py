import random
import string 

def generate_password():
    length = int(input('Enter the desired password length: ').strip()) #convert length into number 
    include_number = input('Do you want to include numbers? Type: yes or no: ').strip().lower()
    include_uppercase = input('Do you want to include uppercase letters? Type: yes or no: ').strip().lower()
    include_special_character = input('Do you want to include special characters? Type: yes or no: ').strip().lower()

    if length < 4: #if put 4 characters than at least all characters might be included
       print('Password must be at least 4 characters.')
       return
    
    lower = string.ascii_lowercase #gives all lowercase letters
    uppercase = string.ascii_uppercase if include_uppercase == 'yes' else '' 
    number = string.digits if include_number == 'yes' else '' 
    special_character = string.punctuation if include_special_character == 'yes' else '' 
    all_characters = lower + uppercase + special_character + number

    required_character = []
    if include_number == 'yes':
        required_character.append(random.choice(number))
    if include_uppercase == 'yes':
        required_character.append(random.choice(uppercase))
    if include_special_character == 'yes':
        required_character.append(random.choice(special_character))

    remaining_length = length - len(required_character)
    password = required_character

    for _ in range(remaining_length): #use anomymous variable (underscore) as no defined variable
        character = random.choice(all_characters)
        password.append(character)
    
    random.shuffle(password) #mix up the characters
    
    str_password = ''.join(password) #combines list of characters into a string
    return str_password

password = generate_password()
print(password)




