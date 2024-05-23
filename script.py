from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Initialize a transformer-based pipeline for question answering
nlp = pipeline('question-answering')

def answer_question(context, question):
    result = nlp(question=question, context=context)
    return result['answer']

# Read from a text file
with open('info.txt', 'r', encoding='utf-8') as file:
    text = file.read()

@app.route("/")
def home():    
    return render_template("index.html") 

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(answer_question(text, userText))

if __name__ == "__main__":    
    app.run()
