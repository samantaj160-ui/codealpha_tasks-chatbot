# AI FAQ Chatbot using NLP (NLTK)

## Project Overview

This project is an AI-based FAQ chatbot built using Natural Language Processing (NLP).

The chatbot accepts user questions and finds the most relevant answer from the FAQ dataset using NLP techniques.

## Features

- FAQ based chatbot
- NLP text preprocessing using NLTK
- Tokenization
- Stopword Removal
- Stemming
- TF-IDF Vectorization
- Cosine Similarity Matching
- Available FAQ question section
- Add new Question and Answer
- Flask Web Interface

## Technologies Used

- Python
- Flask
- NLTK
- Scikit-learn
- HTML
- CSS
- JavaScript

## NLP Workflow

User Question

↓

NLTK Preprocessing

(Tokenization + Stopword Removal + Stemming)

↓

TF-IDF Vectorization

↓

Cosine Similarity Matching

↓

Best FAQ Answer

↓

Response Displayed

## Project Structure

```
AI_FAQ_ChatBOT/

│
├── app.py
├── faq_data.json
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## Installation

Install all required libraries:

```bash
pip install -r requirements.txt
```

## Run Project

Start the Flask server:

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

## How It Works

1. User enters a question.
2. NLTK preprocesses the text.
3. Text is converted into numerical vectors using TF-IDF.
4. Cosine Similarity compares the question with stored FAQs.
5. The chatbot returns the closest answer.

## Why This Project Does Not Run Directly on GitHub

GitHub is mainly used for storing and sharing source code.

This project uses:

- Python
- Flask backend
- NLTK processing

GitHub Pages only supports static websites (HTML, CSS, JavaScript).

It cannot execute:

- Python files
- Flask server
- NLP processing

Therefore, the project cannot run directly by opening it from GitHub Pages.

## Run Project From GitHub

1. Clone or download the repository.

2. Open the folder in VS Code.

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run:

```bash
python app.py
```

5. Open:

```
http://127.0.0.1:5000
```


## Project Purpose

This project demonstrates the use of NLP techniques to build an intelligent FAQ chatbot.
