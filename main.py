
from flask import Flask, render_template, request
import random
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

app = Flask(__name__)

def tokenize_paragraph(paragraph):
    # Tokenize the paragraph into sentences
    sentences = sent_tokenize(paragraph)
    return sentences

def preprocess_tokens(sentences):
    # Combine all sentences into a single list of tokens
    tokens = [word.lower() for sentence in sentences for word in word_tokenize(sentence)]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]

    return filtered_tokens

def generate_command(filtered_tokens):
    # Construct the command from the filtered tokens
    command = ' '.join(filtered_tokens)
    return command

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        paragraph = request.form['paragraph']

        # Tokenize the paragraph into sentences
        sentences = tokenize_paragraph(paragraph)

        # Preprocess tokens (remove stop words)
        filtered_tokens = preprocess_tokens(sentences)

        # Generate the command
        command = generate_command(filtered_tokens)

        return render_template('index.html', command=command)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


