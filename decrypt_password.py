def decrypt_password(password: str) -> str:
    """Procedure used to decrypt user provided password"""
    rot7, rot9 = 7, 9       # Rotation values. MAY NOT BE MODIFIED!!
    vowels = 'AEIOUaeiou'   # MAY NOT BE MODIFIED!!
    decrypted = str()

    print(len(password))
    if len(password) % 2 == 0:
        current_rot = 7
        print("Using Rot 7")
    else:
        current_rot = 9
        print("Using Rot 9")


        for char in password:
            if char in vowels:
                tmp = ord(char) + current_rot
                new_val = chr((tmp - 127) + 31) if tmp > 127 else chr(tmp)
                new_val = "0" + new_val + "0"
                decrypted += new_val
            else:
                tmp = ord(char) + current_rot
                new_val = chr((tmp - 127) + 31) if tmp > 127 else chr(tmp)
                decrypted += new_val

    print(decrypted)
    return decrypted

#decrypt_password("PASSWORD")
decrypt_password("passwordddok")

#decrypt_password("bAnanASplit")

