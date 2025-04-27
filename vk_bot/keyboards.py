import json

keyboard_start = json.dumps({
    'one_time': False,
    'buttons': [
        [
            {'action': {'type': 'text', 'label': 'Начало занятий'}, 'color': 'primary'},
            {'action': {'type': 'text', 'label': 'Стоимость обучения'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Что необходимо принести?'}, 'color': 'secondary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Запись в автошколу'}, 'color': 'primary'},
            {'action': {'type': 'text', 'label': 'Занятия'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Оплата'}, 'color': 'primary'},
            {'action': {'type': 'text', 'label': 'Обучение до 18'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'FAQ'}, 'color': 'secondary'},
            {'action': {'type': 'text', 'label': 'Моего вопроса нет в списке'}, 'color': 'secondary'}
        ]
    ]
})

keyboard_enrollment = json.dumps({
    'one_time': False,
    'buttons': [
        [
            {'action': {'type': 'text', 'label': 'Подать заявку'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Как записаться?'}, 'color': 'primary'},
            {'action': {'type': 'text', 'label': 'Начало занятий'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Срок обучения'}, 'color': 'primary'},
            {'action': {'type': 'text', 'label': 'Что необходимо принести?'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Вернуться'}, 'color': 'secondary'}
        ],
    ]
})

keyboard_training = json.dumps({
    'one_time': False,
    'buttons': [
        [
            {'action': {'type': 'text', 'label': 'Распорядок занятий'}, 'color': 'primary'}

        ],
        [
            {'action': {'type': 'text', 'label': 'Внутренний экзамен'}, 'color': 'primary'},
            {'action': {'type': 'text', 'label': 'Пересдачи экзаменов'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Вернуться'}, 'color': 'secondary'}
        ],
    ]
})

keyboard_payment = json.dumps({
    'one_time': False,
    'buttons': [
        [
            {'action': {'type': 'text', 'label': 'Оплата за вождение'}, 'color': 'primary'},
            {'action': {'type': 'text', 'label': 'Оплата частями'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Реквизиты для оплаты'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Вернуться'}, 'color': 'secondary'}
        ],
    ]
})

keyboard_underage = json.dumps({
    'one_time': False,
    'buttons': [
        [
            {'action': {'type': 'text', 'label': 'Необходимые документы'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Медицинское страхование'}, 'color': 'primary'}
        ],
        [
            {'action': {'type': 'text', 'label': 'Вернуться'}, 'color': 'secondary'}
        ]
    ]
})
