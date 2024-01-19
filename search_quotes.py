from models import Quote, Author

while True:
    user_input = input("Введіть команду: ").split(':')
    command, value = user_input[0].strip().lower(), user_input[1].strip()

    if command == 'name':
        author_quotes = Quote.objects(author__fullname=value)
        for quote in author_quotes:
            print(quote.quote)
    elif command == 'tag':
        tag_quotes = Quote.objects(tags=value)
        for quote in tag_quotes:
            print(quote.quote)
    elif command == 'tags':
        tag_list = value.split(',')
        tags_quotes = Quote.objects(tags__in=tag_list)
        for quote in tags_quotes:
            print(quote.quote)
    elif command == 'exit':
        break
    else:
        print("Невідома команда. Спробуйте ще раз.")
