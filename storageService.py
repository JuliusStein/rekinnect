import firebase_admin
from firebase_admin import db
from firebase_admin import credentials

import json

def connect():
    cred_obj = credentials.Certificate("config/project-kin-48cec-firebase-adminsdk-b46sc-d108556471.json")
    default_app = firebase_admin.initialize_app(cred_obj, {
        'databaseURL':"https://project-kin-48cec-default-rtdb.firebaseio.com/"
        })
    return default_app

app = connect()

def initializeDB():
    ref = db.reference("/user123/questions")
    with open("data/peopleQuestions.json", "r") as f:
        file_contents = json.load(f)
        ref.set(file_contents)
    print("Database Initialized")

def addQuestions(userid, questionPath):
    ref = db.reference("/" + userid + "/questions")
    with open("data/"+questionPath, "r") as f:
        file_contents = json.load(f)
    for key, value in file_contents.items():
        ref.push().set(value)
    print("Questions Added")

def addQuestion(userid, questionID, question,  response):
    ref = db.reference("/" + userid + "/questions")

    questionObj = {"questionID":questionID, "question": question, "response": response}
    ref.push().set(questionObj)
        
    print("Question Added")

def getQuestions(userid):
    ref = db.reference("/" + userid + "/questions")
    return ref.get()

def getQuestion(userid, questionid):
    ref = db.reference("/" + userid + "/questions/" + questionid)
    return ref.get()

def deleteQuestion(userid, questionid):
    ref = db.reference("/" + userid + "/questions/" + questionid)
    ref.delete()

def deleteUser(userid):
    ref = db.reference("/" + userid + "/questions")
    ref.delete()

def addUser(userid):
    ref = db.reference("/" + userid)
    ref.set({"questions": {}})

#initializeDB()
#addQuestions("user123", "testQuestion.json")
addQuestion("user123", "222", "Were you an only child?", "Y")

