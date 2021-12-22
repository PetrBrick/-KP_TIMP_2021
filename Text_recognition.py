def Yes(input):
    agreements = {"ДА", "ЯВЛЯЕТСЯ", "ДА, ПРИНАДЛЕЖИТ", "ПРИНАДЛЕЖИТ", "СОГЛАСЕН", "УГУ", "АГА",
                  "ПРИНАДЛЕЖИТ", "ПРИНАДЛЕЖИТ T0", "ПРИНАДЛЕЖИТ T1", "ПРИНАДЛЕЖИТ S", "ПРИНАДЛЕЖИТ M", "ПРИНАДЛЕЖИТ L",
                  "СОХРАНЯЕТ 0", "СОХРАНЯЕТ НОЛЬ", "T0",
                  "СОХРАНЯЕТ 1", "СОХРАНЯЕТ ЕДИНИЦУ", "T1",
                  "САМОДВОЙСТВЕННАЯ", "S",
                  "ЛИНЕЙНАЯ", "L",
                  "МОНОТОННАЯ", "M"}
    if input in (agreements):
        return True
    else:
        return False


def No(input):
    disagreements = {"НЕТ", "НЕ ЯВЛЯЕТСЯ", "НЕТ, НЕ ПРИНАДЛЕЖИТ", "НЕ ПРИНАДЛЕЖИТ", "НЕ СОГЛАСЕН", "НЕ", "НЕА",
                     "НЕ ПРИНАДЛЕЖИТ T0", "НЕ ПРИНАДЛЕЖИТ T1", "НЕ ПРИНАДЛЕЖИТ S", "НЕ ПРИНАДЛЕЖИТ M",
                     "НЕ ПРИНАДЛЕЖИТ L",
                     "НЕ СОХРАНЯЕТ 0", "НЕ СОХРАНЯЕТ НОЛЬ", "НЕ T0",
                     "НЕ СОХРАНЯЕТ 1", "НЕ СОХРАНЯЕТ ЕДИНИЦУ", "НЕ T1",
                     "НЕ САМОДВОЙСТВЕННАЯ", "НЕ S",
                     "НЕ ЛИНЕЙНАЯ", "НЕ L",
                     "НЕ МОНОТОННАЯ", "НЕ M"}
    if input in (disagreements):
        return True
    else:
        return False


def Right(input):
    agreements = {"ДА", "СОГЛАСЕН", "УГУ", "АГА",
                  "ПРАВИЛЬНО", "ПРАВ", "Я ПРАВ", "Я ОТВЕТИЛ ПРАВИЛЬНО", "Я БЫЛ ПРАВ", "ОТВЕТИЛ ПРАВИЛЬНО"}
    if input in (agreements):
        return True
    else:
        return False


def Wrong(input):
    disagreements = {"НЕТ", "НЕ СОГЛАСЕН", "НЕ", "НЕА",
                     "НЕ РАВИЛЬНО", "НЕ ПРАВ", "Я НЕ ПРАВ", "Я ОТВЕТИЛ НЕПРАВИЛЬНО", "Я БЫЛ НЕ ПРАВ",
                     "ОТВЕТИЛ НЕПРАВИЛЬНО"}
    if input in (disagreements):
        return True
    else:
        return False


def Practice(input):
    practice = {"ПРАКТИКА", "ЗАДАЧИ", "РЕШАТЬ ЗАДАЧИ", "ПРАКТИКОВАТЬСЯ"}
    if input in (practice):
        return True
    else:
        return False


def Theory(input):
    theory = {"ТЕОРИЯ", "ОПРЕДЕЛЕНИЯ", "ВОПРОСЫ", "ИЗУЧАТЬ ТЕКОРИЮ"}
    if input in (theory):
        return True
    else:
        return False


def Exit(input):
    exit = {"ВЫХОД", "ЗАКАНЧИВАЕМ", "КОНЕЦ", "ВЫЙТИ", "ВЫХОДИМ", "МНЕ НАДОЕЛО"}
    if input in (exit):
        return True
    else:
        return False


def Ready(input):
    ready = {"ГТОВ", "Я ГОТОВ", "ДАВАЙ", "НАЧИНАЕМ"}
    if input in (ready):
        return True
    else:
        return False


def GoOn(input):
    ready = {"ПРОДОЛЖИМ", "ДАЛЕЕ", "ДАВАЙ", "НАЧИНАЕМ"}
    if input in (ready):
        return True
    else:
        return False