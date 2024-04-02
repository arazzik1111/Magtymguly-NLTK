from transformers import pipeline

# Initialize a transformer-based pipeline for question answering
nlp = pipeline('question-answering')

def answer_question(context, question):
    result = nlp(question=question, context=context)
    return result['answer']



# Read from a text file
with open('info.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Ask for user input
while True:
    question = input("Please enter your question: ")
    print(answer_question(text, question))