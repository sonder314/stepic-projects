from random import choice
word_list = ['дом', 'пчела', 'каравай', 'подъезд', 'ухо', 'телескоп', 'воронка', 
'домофон', 'апликатор', 'медицина',  'гороскоп', 'алмаз', 'камень', 'ковёр', 'лицо', 'человек', 'слон', 'скрепка', 'канализация']

def get_word():
    return str(choice(word_list )).upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def word_result(letters, word):
    flag = False
    word_completition = ''
    for i in word:
        for j in letters:
            if i.upper() == j.upper():
                word_completition += j.upper()
                flag = True
        if flag == False:
            word_completition += '_'
        flag = False
    return word_completition


def play():
    word = get_word().upper()
    tries = 6
    guessed_letters = ''
    print('Давайте играть в угадайку слов!')
    print('Количество букв в слове:', len(word))
    print(len(word) * '_')
    if input('Хотите увидеть первую и последнюю буквы слова? да/нет ') == 'да':
        print(word[0] + len(word[1:-1]) * '_' + word[-1])
        guessed_letters += word[0] + word[-1]
    else:
        print('Хорошо, тогда думайте своими мозгами... ')
    while tries != 0:
        print(display_hangman(tries))
        letter = input('Введите букву ')
        if letter.upper() not in guessed_letters and letter in 'йцукенгшщзхъфывапролджэячсмитьбю' and len(str(letter)) == 1:
            guessed_letters += letter.upper()
            print(word_result(guessed_letters, word))
        else:
            print('Ваш символ не похож на русскую букву')
            continue
        if input('Уже готовы угадать слово? да/нет ').lower() == 'да':
            if input('Попробуйте угадать слово ').upper() != word:
                print('Неправильно...', 'Попробуйте ещё раз', sep='\n')
            else:
                print('Поздравляем! Вы выиграли и получили самое бесценное, что у вас было и будет - жизнь!')
                break
        tries -= 1
        print(f'Оставшееся количесвто попыток {tries}')
    else:
        print(display_hangman(tries))
        print('Вы не смогли угадать слово и проиграли. Из-за вас, между прочим, повесили невинного человечка')
        print(f'А загаданное слово было {word}')

        
    

    


    

