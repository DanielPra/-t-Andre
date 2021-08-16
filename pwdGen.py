# Write a password generator in Python. Ask the user how strong they want their
# password to be. For weak passwords,pick a word or two from a list.
import random
password_list = []
basic_pwds = ["Alpha", "Omega", "Bob"]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Ask user for desired length of password
desired_len = int(input("How many characters do you want in your password?: "))

# Generate random string of choosen length
def random_func():
    b = 0
    while b < desired_len:
        ran_num = random.randint(0, 25)
        password_list.append(letters[ran_num])
        b = b + 1

# Convert list to string
def listToString(s):
    my_string = " "
    joined_string = (my_string.join(s))
    joined_string = joined_string.replace(" ", "") # Drop whitespaces
    print(f"Your password is: {joined_string}")

# Choose if we need an easy or hard pwd.
if desired_len < 5:
    num = random.randint(-1,2)
    short_pwd = basic_pwds[num]
    print(f"Your password is {short_pwd}")
else:
    random_func()
    listToString(password_list)

