from random import choice

def  random_user_id(): # function to generate a random user ID
    no = input("Enter the number of characters you want in your user ID: ") # asking user for number of characters
    ValueError if not no.isdigit() else int(no) # validating input
    no = int(no) 
    id = ()
    for i in range(no):  # generating random characters for the user ID
        id += choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'),
    return ''.join(id)

print(random_user_id()) # printing the generated user ID