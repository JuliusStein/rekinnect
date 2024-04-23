#register global variables
global users, passwords
users = {}
passwords = {}

#function to create user password combo and store it in a global dictionary
def createPassword():
    #create a dictionary to store the user password
    password = {}
    #prompt the user to enter their password
    password["password"] = input("Enter your password: ")
    #prompt the user to re-enter their password
    password["confirmPassword"] = input("Confirm your password: ")
    #check if the two passwords match
    if password["password"] == password["confirmPassword"]:
        #if the passwords match, store the password in the global dictionary
        global passwords
        passwords = password
        #return the password
        return password
    else:
        #if the passwords do not match, print an error message
        print("Passwords do not match. Please try again.")
        #call the createPassword function again
        createPassword()

def registerUser():
    #create a dictionary to store the user's details
    user = {}
    #prompt the user to enter their name
    user["name"] = input("Enter your name: ")
    #prompt the user to enter their age
    user["age"] = int(input("Enter your age: "))
    #prompt the user to enter their language
    user["language"] = input("Enter your language: ")
    #call the createPassword function to create the user password
    user["password"] = createPassword()
    #store the user details in the global dictionary
    global users
    users = user
    #return the user details
    return user