import csv
import time, math
from translationService import get_language_code, translate, initializeModel
from transformers import pipeline
from storageService import connect, addQuestion

questions = []
connect()

def loadQuestions():
    #read in a csv containing a list of questions
    with open('data/questions.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        #extract the first collumn as a list
        questions = [i[0] for i in data]
        
loadQuestions()

def rephraseQuestion(question):
    # create pieline for generating text
    gen = pipeline('summarization')
    # generate a new question based on the input question
    new_question = gen(question)
    return new_question[0]["summary_text"]

def saveAnswers(answers):
    with open('answers.csv', mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Question", "Answer", "Translated"])
        for ans in answers:
            writer.writerow([ans["question"], ans["answer"], ans["translated"]])

def storeResponse(question, response):
    addQuestion("testUser2", question, response)

def runService():
    #choose language and initialize model
    language = input("Choose Language: ")
    if language == "" or language == " " or language == "english" or language == "en" or language == "eng" or language == "eng":
        language = "english"
    else:
        lang = get_language_code(language)
        initializeModel(lang)

    num = 0
    answers = []
    #translate each question and print the result
    for quest in questions:
        if language != "english":
            question = translate(quest, lang)
        else:
            question = quest

        answer = input(question + ": ")
        if answer != "":
            if answer.lower() in ["yes", "y", "yeah", "yep"]:
                answer = "Y"
            elif answer.lower() in ["no", "n", "nope", "nah"]:
                answer = "N"
            elif answer.lower() in ["idk", "i don't know", "dont know", "not sure"]:
                answer = "IDK"
            elif answer.lower() in ["probably", "probs", "probably yes", "prob", "p"]:
                answer = "P"
            elif answer.lower() in ["probably not", "probs not", "probably no", "prob no", "pn", "p n"]:
                answer = "PN"
            else:
                print("invalid answer, please enter Y, N, P, PN, or IDK\n")
                answer = "ERROR"
                
            answers[num] = {"question": quest, "answer": answer, "translated": question}
            storeResponse(question, answer)
            num += 1
            print(str(round(num / len(questions),2)) + translate(" percent of questions completed", lang))
            print("......\n")

        else:
            print("No answer given")
            answer = "SKIP"

#runService()
            
print(rephraseQuestion("How far was your house from the nearest river?"))