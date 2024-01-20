import os
from mongoengine import connect
from models import Quote, Author
from dotenv import load_dotenv

load_dotenv()

# Отримання значень змінних середовища
mongo_uri = os.getenv("MONGO_URI")
password = os.getenv("PASSWORD")

connect(db='your_database', host=mongo_uri.replace("<password>", password))

while True:
    user_input = input("Введіть команду: ").split(':')

    if len(user_input) >= 1:
        command = user_input[0].strip().lower()

        if command == 'name':
            if len(user_input) >= 2:
                value = user_input[1].strip()
                author = Author.objects(fullname=value).first()

                if author:
                    author_quotes = Quote.objects(author=author)
                    for quote in author_quotes:
                        print(quote.quote)
                else:
                    print("Автор не знайдений.")
            else:
                print("Неправильний формат команди. Спробуйте ще раз.")
        elif command == 'tag':
            if len(user_input) >= 2:
                value = user_input[1].strip()
                tag_quotes = Quote.objects(tags=value)
                for quote in tag_quotes:
                    print(quote.quote)
            else:
                print("Неправильний формат команди. Спробуйте ще раз.")
        elif command == 'tags':
            if len(user_input) >= 2:
                value = user_input[1].strip()
                tag_list = value.split(',')
                tags_quotes = Quote.objects(tags__in=tag_list)
                for quote in tags_quotes:
                    print(quote.quote)
            else:
                print("Неправильний формат команди. Спробуйте ще раз.")
        elif command == 'exit':
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")
    else:
        print("Неправильний формат команди. Спробуйте ще раз.")

