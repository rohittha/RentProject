import openpyxl


# This function is used to encrypt the password directly from the file.
# This way, if we change the encryption values in the source Excel file, we don't have to change anything in the
def encrypt_password(unencrypted_pwd):
    print(unencrypted_pwd)

    workbook = openpyxl.load_workbook(r'chyper-code.xlsx')
    sheet = workbook.active

    encrypted_password = ""
    for letter in unencrypted_pwd:
        index = 0
        for cell in sheet['A']:
            if letter.isnumeric():
                if int(letter) == cell.value:
                    encrypted_password += str(sheet['B'][index].value)
            elif letter.isalpha():
                if not letter.isnumeric():
                    if letter.upper() == cell.value:
                        encrypted_password += sheet['B'][index].value
            index += 1

    return encrypted_password
