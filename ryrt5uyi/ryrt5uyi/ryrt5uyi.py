import os 

# Функция для чтения слов из файлов и создания словаря
def create_dictionary():
    russian_words = []
    estonian_words = []
    with open('russian_words.txt', 'r') as f:
        for line in f:
            russian_words.append(line.strip())

    with open('estonian_words.txt', 'r') as f:
        for line in f:
            estonian_words.append(line.strip())

    dictionary = dict(zip(russian_words, estonian_words))
    return dictionary

# Функция для добавления новых слов в словарь
def add_word(dictionary):
    print('Sisestage sõnaraamatusse lisamiseks venekeelne sõna:')
    russian_word = input()
    if russian_word in dictionary:
        print(f'Sõna "{russian_word}" on juba olemas.')
    else:
        print(f'Sisestage sõna tõlge "{russian_word}" eesti keeles:')
        estonian_word = input()
        dictionary[russian_word] = estonian_word
        with open('russian_words.txt', 'a') as f1, open('estonian_words.txt', 'a') as f2:
            f1.write(f'{russian_word}\n')
            f2.write(f'{estonian_word}\n')
        print(f'Слово "{russian_word}" lisatud sõnastikku koos tõlkega "{estonian_word}".')

# Создание словаря
dictionary = create_dictionary()

# Поиск перевода слов на эстонском языке по словам на русском языке или добавление новых слов
while True:
    print('Tõlke otsimiseks või uue sõna lisamiseks sisestage sõna vene keeles (või "exit" lõpetamiseks):')
    russian_word = input()
    if russian_word == 'exit':
        break
    if russian_word in dictionary:
        print(f'Sõna tõlge "{russian_word}" eesti keeles: {dictionary[russian_word]}')
    else:
        print(f'Sõna "{russian_word}" sõnaraamatust ei leitud. Kas soovite selle sõnaraamatusse lisada? (Mitte päris)')
        choice = input()
        if choice.lower() == 'jah':
            add_word(dictionary)
