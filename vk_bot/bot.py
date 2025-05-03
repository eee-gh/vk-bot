import vk_api
from keyboards import *
from messages import *
from vk_api.longpoll import VkLongPoll, VkEventType

t = open('token.txt')
TOKEN = list(t)[0]
t.close()
vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def write_msg(uid, message):
    try:
        vk.messages.send(
            user_id=uid,
            message=message,
            random_id=0
        )
    except vk_api.exceptions.ApiError as e:
        print(f'Произошла ошибка API: {e}')


def keyboard_run(keyboard, uid, message):
    try:
        vk.messages.send(
            user_id=uid,
            message=message,
            random_id=0,
            keyboard=keyboard
        )
    except vk_api.exceptions.ApiError as e:
        print(f'Произошла ошибка API: {e}')


def send_to_admin(uid, m_text):
    try:
        f = open('adminid.txt', 'r')
        a_id = list(f)[0]
        f.close()
        write_msg(int(a_id), m_text)
    except FileNotFoundError:
        write_msg(uid, not_available)


print('Чат-бот работает')
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        message_text = str(event.text).strip()
        if message_text[0] == '#':
            send_to_admin(user_id, message_text[1:])
            continue
        else:
            message_text = message_text.lower()
        if message_text == 'моего вопроса нет в списке':
            write_msg(user_id, not_in_list)
        elif message_text == 'faq':
            write_msg(user_id, faq)

        elif message_text == 'начало занятий':
            write_msg(user_id, training_start)
        elif message_text == 'стоимость обучения':
            write_msg(user_id, price)
        elif message_text == 'что необходимо принести?':
            write_msg(user_id, requirements)

        elif message_text == 'подать заявку':
            write_msg(user_id, send_application)
        elif message_text == 'запись в автошколу':
            keyboard_run(keyboard_enrollment, user_id, generic)
        elif message_text == 'как записаться?':
            write_msg(user_id, place_n_time)
        elif message_text == 'срок обучения':
            write_msg(user_id, training_duration)

        elif message_text == 'занятия':
            keyboard_run(keyboard_training, user_id, generic)
        elif message_text == 'распорядок занятий':
            write_msg(user_id, attendance)
        elif message_text == 'внутренний экзамен':
            write_msg(user_id, exam)
        elif message_text == 'пересдачи экзаменов':
            write_msg(user_id, retake)

        elif message_text == 'оплата':
            keyboard_run(keyboard_payment, user_id, generic)
        elif message_text == 'оплата за вождение':
            write_msg(user_id, driving_charge)
        elif message_text == 'оплата частями':
            write_msg(user_id, payment)
        elif message_text == 'реквизиты для оплаты':
            write_msg(user_id, payment_req)

        elif message_text == 'обучение до 18':
            keyboard_run(keyboard_underage, user_id, extra_info)
        elif message_text == 'необходимые документы':
            write_msg(user_id, underage_req)
        elif message_text == 'медицинское страхование':
            write_msg(user_id, underage_med)

        else:
            keyboard_run(keyboard_start, user_id, start_message)
