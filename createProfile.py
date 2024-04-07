#create a class for the user profile that will store to begin with the user's name, age, and language
# the user's name will be stored as a string
# the user's age will be stored as an int
# the user's language will be stored as a string
class Profile:
    def __init__(self, name, age, language, details):
        self.name = name
        self.age = age
        self.language = language,
        self.details = {}

    # create a method to initialize the user profile
    def initializeProfile(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.language = input("Enter your language: ")

    # create a method to display the user profile
    def displayProfile(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Language: {self.language}")
    
    # create a method to update the user profile
    def updateBaseProfile(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.language = input("Enter your language: ")

    # create a method to add details to the user profile
    def addDetails(self, question, answer):
        self.details[question] = answer    
    
    
# create an instance of the Profile class
profile = Profile("First Second Patronym Family", 10, "Arabic")
