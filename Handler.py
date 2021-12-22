import random
from Function import function
from Text_recognition import Yes
from Text_recognition import No
from Text_recognition import Ready
from Text_recognition import Right
from Text_recognition import Wrong
from Text_recognition import Practice
from Text_recognition import Theory
from Text_recognition import Exit
from Text_recognition import GoOn
from Theory_function import ask
from Theory_function import ans
from Theory_function import clas














def handler(event, context):
    """

    Entry-point for Serverless Function.
    :param event: request payload.
    :param context: information about current execution context.
    :return: response to be serialized as JSON.
    """
    end_session = 'false'
    button1_text = 'Теория'
    button1_hide = 'false'
    button2_text = 'Практика'
    button2_hide = 'false'
    exit_button_hide = 'false'
    reqest_input = str(event['request']['original_utterance'])
    reqest_input = reqest_input.upper()
    if bool(event['session']['new']):
        text = 'Привет! Я - Пост, меня назвали в честь Эмиля Поста, чью теорему ты будешь активно использовать далее.' \
               ' Я помогу тебе в подготовке к зачёту и в освоении программы предмета математические основы информатики.' \
               ' С чего начнём?'
        state_value = '111110'
    else:
        text = 'Прости, я тебя не понял, попробуй перефразировать.'
        state_value = str(event['state']['session']['value'])
    if Exit(reqest_input):
        end_session = 'true'
        text = 'Увидимся снова! Удачи!'
        button2_hide = 'true'
        button1_hide = 'true'
        exit_button_hide = 'true'
    if Practice(reqest_input):
        random.seed()
        a = random.randint(1, 6)
        if a > 3:
            f = function(8)
            text_funkt = str()
            for i in range(8):
                text_funkt += str(f.vect[i])
            text = "Определи, к каким замкнутым классам Поста относится функция f = " + text_funkt + "? Когда будешь готов дать отвект просто скажи \"Я готов\" или нажми кнопку."
            state_value = "7" + f.post_vect + "0"
            button2_hide = 'true'
            button1_text = 'Я готов'
        else:
            f = function(8)
            g = function(8)
            text_f = str()
            text_g = str()
            for i in range(8):
                text_f += str(f.vect[i])
                text_g += str(g.vect[i])
            text = "Определи, является ли система {f, g} где f = " + text_f + " и g =" + text_g + " функционально полной?"
            is_syst = 1
            for i in range(5):
                is_syst = int(f.post_vect[i]) * int(g.post_vect[i])
            state_value = '6' + str(is_syst) + '00000'
            button1_text = "Да"
            button2_text = "Нет"
    if state_value[0] == '6' and state_value[6] == '0':
        if bool(state_value[2]):
            if Yes(reqest_input):
                text = "Молодец, так держать! Продолжим?"
                button1_text = "Продолжим"
                button2_hide = 'true'
                state_value = LastJoin(state_value, "9")
            else:
                if No(reqest_input):
                    text = "А вот и нет, впредь будь внимательнее. Продолжим?"
                    button1_text = "Продолжим"
                    button2_hide = 'true'
                    state_value = LastJoin(state_value, "9")
        else:
            if No(reqest_input):
                text = "Молодец, так держать! Продолжим?"
                button1_text = "Продолжим"
                button2_hide = 'true'
                state_value = LastJoin(state_value, "9")
            else:
                if Yes(reqest_input):
                    text = "А вот и нет, впредь будь внимательнее. Продолжим?"
                    button1_text = "Продолжим"
                    button2_hide = 'true'
                    state_value = LastJoin(state_value, "9")
    if state_value[0] == '7' and Ready(reqest_input) and state_value[6] == '0':
        random.seed()
        a = random.randint(1, 5)
        text = "Принадлежит ли функция к классу " + clas(a) + "?"
        button1_text = "Принадлежит"
        button2_text = "Не принадлежит"
        temp = str()
        state_value = LastJoin(state_value, str(a))
    if state_value[0] == '7' and state_value[6] != '0' and state_value[6] != '9':
        if bool(state_value[int(state_value[6])]):
            if Yes(reqest_input):
                text = "Молодец, так держать! Продолжим?"
                button1_text = "Продолжим"
                button2_hide = 'true'
                state_value = LastJoin(state_value, "9")
            else:
                if No(reqest_input):
                    text = "А вот и нет, впредь будь внимательнее. Продолжим?"
                    button1_text = "Продолжим"
                    button2_hide = 'true'
                    state_value = LastJoin(state_value, "9")
        else:
            if No(reqest_input):
                text = "Молодец, так держать! Продолжим?"
                button1_text = "Продолжим"
                button2_hide = 'true'
                state_value = LastJoin(state_value, "9")
            else:
                if Yes(reqest_input):
                    text = "А вот и нет, впредь будь внимательнее. Продолжим?"
                    button1_text = "Продолжим"
                    button2_hide = 'true'
                    state_value = LastJoin(state_value, "9")
    if (state_value[0] == '7' or state_value[0] == '6') and state_value[6] == '9' and GoOn(reqest_input):
        random.seed()
        a = random.randint(1, 6)
        if a > 3:
            f = function(8)
            text_funkt = str()
            for i in range(8):
                text_funkt += str(f.vect[i])
            text = "Определи, к каким замкнутым классам Поста относится функция f = " + text_funkt + "? Когда будешь готов дать отвект просто скажи \"Я готов\" или нажми кнопку."
            state_value = "7" + f.post_vect + "0"
            button2_hide = 'true'
            button1_text = 'Я готов'
        else:
            f = function(8)
            g = function(8)
            text_f = str()
            text_g = str()
            for i in range(8):
                text_f += str(f.vect[i])
                text_g += str(g.vect[i])
            text = "Определи, является ли система {f, g} где f = " + text_f + " и g =" + text_g + "?"
            is_syst = 1
            for i in range(5):
                is_syst = int(f.post_vect[i]) * int(g.post_vect[i])
            state_value = '6' + str(is_syst) + '00000'
            button1_text = "Да"
            button2_text = "Нет"
    state_value = int(state_value)
    if Theory(reqest_input):
        random.seed()
        a = random.randint(10, 30)
        state_value = 9000000 + a
        text = "Сформулируйте " + ask(a) + " Когда будешь готов дать ответ просто скажи \"Я готов\" или нажми кнопку."
        button2_hide = 'true'
        button1_text = 'Я готов'
    if state_value > 9000000 and Ready(reqest_input):
        text = "Внимание, правильный ответ:'\n'" + ans(
            state_value - 9000000) + "'\n'Надеюсь, что ты был прав, я в тебе не ошибся?"
        button1_text = "Я был прав"
        button2_text = "Я был не прав"
    if state_value > 9000000 and Right(reqest_input):
        text = "Молодец, так держать! Продолжим?"
        button1_text = "Продолжим"
        button2_hide = 'true'
        state_value = 9000000
    if state_value > 9000000 and Wrong(reqest_input):
        text = "Печалька, запомни на будущее. Продолжим?"
        button1_text = "Продолжим"
        button2_hide = 'true'
        state_value = 9000000
    if state_value >= 9000000 and GoOn(reqest_input):
        random.seed()
        a = random.randint(10, 30)
        state_value = 9000000 + a
        text = "Сформулируйте " + ask(a)
        button2_hide = 'true'
        button1_text = 'Я готов'

    return {
        'version': event['version'],
        'session': event['session'],
        'response': {
            'text': text,
            'buttons': [
                {"title": button1_text,
                 "hide": button1_hide},
                {"title": button2_text,
                 "hide": button2_hide},
                {"title": "Выход",
                 "hide": exit_button_hide}
            ],
            'end_session': end_session
        },
        "session_state": {
            "value": state_value
        },
    }
