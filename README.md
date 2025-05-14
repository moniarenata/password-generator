# password-generator
Beginner friendly python project

Another easy project and I enjoyed this one!

This code helps the user generate a random password based on their preferences, like:

How long the password should be.

Whether it should include numbers, uppercase letters, and special characters (like !, @, #).

Step by step:

1. Importing the Goodies

import random
import string
We bring in two built-in Python libraries:

random: Lets us pick things randomly (great for shuffling and selecting characters).

string: Gives us ready-made lists like all lowercase letters, uppercase letters, numbers, etc.

2. Defining the Function

def generate_password():
I'm defining a function called generate_password() — think of it like a little machine that creates a password when called!

3. Getting User Preferences

length = int(input('Enter the desired password length: ').strip())
Asks the user how long the password should be.

input() gets the answer, .strip() tidies up any extra spaces, and int() turns it into a number.


include_number = input('Do you want to include numbers? Type: yes or no: ').strip().lower()
Asks if numbers should be included.

.lower() makes it lowercase so "Yes", "YES", or "yes" are all treated the same. Clever, right?

Same idea for uppercase and special characters:

include_uppercase = ...
include_special_character = ...
4. Checking for Minimum Length
if length < 4:
    print('Password must be at least 4 characters.')
    return
Passwords should be at least 4 characters to allow variety.

If the user enters less than 4, I give a message and stop the function early using return.

5. Building the Character Pool

lower = string.ascii_lowercase
This gives us: 'abcdefghijklmnopqrstuvwxyz'

Then, based on what the user said:

uppercase = string.ascii_uppercase if include_uppercase == 'yes' else ''
number = string.digits if include_number == 'yes' else ''
special_character = string.punctuation if include_special_character == 'yes' else ''
These lines use a ternary expression — a shortcut way to choose one of two options.

If the user said "yes", I use the appropriate set of characters; otherwise, I use an empty string (so nothing gets added).

Finally:

all_characters = lower + uppercase + special_character + number
I mix all allowed characters together into one big string from which I’ll choose random characters.

6. Making Sure Each Type is Included

required_character = []
This list will store at least one of each type the user said "yes" to.

Then:

if include_number == 'yes':
    required_character.append(random.choice(number))
This grabs a random character from the numbers and adds it to the list — same logic is used for uppercase and special characters.

7. Filling the Rest of the Password

remaining_length = length - len(required_character)
Figures out how many more characters we need to reach the desired password length.


password = required_character
Starts the password list with the characters I must include.

Then:


for _ in range(remaining_length):
    character = random.choice(all_characters)
    password.append(character)
Adds the remaining characters by randomly choosing from the pool.

The underscore _ is used when we don't care about the loop variable – just running the loop a certain number of times.

8. Shuffling the Password

random.shuffle(password)
Mixes up the characters so our required ones don’t all sit at the front. Makes it more secure and unpredictable!

9. Turning It Into a String

str_password = ''.join(password)
Joins all the characters in the list into one tidy string — this is the final password.

10. Returning and Printing

return str_password
The function gives back the final password.

password = generate_password()
print(password)
I call the function (notice the (), very important!).

Then I print the password so the user can see it.

Summary
The code is a lovely little password maker based on your own choices.

It uses some handy built-in tools (random, string).

It’s careful to include at least one of each selected type.

And it makes sure your password is random, secure, and properly mixed up!
