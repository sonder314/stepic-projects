import random
answers = ['Бесспорно', 'Мне кажется - да',	'Пока неясно, попробуй снова', 'Даже не думай', 'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 'Можешь быть уверен в этом', 'Да',	'Сконцентрируйся и спроси опять', 'Весьма сомнительно']

print('Привет Мир, я магический шар, и я знаю ответ на любой вопрос.')
name = input('Как вас зовут? ')
print(f'Привет, {name}')
ans = 'да'
ask = ''

while ans.lower() == 'да':
    ask = input('Введите ваш вопрос ')
    print(random.choice(answers))
    ans = input('Остались ещё вопросы? (да/нет) ')

print('Возвращайся, если возникнут вопросы! ')






