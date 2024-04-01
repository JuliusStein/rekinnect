# Description: This file contains the code for the question service. This service is responsible for answering questions based on the context provided.
# Model and Tokenizer initialization
from transformers import pipeline
global question_answerer

# Initialize the question answering pipeline
question_answerer = pipeline(
    "question-answering",
    model="mrm8488/bert-multi-cased-finetuned-xquadv1",
    tokenizer="mrm8488/bert-multi-cased-finetuned-xquadv1"
)

# Given a context and a question, return the answer
def answer_question(question, context):
    return question_answerer(question=question, context=context)

def example_en():
    context = "On the first day of April, 17-year-old Wassim Hamam disappeared near the bustling centre of Hove. He was never seen again. Days later another teenager, Burim Markaj, 16, vanished nearby. Within hours, a 15-year-old was also reported missing. The disappearances continued. Four days later Alban Berisha, a 17-year-old whose portrait suggests a pensive, wary character, suddenly vanished from the streets of the Sussex coastal city. The same day, a 5ft 5in 17-year-old, Khalid Muha, was last seen wearing a black bomber jacket and white trainers."
    question = "what happened to Wassim Hamam?"
    response = answer_question(question, context)
    print(response['answer'])

def example_es():
    context = "El 1 de abril, Wassim Hamam, de 17 años, desapareció cerca del bullicioso centro de Hove. Nunca más se le volvió a ver. Días después, otro adolescente, Burim Markaj, de 16 años, desapareció cerca. Horas después, también se informó de la desaparición de un joven de 15 años. Las desapariciones continuaron. Cuatro días después, Alban Berisha, de 17 años, cuyo retrato sugiere un carácter pensativo y cauteloso, desapareció repentinamente de las calles de la ciudad costera de Sussex. El mismo día, Khalid Muha, de 17 años y 5 pies 5 pulgadas, fue visto por última vez llevando una chaqueta bomber negra y zapatillas blancas."
    question = "¿Qué le pasó a Wassim Hamam?"
    response = answer_question(question, context)
    print(response['answer'])

def example_fr():
    context = "Le premier avril, Wassim Hamam, 17 ans, a disparu près du centre animé de Hove. On ne l'a jamais revu. Quelques jours plus tard, un autre adolescent, Burim Markaj, 16 ans, a disparu à proximité. Quelques heures plus tard, un jeune de 15 ans a également été signalé disparu. Les disparitions ont continué. Quatre jours plus tard, Alban Berisha, 17 ans, dont le portrait suggère un caractère pensif et méfiant, a soudainement disparu des rues de la ville côtière du Sussex. Le même jour, un jeune de 17 ans, Khalid Muha, mesurant 5 pieds 5 pouces, a été vu pour la dernière fois portant une veste de bombardier noire et des baskets blanches."
    question = "Qu'est-il arrivé à Wassim Hamam?"
    response = answer_question(question, context)
    print(response['answer'])

def example_ar():
    context = "في الأول من أبريل، اختفى وسيم حمام، البالغ من العمر 17 عامًا، بالقرب من مركز هوف الصاخب. لم يُرَ مرة أخرى. بعد أيام، اختفى مراهق آخر، بوريم ماركاج، 16 عامًا، بالقرب من هنا. في غضون ساعات، تم الإبلاغ أيضًا عن اختفاء شاب يبلغ من العمر 15 عامًا. استمرت الاختفاءات. أربعة أيام لاحقًا، اختفى ألبان بيريشا، 17 عامًا، الذي يوحي صورته بشخصية متأملة ومحترسة، فجأة من شوارع مدينة ساسكس الساحلية. في نفس اليوم، شوهد خالد موها، البالغ من العمر 17 عامًا والذي يبلغ طوله 5 أقدام و5 بوصات، يرتدي سترة قنبلة سوداء وحذاء رياضي أبيض."
    question = "ماذا حدث لوسيم حمام؟"
    response = answer_question(question, context)
    print(response['answer'])

example_ar()