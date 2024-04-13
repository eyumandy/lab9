def decode(password):
    decoded_password = ''
    for num in password:
        decoded_password += str(int(num)-3)
    return decoded_password
