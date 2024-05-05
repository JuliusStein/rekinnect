import csv
import os
import time, math, random
from translationService import get_language_code, translate, initializeModel
#from transformers import pipeline
from storageService import connect, addQuestion

global questions
global lang, language
questions = []

def loadQuestions():
    global questions
    #read in a csv containing a list of questions
    with open('data/questions.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        #extract the first collumn as ids
        ids = [i[0] for i in data] 
        #extract the second collumn as questions
        questionsRaw = [i[1] for i in data]
        #extract the third collumn as categories
        categories = [i[2] for i in data]
        for i in range(1,len(ids)):
            questions.append((ids[i], questionsRaw[i], categories[i]))

loadQuestions()
random.shuffle(questions)
#print(questions[10])

def rephraseQuestion(questionText):
    ## create pieline for generating text
    #gen = pipeline('summarization')
    ## generate a new question based on the input question
    #new_question = gen(question)
    #return new_question[0]["summary_text"]
    return questionText

def chooseLanguage():
    global lang, language
    #choose language and initialize model
    language = input("Choose Language: ")
    if language == "" or language == " " or language == "english" or language == "en" or language == "eng" or language == "eng":
        language = "english"
        lang = "en"
    else:
        lang = get_language_code(language)
        initializeModel(lang)
    return lang, language

def speakQuestion(question, langCode):
    #take in any string and speak it aloud
    from gtts import gTTS  

    myobj = gTTS(text=question, lang=langCode, slow=False) 
    myobj.save("data/output.mp3") 
    os.system("start data/output.mp3") 


def storeResponse(userID, question, response):
    addQuestion(userID, question[0], question[1], question[2], response)

def runService(userID = "testUser3", speech = False):
    global lang, language
    os.system("cls")
    #choose language and initialize model
    lang, language = chooseLanguage()

    num = 0
    #translate each question and print the result
    for quest in questions:
        os.system("cls")
        if language != "english":
            question = translate(quest[1], lang)
        else:
            question = quest[1]
        
        print(question)
        time.sleep(0.5)
        if speech: 
            print("Generating spoken audio...")
            print("......\n")
            speakQuestion(question, lang)

        answer = input("> ")
        if answer != "":
            if answer == "LANG":
                lang = chooseLanguage()
                print("Loading new language model...")
                time.sleep(0.25)
                print("......\n")
                time.sleep(0.25)        
            elif answer.lower() in ["yes", "y", "yeah", "yep"]:
                answer = "Y"
                print("Response recorded")
                time.sleep(0.25)
                print("......\n")
                time.sleep(0.25)
            elif answer.lower() in ["no", "n", "nope", "nah"]:
                answer = "N"
                print("Response recorded")
                time.sleep(0.25)
                print("......\n")
                time.sleep(0.25)
            elif answer.lower() in ["idk", "i don't know", "dont know", "not sure"]:
                answer = "IDK"
                print("Response recorded")
                time.sleep(0.25)
                print("......\n")
                time.sleep(0.25)
            elif answer.lower() in ["probably", "probs", "probably yes", "prob", "p"]:
                answer = "P"
                print("Response recorded")
                time.sleep(0.25)
                print("......\n")
                time.sleep(0.25)
            elif answer.lower() in ["probably not", "probs not", "probably no", "prob no", "pn", "p n"]:
                answer = "PN"
                print("Response recorded")
                time.sleep(0.25)
                print("......\n")
                time.sleep(0.25)
            else:
                print("invalid answer, please enter Y, N, P, PN, or IDK\n")
                answer = "ERROR"
                
            #store the response in the database
            storeResponse(userID, quest, answer)
            #post the response to the console
            
            num += 1
            #print(str(round(num / len(questions),2)) + translate(" percent of questions completed", lang))
            print("Generating next question...")
            time.sleep(0.25)
            print("......\n")
            time.sleep(0.25)

        else:
            print("No answer given")
            answer = "SKIP"

runService("dh34kb1l34509b", True)
            
#print(rephraseQuestion("How far was your house from the nearest river?"))