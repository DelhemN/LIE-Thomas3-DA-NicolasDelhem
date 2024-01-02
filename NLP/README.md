# Natural Language Processing

![nlp](https://canopylab.com/wp-content/uploads/2019/11/shutterstock_1455391502-2.jpg)

## What is NLP?

**NLP** stands for **N**atural **L**anguage **P**rocessing.
In simpler words: "Making the machine understand human language". This field is becoming more and more popular in companies.
Why, you will ask? That is because being able to understand French, English, Dutch, and other languages helps companies automate boring task.

Imagine having to classify emails to filter spam, or to redirect each email to the correct departement.
Imagine having to read thousands of documents just to extract the name of the author or to classify the document in categories, to check the price of an invoice, etc...

Well, with NLP we are able to automate those tasks.

## How is that possible?

As you know, machines don't understand letters, they only understand numbers. That's why the first step will be preprocessing the text. We will have to translate our words to **vectors** (series of numbers).
Ok. The machine can now identify words, great.
But a language is complicated, a single word can have many different declinations. To avoid the machine thinking "accurate" and "accuracy" are two completly different words, we will apply **lemmatization**. It will convert each word to its simplest version. There are a lot of other preprocessing steps possible but we will see them later.

Now that the text is understandable by the machine, we can start the fun part: **modeling**. There are several possible models depending on the task you want to perform. NLP is in the midle of an amazing expansion, it evolves a lot. That's why we will try to make you understand these keys concept, rather than sticking to very specific things.

![Trust the process](https://media.giphy.com/media/XGVB1T61iAr4IEilhd/giphy.gif)

## Some vocabulary

To understand blog posts, courses, and discussions about NLP, you will need to understand a few words:

* **A corpus:** a collection of text (a dataset). It can be legal documents, book, papers, emails,...
* **A document**: an element of a corpus. If we have a corpus of mails, a single mail is a document. For a **corpus** of books, each book is a document.
* **Stop words:** All the small words usually removed during the preprocessing of the document. (the, a, an,...)
* **Vocabulary:** the list of all the words in the corpus.
* **Parts Of Speech (POS):** This is the syntatic function of a word in a sentence. (noun, verb, adverb, adjective,...)

## Structure of the course

1. Preprocessing
    * Tokenization
    * Embeddings
    * Lemmatization
    * Tagging and chunking
    * Html tags
    * Text formatting
    * Stop words
2. Modeling
    * Document classification (TF-ID)
    * Named Entity Recognition (NER)
    * Spacy
    * RNN
    * Sementic search
    * Chatbots (Rasa NLU)
    * Attention layers
    * Transformers (Bert)
    * RoBERTa

3. Projects
    * Email classification
    * Spam filtering
    * Document classification
    * Semantic search
    * Chatbot restaurant
    * NER project

Good luck!
