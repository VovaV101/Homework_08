import json
import os
from mongoengine import connect
from models import Quote, Author
from dotenv import load_dotenv

load_dotenv()

# Отримання значень змінних середовища
mongo_uri = os.getenv("MONGO_URI")
password = os.getenv("PASSWORD")

connect(db='your_database', host=mongo_uri.replace("<password>", password))

# Завантаження авторів
with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)
    for author_data in authors_data:
        author = Author(**author_data)
        author.save()

# Завантаження цитат
with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)
    for quote_data in quotes_data:
        author_name = quote_data.get('author')
        author = Author.objects(fullname=author_name).first()
        quote_data['author'] = author
        quote = Quote(**quote_data)
        quote.save()
