from flask import Flask, render_template, request, jsonify
import json
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

app = Flask(__name__)

with open("faq_data.json", "r") as file:
    faqs = json.load(file)

stop_words = set(stopwords.words("english"))

def preprocess(text):

    tokens = word_tokenize(text.lower())

    filtered = []

    for word in tokens:
        if word.isalnum() and word not in stop_words:
            filtered.append(word)

    return " ".join(filtered)

def rebuild_model():

    global vectorizer
    global faq_vectors
    global processed_questions

    processed_questions = [
        preprocess(faq["question"])
        for faq in faqs
    ]

    vectorizer = TfidfVectorizer()

    faq_vectors = vectorizer.fit_transform(
        processed_questions
    )

rebuild_model()

def chatbot_response(user_input):

    processed_input = preprocess(user_input)

    user_vector = vectorizer.transform(
        [processed_input]
    )

    similarity = cosine_similarity(
        user_vector,
        faq_vectors
    )

    best_match = similarity.argmax()

    score = similarity[0][best_match]

    if score > 0.3:
        return faqs[best_match]["answer"]

    return "Sorry, I could not find an answer."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data["message"]

    reply = chatbot_response(user_message)

    return jsonify({
        "reply": reply
    })

@app.route("/questions")
def questions():

    return jsonify([
        faq["question"]
        for faq in faqs
    ])

@app.route("/add_faq", methods=["POST"])
def add_faq():

    global faqs

    data = request.get_json()

    question = data["question"]
    answer = data["answer"]

    faqs.append({
        "question": question,
        "answer": answer
    })

    with open(
        "faq_data.json",
        "w"
    ) as file:

        json.dump(
            faqs,
            file,
            indent=4
        )

    rebuild_model()

    return jsonify({
        "message":"FAQ Added Successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)