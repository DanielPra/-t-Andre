#!/usr/bin/env python

""" DT179G - LAB ASSIGNMENT 2
You find the description for the assignment in Moodle, where each detail regarding requirements
are stated. Below you find the inherent code, some of which fully defined. You add implementation
for those functions which are needed:

 - authenticate_user(..)
 - format_username(..)
 - decrypt_password(..)
"""

import argparse
import sys

__version__ = '1.0'
__desc__ = "A simple script used to authenticate spies!"


def authenticate_user(credentials: str) -> bool: # Part 1. Just split pwd and username
    """Procedure for validating user credentials. The main responsibility of the
    function is to verify whether provided credentials conforms to any of the
    existing key / value pairs in dictionary agents"""

    agents = {  # Expected credentials. MAY NOT BE MODIFIED!!
        'Chevy_Chase': 'i0J0u0j0u0J0Zys0r0{',   # cipher: bAnanASplit
        'Dan_Aykroyd': 'i0N00h00^0{b',          # cipher: bEaUtY
        'John_Belushi': 'j0J0sc0v0w0L0',        # cipher: cAlZonE
    }
    #user_tmp = pass_tmp = str() # Default code

    #Split credentials into two parts
    username = credentials.split()[:2] #"first two words in credentials"
    password = credentials.split()[2]

    user_tmp = format_username(username)
    pass_tmp  = decrypt_password(password)

    ''' PSEUDO CODE
    PARSE string value of 'credentials' into its components: username and password.
    SEND username for FORMATTING by utilizing devoted function. Store return value in 'user_tmp'.
    SEND password for decryption by utilizing devoted function. Store return value in 'pass_tmp'.
    VALIDATE that both values corresponds to expected credentials existing within dictionary.
    RETURN outcome of validation as BOOLEAN VALUE.
    '''

def format_username(username: list) -> str: # Take input as list, return string
    """Procedure to format user provided username"""

    ''' PSEUDO CODE
    FORMAT first letter of given name to be UPPERCASE.
    FORMAT first letter of surname to be UPPERCASE.
    REPLACE empty space between given name and surname with UNDERSCORE '_'
    RETURN formatted username as string value.
    '''
    #Convert list to string
    credentials_string = " "
    credentials_string = credentials_string.join(username)

    #Uppercase the first word
    credentials = credentials_string.title()

    # Convert whitespace to underscore
    credentials = credentials.replace(" ", "_")
    #return credentials


def decrypt_password(password: str) -> str: #Takes pwd from authenticate_user and formats it
    """Procedure used to decrypt user provided password"""
    rot7, rot9 = 7, 9       # Rotation values. MAY NOT BE MODIFIED!!
    vowels = 'AEIOUaeiou'   # MAY NOT BE MODIFIED!!
    decrypted = str()

    ''' PSEUDO CODE
    REPEAT {
        DETERMINE if char IS VOWEL.
        DETERMINE ROTATION KEY to use.
        DETERMINE decryption value
        ADD decrypted value to decrypted string
    }
    RETURN decrypted string value
    '''
    for i in range(len(password)):
        if i % 2 == 0:
            current_rot = 7
            if password[i] in vowels:
                tmp = ord(password[i]) + current_rot
                new_val = chr((tmp - 127) + 31) if tmp > 127 else chr(tmp)
                new_val = "0" + new_val + "0"
                decrypted += new_val
            else:
                tmp = ord(password[i]) + current_rot
                new_val = chr((tmp - 127) + 31) if tmp > 127 else chr(tmp)
                decrypted += new_val

        else:
            current_rot = 9
            if password[i] in vowels:
                tmp = ord(password[i]) + current_rot
                new_val = chr((tmp - 127) + 31) if tmp > 127 else chr(tmp)
                new_val = "0" + new_val + "0"
                decrypted += new_val
            else:
                tmp = ord(password[i]) + current_rot
                new_val = chr((tmp - 127) + 31) if tmp > 127 else chr(tmp)
                decrypted += new_val

"""
def main():
    The main program execution. YOU MAY NOT MODIFY ANYTHING IN THIS FUNCTION!!
    epilog = "DT0179G Assignment 2 v" + __version__
    parser = argparse.ArgumentParser(description=__desc__, epilog=epilog, add_help=True)
    parser.add_argument('credentials', metavar='credentials', type=str,
                        help="Username and password as string value")

    args = parser.parse_args()

    if not authenticate_user(args.credentials):
        print("Authentication failed. Program exits...")
        sys.exit()

    print("Authentication successful. User may now access the system!")


if __name__ == "__main__":
    main()"""
