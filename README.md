Magtymguly Pyragy related questions answering simple script using Hugging Face Transformers.
This script uses the Hugging Face's Transformers library to answer questions based on a given context. The context is read from a text file and the question is provided by the user.

How to Use:
Ensure that you have the Transformers library installed. If not, you can install it using pip:

pip install transformers

Place your context in a text file named 'info.txt' in the same directory as the script.

Run the script:
python script.py
When prompted, enter your question. The script will return the answer based on the context provided in 'info.txt'.


Code Overview
The script initializes a transformer-based pipeline for question answering. It then defines a function answer_question that takes a context and a question, and returns the answer to the question based on the context.

The script reads the context from 'info.txt', asks the user to input a question, and then prints the answer to the question.

Dependencies
Python 3
Transformers library
Please note that the accuracy of the answers depends on the quality of the context provided and the capabilities of the transformer model used.
